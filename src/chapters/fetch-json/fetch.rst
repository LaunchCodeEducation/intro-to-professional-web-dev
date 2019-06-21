Fetching Data
=============

Now that we know what an API is, let's use one to update a web page. Let's use a weather API
to add weather data to a webpage. The URL for this special LaunchCode weather API is
`<https://api.education.launchcode.org/weather>`_.

Example JSON returned from weather API.

.. sourcecode:: js

   {
      "temp": 67,
      "windSpeed": 5,
      "tempMin": 50,
      "tempMax": 71,
      "status": "Sunny",
      "chanceOfPrecipitation": 20,
      "zipcode": 63108
   }

We can see that this API returns useful information like ``temp`` and ``windSpeed``. Our goal is to
add that data to a Launch Status web page. Note this API is for instruction purposes and does not
contain real time data.

.. admonition:: Example

   Launch Status web page, which we will add weather data to.

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>Launch Status</title>
         </head>
         <body>
            <h1>Launch Status</h1>
            <h3>Weather Conditions</h3>
            <div id="weather-conditions">
               <!-- TODO: dynamically add html about weather using data from API -->
            </div>
         </body>
      </html>


``fetch`` Function
------------------

.. index:: !fetch

To request the weather data, we will use the ``fetch`` function. ``fetch`` is a global
function that requests, or fetches resources such as data from an API.

Take note of two necsseary aspects of the ``fetch`` function:

1. The URL of where the data is located.

   * For this example it will be ``'https://api.education.launchcode.org/weather'``

2. A response handler function to utilize the data that is being fetched.

   * For this example it will be ``function(response){...};``

.. admonition:: Example

   Notice a string URL is passed to ``fetch``. Also notice the anonymous function that
   has a ``response`` parameter, that is the request handler function. The ``then``
   function will be explained soon.

   .. sourcecode:: js

      fetch('https://api.education.launchcode.org/weather').then( function(response) {
         console.log(response);
      } );

   In this example we are requesting data from ``https://api/education.launchcode.org/weather`` and our response handler (the function) simply logs the response to the console.

``fetch`` Example
-----------------

Now let's add ``fetch`` in the Launch Status web page.

.. admonition:: Example

   A ``<script>`` tag has been added that includes:

   1. A *load* event handler on line 5
   2. A ``fetch`` and response handler function on line 6
   3. A ``console.log(response);`` on line 7 that prints out the response object

   .. replit:: html
      :linenos:
      :slug: fetch-weather-pt1

      <html>
         <head>
            <title>Launch Status</title>
            <script>
               window.addEventListener("load", function() {
                  fetch("weather.json").then( function(response) {
                     console.log(response);
                  } );
               });
            </script>
         </head>
         <body>
            <h1>Launch Status</h1>
            <h3>Weather Conditions</h3>
            <div id="weather-conditions">
               <!-- TODO: dynamically add html about weather using data from API -->
            </div>
         </body>
      </html>

Let's break down how ``fetch`` works. A URL is passed to ``fetch`` as a parameter, that causes
an HTTP GET request to be sent from the browser to the API. Remember that HTTP is a request then
response protocol. The response handler function, as the name implies, handles the response sent
back from the API. Using the data in the response, the web page can be updated using DOM methods.

View the GET Request
^^^^^^^^^^^^^^^^^^^^
We can see evidence of the GET request by following these steps:

1. Open the `Launch Status web page <https://fetch-weather-pt1--launchcode.repl.co/>`_ in it's own tab.
2. Open developer tools.
3. Open the *Network* tab in developer tools.

.. figure:: figures/weather-developer-tools.png
       :alt: Screen shot showing developer tools open with the network call to the API highlighted.

       The GET request to the Weather API highlighted in developer tools.

In the above image you can see the web page has been rendered on the left. In the developer tools
the GET request to the Weather API has been highlighted along with the response from that request.
The response shows the JSON data that was sent. In the console output you can see the ``Response``
object has been logged. We will use that object next.

Response Object
^^^^^^^^^^^^^^^
The response to the GET request is contained in a ``response`` object that is an instance of the
`Response class <https://developer.mozilla.org/en-US/docs/Web/API/Response>`_. The Response class
represents a Response and has methods to gaining access to the status and data of a response.

.. admonition:: Example

   On line 7 the ``json()`` method is used to gain access to the JSON data contained in the response.
   
   Line 8 logs the JSON to the console. Explanation of ``then`` is coming very soon.

   .. replit:: html
      :linenos:
      :slug: fetch-weather-pt2

      <html>
         <head>
            <title>Launch Status</title>
            <script>
               window.addEventListener("load", function() {
                  // Access the JSON in the response
                  response.json().then( function(json) {
                     console.log(json);
                  });
               });
            </script>
         </head>
         <body>
            <h1>Launch Status</h1>
            <h3>Weather Conditions</h3>
            <div id="weather-conditions">
               <!-- TODO: dynamically add html about weather using data from API -->
            </div>
         </body>
      </html>

   **Console Output**
   ::

      Object { temp: 67, windSpeed: 5, tempMin: 50, tempMax: 71, status: "Sunny", chanceOfPrecipitation: 20, zipcode: 63108 }

Use the DOM and JSON Data to Update the Page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now that we have JSON weather data we can add HTML elements to the page to show the data.

.. admonition:: Example



   .. replit:: html
      :linenos:
      :slug: fetch-weather-pt3

      <html>
         <head>
            <title>Launch Status</title>
            <script>
               window.addEventListener("load", function() {
                  // Access the JSON in the response
                  response.json().then( function(json) {
                     const div = document.getElementById('weather-conditions');
                     // Add HTML that includes the JSON data
                     div.innerHTML = `
                        <ul>
                           <li>Temp ${json.temp}</li>
                           <li>Wind Speed ${json.windSpeed}</li>
                           <li>Status ${json.status}</li>
                           <li>Chance of Precip ${json.chanceOfPrecipitation}</li>
                        </ul>
                     `;
                  });
               });
            </script>
         </head>
         <body>
            <h1>Launch Status</h1>
            <h3>Weather Conditions</h3>
            <div id="weather-conditions">
               <!-- Weather data is added here dynamically. -->
            </div>
         </body>
      </html>

.. figure:: figures/weather-data-on-page.png
   :alt: Screen shot of browser showing Launch Status web page with the weather data in HTML.

   Weather data added to web page.


Things left to discuss

* NOTE about seeing many other ways to request data online (jQuery.get, XmlHttpRequest, ...)
* NOTE about fetch can also be used to sent POST and PUT requests. maybe link to MDN
* WARNING that fetch does NOT work in IE, be sure to say that Edge is ok. Provide link to site that helps them pick a different browser.
* In depth about Promises and asynchronous cycle of network requests
* Mention and define AJAX and XHR (where to do this?) -- a note after XmlHttpRequest, and jQuery
