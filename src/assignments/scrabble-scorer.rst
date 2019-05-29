Assignment #2: Scrabble Scorer
==============================

To see how far your skills have come, we are going to give you a mission to update
our *super* important Scrabble Scorer program. Did you think you were going
to work on Mars rover code already?

The current Scrabble Scorer, is a program that will take in a word and return the point value.
The program needs to be rewritten for two reasons. First the data structure used to store
the letter point values is inefficient. Second the program should have three scoring
algorithms and allow the user to pick which algorithm to use. These new features will make
the program more efficient and user friendly.


Requirements
------------

#. Create an ``oldScoreKey`` object that contains the previous scoring system.
#. Create a ``transform`` function which will return a ``newScoreKey`` object.
#. Create ``scoringAlgorithms`` array to hold three scoring objects, which include the scoring functions.
#. Create a ``initialPrompt`` function that asks the user which scoring algorithm to use.
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
Currently the Scrabble Grader software uses the below data structure for the traditional
Scrabble scoring algorithm. Take a few moments to review how ``oldScoreKey`` relates a
letter to a point value.

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

The object keys of ``oldScoreKey`` are the Scrabble points and the values
are arrays of letters. All letters in the array have the Scrabble
point value equal to the key. Example ``'A'`` is worth 1 and ``'J'`` is worth 8.

Write a ``transform`` function that takes in as a parameter the ``oldScoreKey``
object. ``transform(oldScoreKey)`` will return an object with the letters as keys. The keys
in the ``newScoreKey`` object should be *lowercase* letters.

The ``newScoreKey`` object will have 26 keys, one for each letter. The value associated to each key
will be the Scrabble point value.

Example of new key storage

* ``a`` is worth ``1``
* ``j`` is worth ``8``
* ``k`` is worth ``10``

The new data structure for storing point values is more efficient. Can you think of why?
With the old data structure, to find the point value for a letter you would need to iterate
over each point value and see if the letter is found in the array of letters that have
that value. In the new data structure has the letters themselves as keys which makes it
much faster to lookup the point value.

.. admonition:: Example

   Example of ``newScoreKey`` object usage.

   .. sourcecode:: js

      console.log("Scrabble scoring values for");
      console.log("letter a: ", newScoreKey.a);
      console.log("letter j: ", newScoreKey.j);
      console.log("letter z: ", newScoreKey["z"]);

   Console Output

   ::

      Scrabble scoring values for
      letter a:  1
      letter j:  8
      letter z:  10


Pick Scoring Algorithm
^^^^^^^^^^^^^^^^^^^^^^
The current Scrabble Scorer only uses one scoring algorithm. For the new version we
want to let the user pick between three algorithms. Define a ``initialPrompt`` function
that will introduce the program and then ask the user which scoring algorithm they want
to use. See Example Output above and the next section for details on available options.

Scoring Algorithms
^^^^^^^^^^^^^^^^^^
Create a ``scoringAlgorithms`` array that contains three scorer objects. Each scorer
object should have these three members ``name``, ``description``, and ``scoreFunction``.

The ``scoreFunction`` property for each scoring algorithm object should be a function.
Each ``scoreFunction`` function will take one parameter named ``word`` and return
the point value, using the logic listed below. The ``scoreFunction``
functions can named or anonymous functions.

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

   .. sourcecode:: js

      // Scrabble scoring
      console.log("algorithm name: ", scoringAlgorithms[0].name);
      console.log("scoreFunction result: ", scoringAlgorithms[0].scoreFunction("JavaScript"));
      // Simple scoring
      console.log("algorithm name: ", scoringAlgorithms[1].name);
      console.log("scoreFunction result: ", scoringAlgorithms[1].scoreFunction("JavaScript"));
      // Bonus Vowel scoring
      console.log("algorithm name: ", scoringAlgorithms[2].name);
      console.log("scoreFunction result: ", scoringAlgorithms[2].scoreFunction("JavaScript"));

   Console Output

   ::

      algorithm name:  Scrabble
      scoreFunction result:  24
      algorithm name:  Simple Score
      scoreFunction result:  10
      algorithm name:  Bonus Vowels
      scoreFunction result:  16

.. note:: All three scoring algorithms are case *insensitive*, meaning that they should ignore case.

Tie it All Together
^^^^^^^^^^^^^^^^^^^
Define a ``runProgram`` function that will:

1. Use ``initialPrompt`` to pick the algorithm.
2. Then prompt the user for a word to score.
3. Use the picked algorithm to determine a word score.

   * If you user entered ``0`` then use the Scrabble Scoring ``scoreFunction``

4. Display the score for the word.
5. Repeat steps 1 to 4 until program is stopped.


Bonus Mission
-------------
Handle scoring words that were spelled with blank tiles by adding ``' '`` to the ``newScoreKey`` object. The
point value for a blank tile is ``0`` points.


Submitting Your Work
--------------------

.. todo:: DO THIS
