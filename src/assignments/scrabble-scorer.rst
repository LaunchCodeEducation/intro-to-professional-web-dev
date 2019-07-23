Assignment #2: Scrabble Scorer
==============================

To see how far your skills have come, we are going to give you a mission to
update our *super* important Scrabble Scorer program. Did you think you were
going to work on Mars rover code already?

The current Scrabble Scorer, is a program that will take in a word and return
the point value. The program needs to be rewritten for two reasons. First the
data structure used to store the letter point values is inefficient. Second the
program should have three scoring algorithms and allow the user to pick which
algorithm to use. These new features will make the program more efficient and
user friendly.

Fork the starter code at this
`repl.it <https://repl.it/@launchcode/scrabble-scorer>`__.

Requirements
------------

#. Create an ``oldScoreKey`` object that contains the previous scoring system.
#. Create a ``transform`` function which will return a ``newScoreKey`` object.
#. Create ``scoringAlgorithms`` array to hold three scoring objects, which
   include the scoring functions.
#. Create an ``initialPrompt`` function that asks the user which scoring
   algorithm to use.
#. Create a ``runProgram`` function to contain the starting point for your
   running program.

Example Output
^^^^^^^^^^^^^^
::

   Welcome to the Scrabble score calculator. Click 'Stop' to quit.

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
Currently the Scrabble Grader software uses the data structure below for the
traditional Scrabble scoring algorithm. Take a few moments to review how
``oldScoreKey`` relates a letter to a point value.

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

The object keys of ``oldScoreKey`` are the Scrabble points, and the values
are arrays of letters. All letters in the array have the Scrabble
point value equal to the key. For example, ``'A'`` is worth 1, and ``'J'`` is
worth 8.

With the old format, to find the point value for a letter, the program must
iterate over each key in ``oldScoreKey`` and then check if the letter is inside
the array paired with that key. This search within a search is inefficient.

It would be better to create a ``newScoreKey`` object that has 26 keys, one for
each letter. The value of each key will be the Scrabble point value.

Example of new key storage

* ``a`` is worth ``1``
* ``j`` is worth ``8``
* ``k`` is worth ``10``

In ``newScoreKey``, the letters themselves are keys, so a single search will
identify a point value.

.. admonition:: Example

   Example of ``newScoreKey`` object usage.

   .. sourcecode:: js

      console.log("Scrabble scoring values for");
      console.log("letter a: ", newScoreKey.a);
      console.log("letter j: ", newScoreKey.j);
      console.log("letter z: ", newScoreKey["z"]);

   **Console Output**

   ::

      Scrabble scoring values for
      letter a:  1
      letter j:  8
      letter z:  10

Write a ``transform`` function that takes the ``oldScoreKey`` object as a
parameter. ``transform(oldScoreKey)`` will return an object with the letters as
keys. The keys in the ``newScoreKey`` object should be *lowercase* letters.

Hints
~~~~~~

#. Recall that ``for...in`` loops iterate over the keys within an object.
#. To access the letter arrays within ``oldScoreKey``, use bracket notation
   (e.g. ``oldScoreKey['key']``).
#. To access a particular element within a letter array, add a second set of
   brackets (e.g. ``oldScoreKey['key'][index]``), or assign the array to a
   variable.

.. admonition:: Example

   .. sourcecode:: JavaScript
      :linenos:

      console.log("Letters with score '4':", oldScoreKey['4']);
      console.log("3rd letter within the key '4' array:", oldScoreKey['4'][2]);

      let letters = oldScoreKey['8'];
      console.log("Letters with score '8':", letters);
      console.log("2nd letter within the key '8' array:", letters[1]);

   **Console Output**

   ::

      Letters with score '4': [ 'F', 'H', 'V', 'W', 'Y' ]
      3rd letter within the key '4' array: V

      Letters with score '8': [ 'J', 'X' ]
      2nd letter within the key '8' array: X

Pick Scoring Algorithm
^^^^^^^^^^^^^^^^^^^^^^
The current Scrabble Scorer only uses one scoring algorithm. For the new
version we want to let the user pick between three algorithms. Define an
``initialPrompt`` function that will introduce the program and then ask the
user which scoring algorithm they want to use. See Example Output above and the
next section for details on available options.

Scoring Algorithms
^^^^^^^^^^^^^^^^^^
Create a ``scoringAlgorithms`` array that contains three scorer objects. Each
scorer object should have these three keys: ``name``, ``description``, and
``scoreFunction``.

The ``scoreFunction`` for each object should be a function that takes in one
parameter named ``word`` and returns a point value based on the logic listed
below. The ``scoreFunction`` functions can named or anonymous.

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Score Function
   * - Scrabble
     - The traditional scoring algorithm.
     - A function with a ``word`` parameter that returns a score.
       Uses the ``newScoreKey`` object to determine that score.
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

#. Take ``scoringAlgorithms`` as a parameter.
#. Use ``initialPrompt`` to pick the algorithm.
#. Prompt the user for a word to score.
#. Use the picked algorithm to determine a word score.

   a. If the user enters ``0`` or an invalid option, then use the Scrabble
      ``scoreFunction``
   b. If the user enters ``1`` then use the Simple Score ``scoreFunction``
   c. If the user enters ``2`` then use the Bonus Vowels ``scoreFunction``

#. Display the score for the word.
#. Repeat steps 3 to 5 until program is stopped.

Test Words
-----------

Here are some words you can use to test your code:

#. ``JavaScript`` = 24 points using Scrabble, 10 using Simple, and 16 using
   Bonus Vowels.
#. ``Scrabble`` = 14 points using Scrabble, 8 using Simple, and 12 using
   Bonus Vowels.
#. ``Zox`` = 19 points using Scrabble, 3 using Simple, and 5 using Bonus
   Vowels.

Bonus Mission
-------------
Handle scoring words that were spelled with blank tiles by adding ``' '`` to
the ``newScoreKey`` object. The point value for a blank tile is ``0`` points.

Submitting Your Work
--------------------

#. From the address bar at the top of the browser window, copy the URL of the
   repl.it that contains your solution.

   .. admonition:: Examples

      repl.it account URL: ``https://repl.it/@your-username/candidate-tester``

      repl.it classroom URL: ``https://repl.it/student/submissions/9999999``

#. Go to the Canvas assignment page and click Submit Assignment.
#. Paste the URL into the Website URL input.
#. Click Submit Assignment again.
#. Notify your TA that your assignment is ready to be graded.
