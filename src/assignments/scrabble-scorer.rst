Assignment #2: Scrabble Scorer
==============================

To see how far you skills have come, we are going to give you a mission to update
our *super* important Scrabble Scorer program. What, did you think you were going
to work on Mars rover code already?

The current Scrabble Scorer program will take in a word and return the Scrabble value for
that word. Below are the requirements for the new version.


Requirements
------------

#. Create an ``oldScoreKey`` object that contains the previous scoring system.
#. Create a ``transform`` function which will return a ``newScoreKey`` object.
#. Create ``scoringAlgorithms`` array to hold three scoring objects, which include the scoring functions.
#. Create a ``initialPrompt`` function that asks user what score algorithm to use.
#. Create a ``runProgram`` function to contain the starting point for your running program.

Example Output
^^^^^^^^^^^^^^
::

   Welcome to the Scrabble score calculator. Use ctrl+c to quit.

   Which scoring algorithm would you like to use?

   0 - Scrabble: The traditional scoring algorithm.
   1 - Simple Score: Each letter is worth 1 point.
   2 - Bonus Vowels: Vowels are 3 pts, consonants are 1pt
   Enter 0,1,2: 0
   Using algorithm: Scrabble

   Enter a word to be scored:  LaunchCode
   Score for 'LaunchCode': 18

   Enter a word to be scored:  Rocket
   Score for 'Rocket': 12

   Enter a word to be scored:


Detailed Requirements
---------------------

Transform
^^^^^^^^^
Currently our Scrabble Grader uses this data structure when calculating scores
using the standard Scrabble scoring algorithm.

.. sourcecode:: js
   :linenos:

   const oldScoreKey = {
      1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
      2: ['D', 'G'],
      3: ['B', 'C', 'M', 'P'],
      4: ['F', 'H', 'V', 'W', 'Y'],
      5: ['K'],
      8: ['J', 'X'],
      10: ['Q', 'Z']
   };

Write a ``transform`` function that takes in as a parameter the ``oldScoreKey``
object. ``transform(oldScoreKey)`` will return an object with the letters as keys. The keys
in the ``newScoreKey`` should be *lowercase* letters.

Example of new key storage

* ``a`` is worth ``1``
* ``j`` is worth ``8``
* ``k`` is worth ``10``


.. admonition:: Example

   Example of ``newScoreKey`` object usage.

   .. sourcecode:: js

      console.log("Scrabble scoring values for");
      console.log("letter a: ", newScoreKey.a);
      console.log("letter j: ", newScoreKey.j);
      console.log("letter z: ", newScoreKey.z);

   Console Output

   ::

      Scrabble scoring values for
      letter a:  1
      letter j:  8
      letter z:  10


Prompt User
^^^^^^^^^^^
The current Scrabble Scorer only uses one scoring algorithm. For the new version we
want to let the user pick between three algorithms. Define a ``initialPrompt`` function
that will introduce the program and then ask the user which scoring algorithm they want
to use. See Example Output above and the next section for details on available options.

Scoring Algorithms
^^^^^^^^^^^^^^^^^^
Create a ``scoringAlgorithms`` array that contains three scorer objects. Each scorer
object should have these three keys ``name``, ``description``, and ``scoreFunction``.
All three scoring algorithms are case *insensitive*, meaning that they should ignore case.

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Score Function
   * - Scrabble
     - The traditional scoring algorithm.
     - A function with a ``word`` parameter that returns a score.
       Uses ``newScoreKey`` object to determine score.
   * - Simple Score
     - Each letter is worth 1 point.
     - A function with a ``word`` parameter that returns a score.
   * - Bonus Vowels
     - Vowels are 3 pts, consonants are 1pt.
     - A function with ``word`` parameter that returns a score.

.. admonition:: Example

   Example of ``scoringAlgorithms`` object usage.

   .. sourcecode:: js

      console.log("algorithm name: ", scoringAlgorithms[0].name);
      console.log("using scoreFunction: ", scoringAlgorithms[0].scoreFunction("LaunchCode"));

   Console Output

   ::

      algorithm name:  Scrabble
      using scoreFunction:  18

Tie it All Together
^^^^^^^^^^^^^^^^^^^
Define a ``runProgram`` function that will:

1. Use ``initialPrompt`` to pick the algorithm.
2. Then prompt the user for a word to score.
3. Use the picked algorithm to determine a word score.
4. Display the score for the word.
5. Repeat steps 1 to 4 until program is stopped.


Submitting Your Work
--------------------

.. todo:: DO THIS
