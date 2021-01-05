Assignment #2: Scrabble Scorer
==============================

For your second assignment, we'll ask you to modify and improve our Scrabble Scorer program. 
Did you think you were going to work on Mars Rover code already? That will come next!

We want you to update our program that asks a user for a word 
and outputs a score. Your final version will have three scoring algorithms and 
allow a user to interactively choose which algorithm to use. We've provided some starter code that
includes the official Scrabble scoring point system and we'd like you to make 
some modifications to improve it.

Let's roll.

.. TODO: mod this replit instruction. 3 types of students. independent learning track, instructor led track, and independent readers

If you are NOT enrolled in a repl.it classroom for this course, fork the
starter code at this `repl.it <https://repl.it/@launchcode/scrabble-scorer>`__.

Requirements
------------

.. admonition:: Note

   The requirements below are what your assignment should look like when it's 
   time to submit. Rome wasn't built in a day and neither was Scrabble.

   This assignment is broken down so you can complete small pieces as you go.
   You need to move sequentially starting with Part A below. You'll have a much more 
   enjoyable time writing this program if you read this entire page before even opening repl.it.

#. Write an ``initialPrompt()`` function that asks a user to input a word.
#. Have the program return a score for the word using ``oldScrabbleScorer()``.
#. Add additional scoring algorithms and store them in the ``scoringAlgorithms`` array.
#. Create a ``transform()`` function that takes in the ``oldPointStructure``
   object and returns a ``newPointStructure`` object.
#. Use the ``runProgram()`` function to serve as the starting point for your
   program.

Starter Code
------------

You only need to pay attention to one file here, ``scrabble-scorer.js``. Within this JavaScript
file is still some more starter code that you don't need to touch. We'll point out what you 
should be modifying here to write your Scrabble Scorer program.

Hit the repl.it run button initially and you'll see a message printed to the console:

:: 

   > node program
   Let's play some Scrabble! Enter a word:
   >

.. admonition:: Tip

   If you don't see this message printed and have exhausted your troubleshooting skills, 
   reach out to your classmates or course staff ASAP so you can get started with the real coding.

Instructions
------------

A) Initial Prompt
^^^^^^^^^^^^^^^^^

#. Modify the provided ``initialPrompt()`` function to prompt the user to enter a word to score. 
#. Use the ``oldScrabbleScorer()`` function provided to score the word provided by the user. Print the result to the console.


Before you move on, be sure you're on the right track. At this point, your program should have an output like this:

:: 

   > node program
   Let's play some Scrabble!

   Enter a word to score: pineapple
   Points for 'P': 3
   Points for 'I': 1
   Points for 'N': 1
   Points for 'E': 1
   Points for 'A': 1
   Points for 'P': 3
   Points for 'P': 3
   Points for 'L': 1
   Points for 'E': 1

   >


B) Add and Organize Scoring Algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your job here is to write two other scoring algorithms for the Scrabble player.

#. ``simpleScorer``: Define a function that takes a word as a parameter and
   returns a numerical score. Each letter within the word is worth 1 point.
#. ``vowelBonusScorer``: Define a function that takes a word as a parameter and
   returns a score. Each vowel within the word is worth 3 points, and each
   consonant is worth 1 point.

.. admonition:: Note

   Make each scoring algorithm case *insensitive*, meaning that they
   should all ignore case when assigning points.


Once you've written these scoring functions, organize all three of the scoring options into an array.
Your program will use the ``scoringAlgorithms`` array to retrieve information about the 
three scoring algorithms and convey that information to the user. 

#. Finish writing the ``scoringAlgorithms`` array. It should be populated with three objects, one for each of the three scoring options. 
   Each object should contain three keys: ``name``, ``description``, and ``scorerFunction``.
#. Examine the table for the information to store in ``name`` and
   ``description``. The ``scorerFunction`` for each object should be the name of
   one of the three scoring algorithms already defined.

   .. list-table::
      :header-rows: 1

      * - Name
        - Description
        - Score Function
      * - Simple Score
        - Each letter is worth 1 point.
        - A function with a parameter for user input that returns a score.
      * - Bonus Vowels
        - Vowels are 3 pts, consonants are 1 pt.
        - A function that returns a score based on the
          number of vowels and consonants.
      * - Scrabble
        - The traditional scoring algorithm.
        - Uses the ``oldScrabbleScorer()`` function to determine the score for a given
          word.


#. Finish writing ``scorerPrompt()`` so that the user can select which scoring algorithm to use when the program scores their word. 
   Use the selected algorithm to determine the score for the word:

   a. If the user enters ``0``, have the program output a score using the simple scorer.
   b. If the user enters ``1``, use the vowel bonus scoring function.
   c. If the user enters ``2``, use the Scrabble scoring option.

   ``scorerPrompt()`` should return the object the user has selected.

   .. admonition :: Tips

      Your ``scoringAlgorithms`` structure now holds all of the scoring information required for the program.

      To access a scoring object and its properties, use a combination of bracket notation and dot notation.

      .. admonition:: Examples

         .. sourcecode:: js

            // Simple scoring
            console.log("algorithm name: ", scoringAlgorithms[0].name);
            console.log("scorerFunction result: ", scoringAlgorithms[0].scorerFunction("JavaScript"));

         Console Output

         ::

            algorithm name:  Simple Score
            scorerFunction result:  10

#. Call ``scorerPrompt()`` inside of ``runProgram()`` so that the program asks the user for a scoring algorithm after prompting for a word.
   Use the scoring object returned from ``scorerPrompt()`` to score the user's word and let the user know what score their word receives.

Before moving forward, your running program should behave roughly like this:

:: 

   > node program
   Let's play some Scrabble!

   Enter a word to score: coconut
   Which scoring algorithm would you like to use?

   0 - Simple: One point per character
   1 - Vowel Bonus: Vowels are worth 3 points
   2 - Scrabble: Uses scrabble point system
   Enter 0, 1, or 2: 0
   Score for 'coconut': 7

   > 

C) Transform Scrabble Scoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the software contains the data structure below for the traditional
Scrabble scoring algorithm. Take a few moments to review how the
``oldPointStructure`` object relates a point value to a letter.

.. sourcecode:: js
   :linenos:

   const oldPointStructure = {
      1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
      2: ['D', 'G'],
      3: ['B', 'C', 'M', 'P'],
      4: ['F', 'H', 'V', 'W', 'Y'],
      5: ['K'],
      8: ['J', 'X'],
      10: ['Q', 'Z']
   };

The *keys* of ``oldPointStructure`` are the Scrabble points, and the
*values* are arrays of letters. All letters in the array have the Scrabble
point value equal to the key. For example, ``'A'`` and ``'R'`` are worth 1,
``'K'`` is worth 5, and ``'J'`` is worth 8.

To find the point value for a letter with the old format, the program must
iterate over each key in ``oldPointStructure`` and then check if the letter is
inside the array paired with that key. *This search within a search is
inefficient*.

.. admonition:: Tip

   Think about this for a second. The scoring action takes in letters in a word as input
   and outputs numerical point values. 

   We can improve our program by rewriting the data structure to better fit the action
   we want to take. Keep this idea in mind as you go on to code your own
   applications.

It would improve the performance of the program to create a ``newPointStructure`` object that has 26 keys,
one for each letter. The value of each key will be the Scrabble point value.

Examples of the new key storage:

* ``a`` is worth ``1``
* ``b`` is worth ``3``
* ``c`` is worth ``3``
* ``j`` is worth ``8``

In ``newPointStructure``, the letters themselves are keys, so a *single* search
will identify a point value. 

.. admonition:: Example

   Example of ``newPointStructure`` object usage.

   .. sourcecode:: js

      console.log("Scrabble scoring values for");
      console.log("letter a: ", newPointStructure.a);
      console.log("letter j: ", newPointStructure.j);
      console.log("letter z: ", newPointStructure["z"]);

   **Console Output**

   ::

      Scrabble scoring values for
      letter a:  1
      letter j:  8
      letter z:  10

Transform the Object
~~~~~~~~~~~~~~~~~~~~

#. Write the rest of the ``transform()`` function. It will need to take an object 
   as a parameter - specifically the ``oldPointStructure`` object. Calling
   ``transform(oldPointStructure)`` will return an object with *lowercase*
   letters as keys. The value for each key will be the points assigned to that
   letter.

   .. admonition:: Tips

      a. Recall that ``for...in`` loops iterate over the keys within an object.
      b. If you need a reminder of how to assign new key/value pairs, review the
         :ref:`relevant section <add-new-object-properties>` in the
         ``Objects and Math`` chapter.
      c. To access the letter arrays within ``oldPointStructure``, use bracket
         notation (``oldPointStructure['key']``).
      d. To access a particular element within a letter array, add a second set of
         brackets (``oldPointStructure['key'][index]``), or assign the array to a
         variable and use ``variableName[index]``.

         .. admonition:: Examples

            .. sourcecode:: JavaScript
               :linenos:

               console.log("Letters with score '4':", oldPointStructure['4']);
               console.log("3rd letter within the key '4' array:", oldPointStructure['4'][2]);

               let letters = oldPointStructure['8'];
               console.log("Letters with score '8':", letters);
               console.log("2nd letter within the key '8' array:", letters[1]);

            **Console Output**

            ::

               Letters with score '4': [ 'F', 'H', 'V', 'W', 'Y' ]
               3rd letter within the key '4' array: V

               Letters with score '8': [ 'J', 'X' ]
               2nd letter within the key '8' array: X


#. Locate the ``newPointStructure`` object in the starter code and set it equal to
   ``transform(oldPointStructure)``.


.. admonition:: Warning 

   Hardcoding the ``newPointStructure`` object literal like this:

   .. sourcecode:: js

      let newPointStructure = 
      {
         a:1,
         b: 1,
         c: 1,
         etc ...
      }

   won't pass. And you'll lose an opportunity to practice this skill.

4. Once you've defined ``newPointStructure``, use it to finish writing the ``scrabbleScorer()`` function and then replace 
   the ``oldScrabbleScorer()`` function in ``scoringAlgorithms`` with this new function.

   .. admonition:: Tip

      ``oldScrabbleScorer()`` uses ``oldPointStructure`` and returns a score for each letter in a word. You'll want to write
      ``scrabbleScorer()`` to use ``newPointStructure`` and return a cumulative score for the whole word entered.

Test Words
----------

Here are some words you can use to test your code:

#. ``JavaScript`` = 24 points using Scrabble, 10 using Simple Score, and 16
   using Bonus Vowels.
#. ``Scrabble`` = 14 points using Scrabble, 8 using Simple Score, and 12 using
   Bonus Vowels.
#. ``Zox`` = 19 points using Scrabble, 3 using Simple Score, and 5 using Bonus
   Vowels.

.. _example-output:

Example Output
^^^^^^^^^^^^^^

::

   > node program
   Let's play some Scrabble!

   Enter a word to score: rum
   Which scoring algorithm would you like to use?

   0 - Simple: One point per character
   1 - Vowel Bonus: Vowels are worth 3 points
   2 - Scrabble: Uses scrabble point system
   Enter 0, 1, or 2: 2
   Score for 'rum': 5

   > 

Bonus Missions
--------------

#. Currently, the prompts accept ANY input values. The user could enter
   something *other* than 0, 1, or 2 when selecting the scoring algorithm, and
   they could enter numbers or symbols when asked for a word. Modify your code
   to reject invalid inputs and then re-prompt the user for the correct
   information.
#. Score words spelled with blank tiles by adding ``' '`` to the
   ``newPointStructure`` object. The point value for a blank tile is ``0``.

.. TODO: what does submission look like now?

.. Submitting Your Work
.. --------------------

.. #. From the address bar at the top of the browser window, copy the URL of the
..    repl.it that contains your solution.
.. #. Go to the Graded Assignment #2 page in Canvas and click *Submit Assignment*.
.. #. Paste the URL into the Website URL input.
.. #. Click *Submit Assignment* again.
.. #. Notify your TA that your assignment is ready to be graded.
