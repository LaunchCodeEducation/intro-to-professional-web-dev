.. _exercises-more-on-functions:

Exercises: More on Functions
============================

Arrr! Welcome back, pirates. 

Practice Your Skills
--------------------

First, create an anonymous function and practice how to use the map method.

A. Create an anonymous function and set it equal to a variable. Your function
   should:

   a. If passed a number, return the tripled value.

      :ref:`Check your solution <more-on-functions-exercise-solutionsAa>`. 

   b. If passed a string, return the string "ARRR!"
   c. If NOT passed a number or string, return the data unchanged.

      :ref:`Check your solution <more-on-functions-exercise-solutionsAc>`. 

   d. `Build your function here <https://repl.it/@launchcode/MoreFunctionsExercises02>`__, and be sure to test it.


#. Add to your code! Use your function and the :ref:`map method <map-method>` to
   change the array ``['Elocution', 21, 'Clean teeth', 100]`` as follows:

   #. Triple all the numbers.
   #. Replace the strings with "ARRR!"
   #. Print the new array to confirm your work.

Raid a Shuttle
--------------

You may still be wondering *Why would I ever use an anonymous
function?* For today's mission, of course! 

You need to hack into the shuttle code and steal supplies. Since the
LaunchCode TAs keep a sharp eye on the shuttle goodies, you can't just add new functions
like ``siphonFuel`` or ``lootCargo``. You need to be more sneaky.

Clever.

Invisible.

*Anonymous*.

The first mate swiped a copy of the code you need to hack:

.. sourcecode:: js
   :linenos:

   function checkFuel(level) {
      if (level > 100000){
         return 'green';
      } else if (level > 50000){
         return 'yellow';
      } else {
         return 'red';
      }
   }

   function holdStatus(arr){
      if (arr.length < 7) {
         return `Spaces available: ${7 - arr.length}`;
      } else if (arr.length > 7){
         return `Over capacity by ${arr.length - 7} items.`
      } else {
         return "Full";
      }
   }

   let fuelLevel = 200000;
   let cargoHold = ['meal kits', 'space suits', 'first-aid kit', 'satellite', 'gold', 'water', 'AE-35 unit'];

   console.log("Fuel level: "+ checkFuel(fuelLevel));
   console.log("Hold status: "+ holdStatus(cargoHold));

`Hack the code at repl.it <https://repl.it/@launchcode/MoreFunctionsExercises01>`__.

C. First, steal some fuel from the shuttle:

   #. Define an anonymous function and set it equal to a variable with a
      normal, non-suspicious name.  The function takes one parameter. This
      will be the fuel level on the shuttle.

      :ref:`Check your solution <more-on-functions-exercise-solutionsCa>`. 

   #. You must siphon off fuel without alerting the TAs.  Inside your function,
      you want to reduce the fuel level as much as possible WITHOUT changing the
      color returned by the ``checkFuel`` function.
   #. Once you figure out how much fuel to pump out, return that value.

      :ref:`Check your solution <more-on-functions-exercise-solutionsCc>`. 

   #. Decide where to best place your function call to gather our new fuel.
   
   .. admonition:: Tip
   
      Be sure to test your function! Those bilge rat TAs will notice if they
      lose too much fuel.

#. Next, liberate some of that glorious cargo.

   #. Define another anonymous function with an array as a parameter, and
      set it equal to another innocent variable.
   #. You need to swipe two items from the cargo hold.  Choose well. Stealing
      water ain't gonna get us rich.  Put the swag into a new array and return
      it from the function.
   #. The cargo hold has better security than the fuel tanks.  It counts how
      many things are in storage. You need to replace what you steal with
      something worthless.  The count MUST stay the same, or you'll get caught
      and thrown into the LaunchCode brig.
   #. Don't get hasty, matey! Remember to test your function.

#. Finally, you need to print a receipt for the accountant. Don't laugh! That
   genius knows MATH and saves us more gold than you can imagine.

   #. Define a function called ``irs`` that can take ``fuelLevel`` and
      ``cargoHold`` as arguments.

      :ref:`Check your solution <more-on-functions-exercise-solutionsEa>`. 

   #. Call your anonymous fuel and cargo functions from within ``irs``.
   #. Use a template literal to return, ``"Raided _____ kg of fuel from the
      tanks, and stole ____ and ____ from the cargo hold."``

      :ref:`Check your solution <more-on-functions-exercise-solutionsEc>`. 
