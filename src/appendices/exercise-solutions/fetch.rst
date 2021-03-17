.. _fetch-exercise-solutions:

Exercise Solutions: Fetch
=========================

.. _fetch-exercise-solutions1:

1. **Fetch the URL**

   .. sourcecode:: js
      :linenos:

      window.addEventListener("load", function() {
         fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response){
            // TODO: do something after fetching and receiving a response
         });
      });

   :ref:`Back to the exercises <exercises-fetch>`

.. _fetch-exercise-solutions3:

3. **Use the .json() method to print response data:**

   .. sourcecode:: js
      :linenos:

      fetch("https://handlers.education.launchcode.org/static/planets.json").then(function(response){
         response.json().then(function(json) {
            console.log(json);
         });
      });


   Your ``console.log`` statement should return the same array of 6 JSON objects containing planetary data found `here <https://handlers.education.launchcode.org/static/planets.json>`__.

   :ref:`Back to the exercises <exercises-fetch>`

.. _fetch-exercise-solutions5:

5. **Capture the JSON data:**

   .. sourcecode:: js
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

   We can tell that our fetch works because the JSON array is printed to the console.
   However, you should also see an error in the console related to the template literal
   using ``json[0].name``.
   This error occurs because of the asynchronous nature of JavaScript. Although we
   now have ``json`` defined outside of the fetch request, at the point in time that
   we seek it for the template literal, we haven't yet received the json data.
   One clue that asynchronism is at play: the error appears before the printed JSON.

   :ref:`Back to the exercises <exercises-fetch>`

.. _fetch-exercise-solutions7:

7. **Dynamically change planet info displayed**

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

   :ref:`Back to the exercises <exercises-fetch>`