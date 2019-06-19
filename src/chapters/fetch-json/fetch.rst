Fetching Data
=============

Now that we know what an API, let's use one to update a web page. Let's use a weather API
to add weather data to a webpage. The URL for this special LaunchCode weather API is
``https:://weather.education.launchcode.org``.

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
add that data to a Launch Status website.

.. admonition:: Example

   Launch Status web page.

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


* Show example usage of fetch
* Point out the important parts of the code
* Update the web page using data from a response


* In depth about Promises and asynchronous cycle of network requests
* Familiar with terms AJAX and XHR (where to do this?)
