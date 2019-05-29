Exercises: Unit Testing
========================

In many of your previous coding tasks, you had to verify that your code
worked before moving to the next step. Many times, this required you to add
``console.log`` statements to your code to check the values stored in the
varialbles or returned from a function.

You probably also encountered a number of bugs in your code samples that
required you to step through your programs to find syntax, reference, or logic
errors. You applied ``console.log`` and other tricks to help fix the
mistakes.

The following exercises begin with a debugging review and continue with an
introduction to automatic testing. The goal is to write code to test your code,
rather than throwing in ``console.log`` statements to check your work.

Manual Testing
---------------

Assume that a team member wrote the following code:

.. replit:: js
   :slug: UnitTestingExercises01
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

   let response = input.question("Enter the launch code (must be an integer): ");

   console.log(createLaunchOutput(response));

The program must accomplish the following:

#. If the user enters a number divisible only by 2, print ``'Crew ready for
   launch. Shuttle offline.'``
#. If the user enters a number divisible only by 3, print ``'Shuttle ready for
   launch. Crew asleep.'``
#. If the user enters a number divisible by both 2 and 3, print ``'Crew and
   shuttle ready. Cleared for launch!'``
#. If the user enters a number that is NOT divisible by 2 OR 3, print ``'Crew
   and shuttle unresponsive. Launch aborted!'``
#. If the user enters a string, a decimal, or just hits return, print ``'ARRR!
   Raid yonder shuttle!'``

Test for Errors
^^^^^^^^^^^^^^^^

#. ``createLaunchOutput`` runs, so there are no syntax errors, but does the
   program produce the correct output?

   a. Consider the following inputs: 22, 33, 6, 0, and 7. What output should
      the program produce in each case?
   b. Run the code as-is and *test* it with each of the inputs. Do any of the
      values produce incorrect output?

#. Using the techniques you already learned, fix the code so that any integer
   input produces the correct output.

#. We *tested* the code with integers. What if the user types in something
   else?

   a. Add the following validation check to the ``createLaunchOutput``
      function:

      .. sourcecode:: js
         :linenos:

         function createLaunchOutput(entry) {
            let output = "";

            if (!entry.includes('.') || isNaN(entry) || entry === ' '){
               output = "ARRR! Raid yonder shuttle!";
               return output;
            }

            entry = Number(entry);
         etc...

   b. Run the updated program and *test* it with the inputs: 2.22, 'H', and ''.
      Which entries produce incorrect output?
   c. Fix the new code so that it correctly returns ``'ARRR! Raid yonder
      shuttle!'`` for the empty string, decimal values, and non-numerical
      inputs.

#. Once the code returns the correct output for all of the suggested input
   values, continue to *test* it with your own entries. Make sure your fixes
   all work.

Good! You are now ready to *automate* the testing process.

Automatic Testing
------------------

Start Small
^^^^^^^^^^^^

Let's begin with the following, simple code:

.. replit:: js
   :slug: UnitTestingExercises02
   :linenos:

   function checkFive(num){
      let result = '';
      if (num < 5){
         result = num + " is less than 5.";
      } else if (num === 5){
         result = num + " is equal to 5.";
      } else {
         result = num + "is greater than 5.";
      }

      return result;
   }

The function checks to see if a number is greater than, less than, or equal to
5. We do not really need a function to do this, but it provides a good first
practice.

Note that the repl.it contains three files:

a. ``checkFive.js``, which holds the code for the function,
b. ``checkFive.spec.js``, which will hold the testing code,
c. ``index.js`` which holds special code to make Jasmine work.

.. warning::

   Do NOT change the code in ``index.js``. Messing with this file will disrupt
   the automatic testing.

#. We need to add a few lines to ``checkFive.js`` and ``checkFive.spec.js`` to
   get them to talk to each other.

   a. ``checkFive.spec.js`` needs to access ``checkFive.js``, and we also need
      to import the ``assert`` testing function. Add the following code to
      ``checkFive.spec.js``:

      .. sourcecode:: js
         :linenos:

         const test = require('../checkFive.js');
         const assert = require('assert');

      The ``test`` variable will be used to call specific functions written
      inside ``checkFive.js``.

   b. To make the ``checkFive`` function available to ``test``, add the
      following code to the bottom of ``checkFive.js``:

      .. sourcecode:: js

         module.exports = {
            checkFive: checkFive
         };

      Anything named within the ``{}`` can be called from other files using dot
      notation (e.g. ``test.checkFive(num)``).

#. Write your first test for the ``checkFive`` function.

   a. In the ``checkFive.spec.js`` file, add an empty ``describe`` function:

      .. sourcecode:: js

         const test = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            //testing code here...

         });

   b. Now add an ``it`` clause.

      .. sourcecode:: js

         const test = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            it("Descriptive feedback...", function(){
               //code here...
            });

         });

#. Let's write a test to see if ``checkFive`` produces the correct output when
   passed a number *less than 5*.

   a. First, replace ``Descriptive feedback...`` with a DETAILED message. This
      is the text that the user will see if the test *fails*. Do NOT skimp on
      this. Best practice suggests something like ``'should [DO THIS] if [THIS
      HAPPENS]'``, where the text inside the ``[]`` describes what the function
      should do when passed a specific input.
   b. Define the variable ``output``, and initialize it by passing a value of
      ``2`` to ``checkFive``.

      .. sourcecode:: js

         const test = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            it("Descriptive feedback...", function(){
               let output = test.checkFive(2);
            });

         });

   c. Now use the ``assert`` function to check the result:

      .. sourcecode:: js

         const test = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            it("Descriptive feedback...", function(){
               let output = test.checkFive(2);
               assert.equal(output, "2 is less than 5.");
            });

         });

   d. Run the test script and examine the results. The test should have
      passed and prodced output similar to:

      ::

         Started
         .

         1 spec, 0 failures
         Finished in 0.006 seconds

   e. Now change line 3 in ``checkFive.js`` to ``if (num > 5)`` and rerun
      the test. The output should look similar to :

      ::

         Started
         F

         Failures:
         1) checkFive should return 'num is less than 5.' if given a number less than 5
         Message:
            AssertionError [ERR_ASSERTION]: '2 is greater than 5.' == '2 is less than 5.'

   f. Change line 3 back.

   .. note::

      We do NOT need to check every possible value that is less than 5. Testing a single
      example is sufficient to check that part of the function.

#. Add two more ``it`` clauses inside ``describe`` to test what happens when
   ``checkFive`` is passed a value greater than 5 or equal to 5.


Try One on Your Own
^^^^^^^^^^^^^^^^^^^^
Time for Rock, Paper, Scissors! The function below takes the choices
(``'rock'``, ``'paper'``, or ``'scissors'``) of two players as its parameters.
It then decides which player won the match and returns a string.

.. replit:: js
   :slug: UnitTestingExercises03
   :linenos:

   function whoWon(player1,player2){

      if (player1 === player2){
         return 'TIE!';
      }

      if (player1 === 'rock' && player2 === 'paper'){
         return 'Player 2 wins!';
      }

      if (player1 === 'paper' && player2 === 'scissors'){
         return 'Player 2 wins!';
      }

      if (player1 === 'scissors' && player2 === 'rock '){
         return 'Player 2 wins!';
      }

      return 'Player 1 wins!';
   }

#. Set up the ``RPS.js`` and ``RPS.spec.js`` files to talk to each other.

#. Write at least two tests in ``RPS.spec.js`` to check if ``whoWon`` behaves
   correctly. There is one mistake in the code. You might spot it on your own,
   but try to use automated testing to identify it.

Bonus Mission
--------------

What if something OTHER than ``'rock'``, ``'paper'``, or ``'scissors'`` is
passed into the ``whoWon`` function? Modify the code to deal with the
possibility.

Don't forget to add another ``it`` clause in ``RPS.spec.js`` to test for this
case.
