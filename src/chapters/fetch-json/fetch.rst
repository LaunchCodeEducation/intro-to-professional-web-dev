Fetching Data
=============

Now that we know what an API, let's use one to update a web page. Let's use a weather API
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
            <!-- TODO: dynamically add html about weather using data from API -->
         </body>
      </html>


``fetch`` Function
------------------

.. index:: !fetch

To request the weather data, we will use the ``fetch`` function. ``fetch`` is a global
function that requests, or fetches, resources such as data from an API.

Two important parts of fetching data are:

1. The URL of where the data is located.

   * For this example it will be ``'https://api.education.launchcode.org/weather'``

2. A response handler function to utilize the data that is being fetched.

.. admonition:: Example

   Notice a string URL is passed to ``fetch``. Also notice the anonymous function that
   has a ``response`` parameter, that is the request handler function. The ``then``
   function will be explained very soon.

   .. sourcecode:: js

      fetch('https://api.education.launchcode.org/weather').then( function(response) {
         console.log(response);
      } );

Let's break down how ``fetch`` works. A URL is passed to ``fetch`` as a parameter, that causes
an HTTP GET request to be sent from the browser to the API. Remember that HTTP is a request then
response protocol. The response handler function, as the name implies, handles the response sent
back from the API. Using the data in the response, the web page can be updated using DOM methods.

``fetch`` Example
-----------------

Now let's add ``fetch`` in the Launch Status web page.

.. admonition:: Example

   On line 4 a ``<script>`` tag has been added that includes:

   1. A *load* event handler on line 5
   2. A ``fetch`` and response handler function on line 6
   3. A ``console.log(response);`` on line 7  

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
            <!-- TODO: dynamically add html about weather using data from API -->
         </body>
      </html>

   Open the repl.it link. Then 




Things left to discuss
* Show example usage of fetch
* Point out the important parts of the code
* show example of network request in network tab?
* Update the web page using data from a response
* something about HTTP requests
* NOTE about seeing many other ways to request data online (jQuery.get, XmlHttpRequest, ...)
* NOTE about fetch can also be used to sent POST and PUT requests. maybe link to MDN
* WARNING that fetch does NOT work in IE, be sure to say that Edge is ok. Provide link to site that helps them pick a different browser.
* In depth about Promises and asynchronous cycle of network requests
* Familiar with terms AJAX and XHR (where to do this?)
