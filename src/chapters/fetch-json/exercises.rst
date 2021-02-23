Exercises
=========

.. _exercises-JSON:

JSON
----

1. Which of the following three code snippets is correct JSON syntax? Why are the other two options incorrect?

   a. 
      .. sourcecode:: js

         {
            type: "dog",
            name: "Bernie",
            age: 3
         }

   b. 

      .. sourcecode:: js

         {
            "type": "dog",
            "name": "Bernie",
            "age": 3
         }
   
   c.

      .. sourcecode:: js

         {
            "type": 'dog',
            "name": 'Bernie',
            "age": 3
         }

   :ref:`Check your solution <JSON-exercise-solutions1>`. 

2. Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

   a.

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

   b.

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

   c.

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

#. Go to the directory where you are working on your LC101 homework. Create a file called 
   ``fetch_planets.html`` using ``touch``.

#. Open the file in VSCode and add the preliminary HTML:

   .. sourcecode :: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>Fetch Planets</title>
            <script>
               window.addEventListener("load", function(){
                  // TODO: fetch planets JSON
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

#. The URL where our planet data is located is: ``"https://handlers.education.launchcode.org/static/planets.json"``.
   Add the code to fetch this URL inside the load event listener.

   .. sourcecode :: js
      :linenos:

      window.addEventListener("load", function() {
         fetch(URL).then(function(response){
            // TODO: do something after fetching and receiving a response
         });
      });

#. Peek at the ``response`` returned in the request by adding a print statement
   inside of the function.

   Copy the file path of your HTML file and paste it as the URL in your browser.
   You won't see much on the page yet. Open your developer tools and examine both the 
   *Console* tab for the response value, as well as the *Network* tab for the request status.

#. Use the ``.json()`` method on your response now to see more of the data in the console:

   .. sourcecode :: js
      :linenos:

      response.json().then(function(json) {
         console.log(json);
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

#. Now, what happens if we move those last lines we added to outside and after 
   the fetch request? Since ``json`` hasn't been defined outside of the 
   ``response.json()`` method yet, in order to move the template literal that uses
   that ``json`` variable, we'll need to also initiate it outside of the function 
   call. 
   Let's also put our print statement back so we can verify that our fetch works.

   .. sourcecode :: js
      :linenos:

      window.addEventListener("load", function() {
         let json = [];
         fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response){
            response.json().then(function(json) {
               console.log(json);
            });
         });
         const destination = document.getElementById("destination");
         destination.innerHTML = `<h3>Planet ${json[0].name}</h3>`;
      });

   Refresh the page and try this. See any data? See anything of note in the console?

   We can tell that our fetch works because the JSON array is printed to the console.
   However, you should also see an error in the console related to the template literal
   using ``json[0].name``.
   This error occurs because of the asynchronous nature of JavaScript. Although we
   now have ``json`` defined outside of the fetch request, at the point in time that
   we seek it for the template literal, we haven't yet received the json data.
   One clue that asynchronism is at play, the error appears before the printed JSON.


#. Our last task left us with some knowledge about where and how we can use the 
   fetched data, but we don't really want to keep those changes. Instead, how 
   about we use an event to change the planet information we see? Let's move
   the DOM manipulation to inside a click handler.

   .. sourcecode :: js
      :linenos:

      fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response){
         response.json().then(function(json) {
            const destination = document.getElementById("destination");
            destination.addEventListener("click", function(){
               destination.innerHTML = `
                  <div>
                     <h3>Planet ${json[0].name}</h3>
                     <img src=${json[0].image} height=250></img>
                  </div>
               `;
            });
         });
      });

   Now, after refreshing the page, you can click on the ``Planet`` header to make
   the name and image appear. 
   Take note, we're still fetching on load, just not displaying the data until the
   the header is clicked.

#. For fun and good measure, let's dynamically change which planet's info we're displaying each time
   the header is clicked. To do this, 
   
      #. We declare a counter variable, ``index`` that changes each time a 
         ``click`` event takes place.
      #. We then use the value of ``index`` as the position in the planets array to 
         use in the template literal. 
      #. Finally, since we want to cap the value of ``index`` so that it does not 
         exceed the length of the planets array, we'll use a modulo to control how 
         large ``index`` can get.

   .. sourcecode :: js
      :linenos:

      fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response) {
         response.json().then(function(json) {
            const destination = document.getElementById("destination");
            let index = 0;
            destination.addEventListener("click", function(){
               destination.innerHTML = `
                  <div>
                     <h3>Planet ${json[index].name}</h3>
                     <img src=${json[index].image} height=250></img>
                  </div>
               `;
               index = (index + 1) % json.length;
            });
         });
      });

   Et voila! Our destination changes on each click!

   .. figure:: ./figures/planet-destinations.gif
      :alt: Clicking through destinations.

   Put on your planetary shoes. We are moving through planets!


