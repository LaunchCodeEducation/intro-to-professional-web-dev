.. _more-on-functions-exercise-solutions:

Exercise Solutions: More on Functions
=====================================


A. Create an anonymous function.

   .. _more-on-functions-exercise-solutionsAa:

   a. 
      .. sourcecode:: js
         :linenos:

         let practice = function(myArg) {
            if (typeof myArg === "number") {
               return myArg * 3;
            } 
         }
   
   .. _more-on-functions-exercise-solutionsAc:

   c. 
      .. sourcecode:: js
         :linenos:

         let practice = function(myArg) {
            if (typeof myArg === "number") {
               return myArg * 3;
            } else if (typeof myArg === "string") {
               return "ARRR!";
            } else {
               return myArg;
            }

         }

   :ref:`Back to the exercises <exercises-more-on-functions>`


C. Create another anonymous function.

   .. _more-on-functions-exercise-solutionsCa:

   a. 
      .. sourcecode:: js
         :linenos:

         let nonSuspiciousFunction = function(a) { 
         
         }

   .. _more-on-functions-exercise-solutionsCc:

   c. 
      .. sourcecode:: js
         :linenos:

         let nonSuspiciousFunction = function(a) {
            if (checkFuel(a) === 'green') {
               return a - 100001;
            }
            else if (checkFuel(a) === 'yellow') {
               return a - 50001;
            }
            else {
               return a;
            }
         };


   :ref:`Back to the exercises <exercises-more-on-functions>`

E. Print a receipt.

   .. _more-on-functions-exercise-solutionsEa:

   a. 
      .. sourcecode:: js
         :linenos:

         let irs = function(levelOfFuel, itemsInCargo) {
            
         }


   .. _more-on-functions-exercise-solutionsEc:

   c. 
      .. sourcecode:: js
         :linenos:

         let irs = function(levelOfFuel, itemsInCargo {
            let arr = deckMops(itemsInCargo);
            return `Raided ${nonSuspiciousFunction(fuelLevel)} kg of fuel from the tanks, and stole ${arr[0]} and ${arr[1]} from the cargo hold.`
         }


   :ref:`Back to the exercises <exercises-more-on-functions>`