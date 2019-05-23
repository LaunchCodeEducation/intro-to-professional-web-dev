Exercises: Unit Testing
========================

In many of your previous coding tasks, you had to verify that your code
worked before moving to the next step. Usually, this required you to add
``console.log`` statements to your code to check the values stored in the
varialbles or returned from a function.

You probably also encountered a number of bugs in your code samples that
required you to step through your programs to find syntax, reference, or logic
errors. You applied ``console.log`` and other tricks to help fix the
mistakes.

The following exercises begin with a debugging review and continue with an
introduction to automatic testing. The goal is to write code to test your code
rather than throwing in ``console.log`` statements to check your work.

Manual Debugging
-----------------

Assume that a team member wrote the following code:

.. sourcecode:: js
   :linenos:

   function createLaunchOutput(entry) {
      let output = "";
      
      entry = Number(entry);

      if (entry%2 === 0){
         output = "Crew ready for launch. Shuttle offline.";
      } else if (entry%3 === 0){
         output = "Shuttle ready for launch. Crew asleep.";
      } else if (entry%2 === 0 && entry%3 === 0){
         output = "Crew and shuttle ready. Cleared for launch!";
      }

      return output;
   }

   const input = require(`readline-sync`);

   let response = input.question("Enter an integer: ");
   console.log(createLaunchOutput(response));

The program must accomplish the following:

#. If the user enters a number divisible only by 2, print ``'Crew ready for launch. Shuttle offline.'``
#. If the user enters a number divisible only by 3, print ``'Shuttle ready for launch. Crew asleep.'``
#. If the user enters a number divisible by both 2 and 3, print ``'Crew and shuttle ready. Cleared for launch!'``
#. If the user enters a number that is NOT divisible by 2 OR 3, print ``'Crew and shuttle unresponsive. Launch aborted!'``
#. If the user enters a string, a decimal, or just hits return, print ``'ARRR! Raid yonder shuttle!'``

Fix the Errors
^^^^^^^^^^^^^^^

#. ``createLaunchOutput`` is flawed! It runs, so there are no syntax errors,
   but the program does not produce the correct output.

   a. First, consider the following inputs: 22, 33, 6, 0, and 7. What output
      should the program produce in each case?
   b. Run the code as-is and test it with each of the inputs. Which values
      cause errors?

#. Using the techniques you have already learned, fix the code so that any
   integer input results in the correct output.

#. We have only used integers to test the code. What if the user types in
   something else?
   
   a. Add the following validation check to the ``createLaunchOutput``
      function:
   
      .. sourcecode:: js
         :linenos:

         function createLaunchOutput(entry) {
            let output = "";

            if (!entry.includes('.') || isNaN(entry) || entry === ' '){
               output = "Invalid input.";
               return output;
            }
            
            entry = Number(entry);
         etc...

   b. Run the updated program and test it with the inputs: 2.22, 'H', and ''.
      Which entries cause errors?
   c. Fix the code so that it always generates the correct output.

Automatic Debugging
--------------------
