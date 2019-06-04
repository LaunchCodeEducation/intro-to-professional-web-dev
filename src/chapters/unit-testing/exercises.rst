Exercises: Unit Testing
========================

In many of your previous coding tasks, you had to verify that your code
worked before moving to the next step. This often required you to add
``console.log`` statements to your code to check the value stored in a variable
or returned from a function. This approach finds and fixes syntax, reference,
or logic errors AFTER you write your code.

In this chapter, you learned how to use unit testing to solve coding errors.
Even better, you learned how to PREVENT mistakes by writing test cases before
completing the code. The exercises below offer practice with using tests to
find bugs, and the studio asks you to implement TDD.

Automatic Testing to Find Errors
---------------------------------

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
5. We do not really need a function to do this, but it provides good practice
for writing test cases.

Note that the repl.it contains three files:

a. ``checkFive.js``, which holds the code for the function,
b. ``checkFive.spec.js``, which will hold the testing code,
c. ``index.js`` which holds special code to make Jasmine work.

.. warning::

   Do NOT change the code in ``index.js``. Messing with this file will disrupt
   the automatic testing.

.. _export-syntax:

#. We need to add a few lines to ``checkFive.js`` and ``checkFive.spec.js`` to
   get them to talk to each other.

   a. ``checkFive.spec.js`` needs to access ``checkFive.js``, and we also need
      to import the ``assert`` testing function. Add the following code to
      ``checkFive.spec.js``:

      .. sourcecode:: js
         :linenos:

         const checkFive = require('../checkFive.js');
         const assert = require('assert');

      The ``checkFive`` variable now calls the function written inside
      ``checkFive.js``.

   b. To make the ``checkFive`` function available to the spec file, add the
      following code to the bottom of ``checkFive.js``:

      .. sourcecode:: js

         module.exports = checkFive;

#. Write your first test for the ``checkFive`` function. In the
   ``checkFive.spec.js`` file, add a ``describe`` function with one ``it``
   clause:

   .. sourcecode:: js

      const checkFive = require('../checkFive.js');
      const assert = require('assert');

      describe("checkFive", function(){

         it("Descriptive feedback...", function(){
            //code here...
         });

      });

#. Now write a test to see if ``checkFive`` produces the correct output when
   passed a number *less than 5*.

   a. First, replace ``Descriptive feedback...`` with a DETAILED message. This
      is the text that the user will see if the test *fails*. Do NOT skimp on
      this. Refer back to the :ref:`Specifications and Assertions <feedback>`
      section to review best practices.
   b. Define the variable ``output``, and initialize it by passing a value of
      ``2`` to ``checkFive``.

      .. sourcecode:: js

         const checkFive = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            it("Descriptive feedback...", function(){
               let output = checkFive(2);
            });

         });

   c. Now use the ``assert`` function to check the result:

      .. sourcecode:: js

         const checkFive = require('../checkFive.js');
         const assert = require('assert');

         describe("checkFive", function(){

            it("Descriptive feedback...", function(){
               let output = checkFive(2);
               assert.strictEqual(output, "2 is less than 5.");
            });

         });

   d. Run the test script and examine the results. The test should pass and
      produce output similar to:

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
         1) checkFive should return 'num' is less than 5 when passed a number smaller than 5.
         Message:
            AssertionError [ERR_ASSERTION]: Input A expected to strictly equal input B:
            + expected - actual

            - '2 is greater than 5.'
            + '2 is less than 5.'

   f. Change line 3 back.

   .. note::

      We do NOT need to check every possible value that is less than 5. Testing a single
      example is sufficient to check that part of the function.

#. Add two more ``it`` clauses inside ``describe``---one to test what happens
   when ``checkFive`` is passed a value greater than 5, and the other to test
   when the value equals 5.


Try One on Your Own
--------------------

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

#. Set up the ``RPS.js`` and ``RPS.spec.js`` files to talk to each other. If
   you need to review how to do this, re-read the
   :ref:`previous exercise <export-syntax>`, or check
   :ref:`Hello Jasmine <hello.js>`.

#. Write a test in ``RPS.spec.js`` to check if ``whoWon`` behaves correctly
   when the players tie (both choose the same option). Click "Run" and examine
   the output. SPOILER ALERT: The code for checking ties is correct in
   ``whoWon``, so the test should pass. If it does not, modify your ``it``
   statement.

#. Write tests (one at a time) for each of the remaining cases. Run the tests
   after each addition, and modify the code as needed. There is one mistake in
   ``whoWon``. You might spot it on your own, but try to use automated
   testing to identify and fix it.

Bonus Mission
--------------

What if something OTHER than ``'rock'``, ``'paper'``, or ``'scissors'`` is
passed into the ``whoWon`` function? Modify the code to deal with the
possibility.

Don't forget to add another ``it`` clause in ``RPS.spec.js`` to test for this
case.
