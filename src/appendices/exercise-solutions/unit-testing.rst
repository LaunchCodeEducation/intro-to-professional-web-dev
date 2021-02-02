.. _unit-testing-exercise-solutions:

Exercise Solutions: Unit Testing
================================

Automatic Testing to Find Errors
--------------------------------

.. _unit-testing-exercise-solutionsA1:

1. Get the sourcecode file and the test code file to talk to each other.

   a. Add two ``require`` statements.

      ``checkFive.spec.js``:

      .. sourcecode:: js
         :linenos:

         const test = require('../checkFive.js');
         const assert = require('assert');

   :ref:`Back to the exercises <exercises-unit-testing>`

3. Check that ``checkFive`` produces the correct output when passed a number less than 5.

   a. Write a descriptive test name.

      .. _unit-testing-exercise-solutionsA3a:

      ``checkFive.spec.js``:

      .. sourcecode:: js
         :linenos:

         it("returns 'num is less than 5' when num < 5.", function(){
            // test code //
         });

   c. Use ``assert``.

      .. _unit-testing-exercise-solutionsA3c:

      ``checkFive.spec.js``:

      .. sourcecode:: js

         assert.strictEqual(output, "2 is less than 5.");

   e. Change the sourcecode file and see that the test fails.

      .. _unit-testing-exercise-solutionsA3e:

      ``checkFive.js``:

      .. sourcecode:: js
         :linenos:

         if (num > 5) {
            // sourcecode //
         }

   :ref:`Back to the exercises <exercises-unit-testing>`

.. _unit-testing-exercise-solutionsB:

Try One on Your Own
-------------------

1. Set up the ``RPS.js`` and ``RPS.spec.js`` files to talk to each other.

   .. _unit-testing-exercise-solutionsB1:

   ``RPS.js``:

   .. sourcecode:: js
      :linenos:

      module.exports = {
            whoWon: whoWon
      };

   ``RPS.spec.js``:

   .. sourcecode:: js
      :linenos:

      const test = require('../RPS.js');
      const assert = require('assert');

   :ref:`Back to the exercises <exercises-unit-testing>`

3. Two sample tests.

   .. _unit-testing-exercise-solutionsB3:

   ``RPS.spec.js``:

   .. sourcecode:: js 
      :linenos:

      describe("whoWon", function(){

         it("returns 'Player 2 wins!' if P1 = rock & P2 = paper", function(){
            let output = test.whoWon('rock','paper');
            assert.strictEqual(output, "Player 2 wins!");
         });

         it("returns 'Player 2 wins!' if P1 = paper & P2 = scissors", function(){
            let output = test.whoWon('paper','scissors');
            assert.strictEqual(output, "Player 2 wins!");
         });

         // other test cases //

      }
   
Typo to fix:
^^^^^^^^^^^^ 
	
In ``RPS.js``, there is a conditional block that checks if ``player1`` plays ``'scissors'`` and ``player2`` plays ``'rock '``.
The ``'rock '`` string contains a trailing space that should be removed.

:ref:`Back to the exercises <exercises-unit-testing>`
