Exercises
=========

JSON
----

1. Which of the following three code snippets is correct JSON syntax? Why are the other two options incorrect?

.. sourcecode:: js

   {
       type: "dog",
       name: "Bernie",
       age: 3
   }

.. sourcecode:: js

   {
       "type": "dog",
       "name": "Bernie",
       "age": 3
   }

.. sourcecode:: js

   {
       "type": 'dog',
       "name": 'Bernie',
       "age": 3
   }

2. Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

.. sourcecode:: js

   {
       "animals": [
           {
               "type": "dog",
               "name": "Bernie",
               "age": 3
           },
           {
               "type": "cat",
               "name": "Draco",
               "age": 2
           }
       ]
   }

.. sourcecode:: js

   {
       [
          {
               "type": "dog",
               "name": "Bernie",
               "age": 3
           },
           {
               "type": "cat",
               "name": "Draco",
               "age": 2
           } 
       ]
   }

.. sourcecode:: js

   [
        {
            "type": "dog",
            "name": "Bernie",
            "age": 3
        },
        {
            "type": "cat",
            "name": "Draco",
            "age": 2
        } 
    ]


Fetch
-----

#. Create a file called ``fetch_planets.html``.
   In your terminal, type ``touch fetch_planets.html``. 

#. Open the file in VSCode and add the preliminary HTML:

   .. sourcecode :: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>Fetch Planets</title>
            <script>
               window.addEventListener("load", function() {
                  // TODO: fetch planets JSON
               });
            </script>
         </head>
         <body>
            <h1>Destination</h1>
		<div id="destination">
		</div>
         </body>
      </html>

#. The URL where our planet data is located is: ``"https://handlers.education.launchcode.org/static/planets.json"``.
   Add the code to fetch this URL inside the load event listener on line 6:

   .. sourcecode :: js
      :linenos:

      window.addEventListener("load", function() {
         fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response) {
            // TODO: do something after fetching and receiving a response
         });
      });

#. Peek the response returned in the request with a print statement:

   .. sourcecode :: js
      :linenos:

      window.addEventListener("load", function() {
         fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response) {
            console.log(response);
         });
      });

   Copy the file path of this HTML file and paste it as the URL in your browser.
   You won't see much on the page yet. Open your developer tools and examine both the 
   *Console* tab for the response value, as well as the *Network* tab for the request status.

#. Use the ``.json()`` method on your response now to see more of the data in the console:

   .. sourcecode :: js
      :linenos:

      window.addEventListener("load", function() {
         fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response) {
            response.json().then(function(json) {
               console.log(json);
            });
         });
      });
   
   What data type do you see printed? 

#. Replace your ``console.log(json)`` with the following to view a portion of the JSON 
   into the app. 

   .. sourcecode :: js
      :linenos:

      const destination = document.getElementById("destination");
      destination.innerHTML = `<h3>Planet ${json[0].name}</h3>`;

   Refresh the page to see some new data in your HTML. 
   Play around by changing the index number. Does the planet name change?
   Can you change the planet's property being printed?

#. TODO: LAST INSTRUCTIONS

   .. sourcecode :: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>Fetch Planets</title>
            <script>
               window.addEventListener("load", function() {
                  let planetData = [];
                  fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response) {
                     response.json().then(function(json) {
                        planetData = json;
                     });
                  });
                  const destination = document.getElementById("destination");
                  let index = 0;
                  destination.addEventListener("click", function(){
                     destination.innerHTML = `
                           <div>
                              <h3>Planet ${planetData[index].name}</h3>
                              <img src=${planetData[index].image} height=250></img>
                           </div>
                        `;
                     index = (index + 1) % planetData.length;
                  });
               });
            </script>
         </head>
         <body>
            <h1>Destination</h1>
            <div id="destination">
               <h3>Planet</h3>
            </div>
         </body>
      </html>
