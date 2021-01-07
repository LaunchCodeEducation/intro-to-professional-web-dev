.. _candidateQuiz:

Assignment #1: Candidate Testing
================================

OK, staff, we received many applications for our astronaut training program,
and we need to do an initial evaluation of the candidates.  Management needs
you to create a quick quiz to help select the best candidates.

.. note::

   The requirements below are what your END assignment will look like.
   This assignment is broken down so you can complete small pieces as you go. You need to move sequentially starting at Part 1.
   Please read the WHOLE assignment page before starting.

Requirements
------------

#. Ask the candidate (user) to enter their name
#. Use a loop to ask five questions, one at a time, to the candidate
#. Collect the candidate's answers
#. Check those answers for accuracy (case insensitive equality check)
#. Calculate the candidate's overall percentage
#. Determine if the candidate did well enough to enter our program (need >= 80%
   to pass)
#. Display the results.

Take It Step by Step
--------------------

When starting any project, it's best to approach it as a series of smaller,
testable parts. The goal is to get simple parts working first and then expand
the code in a systematic way. The following is NOT the only way to complete
this assignment, but it provides a framework for thinking through the project.

Login to repl.it
^^^^^^^^^^^^^^^^^

If you are enrolled in a repl.it classroom for this course, login to that
classroom and open the starter code for the *Candidate Testing* assignment. If
you are NOT enrolled in a repl.it classroom, fork this
`starter repl.it <https://repl.it/@launchcode/candidate-tester>`__.

Part 1: Minimum Viable Quiz
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. #. Define variables for:

..    a. candidate's name
..    b. a quiz question (pick any question from the table in Part 2 below)
..    c. the correct answer
..    d. the candidate's response

1.1 candidateName
~~~~~~~~~~~~~~~~~

a. Ask for the candidate's name. Look for ``TODO 1.1a`` in the starter code. 
   On the line below this TODO comment, define a variable called ``candidateName``
   with an initial value of the empty string.

#. Look for ``TODO 1.1b``. Inside of the function ``askForName()``, write code
   asking the user to enter their name into the program and store the value as
   ``candidateName``.

#. Look for ``TODO 1.1c``. Underneath it, write a message to the console greeting 
   the user using the name they just provided.


1.2 question, correctAnswer, and candidateAnswer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a. Ask the user to answer a single quiz question. Look for ``TODO 1.2a``.
   Below the TODO comment, define variables called ``question``, ``correctAnswer``,
   and ``candidateAnswer``.

   - ``question`` should be initialized to the following string: ``"Who was the first American woman in space? "``.

   .. admonition:: Tip

      Note the trailing space at the end of this string is required. 

   - ``correctAnswer`` should be initialized to ``"Sally Ride"``.

   - ``candidateAnswer`` will initially be set to the empty string.

#. Find ``TODO 1.2b``. Using your question variable, display the question and prompt the candidate for 
   their answer. Store their response in one of the variables you defined just above.

#. Under ``TODO 1.2c``, check the candidate's answer to see if it is correct. 
   Provide basic feedback to the candidate, letting them know if their answer is correct
   or not.

.. admonition:: Note

   Make sure your small app works properly before moving on to part 2.

Part 2: Use Arrays
^^^^^^^^^^^^^^^^^^

Now that your small app is working, expand it to deal with multiple questions.

#. Redefine your question and correct answer variables to be arrays.
#. Fill these arrays with the questions and answers listed in the table below.
#. You still need to ask for the candidate's name.
#. Using bracket notation, select one question and use that to prompt the
   candidate.
#. Compare the candidate's response to the proper entry in the answers array.
#. Replace the basic feedback with a template literal.

.. admonition:: Note

   Checking for the correct answer should be case insensitive (e.g. "Orbit" is the same as "orbit").

.. list-table::
   :header-rows: 1

   * - Question
     - Answer

   * - True or false: 5000 meters = 5 kilometers.
     - "True"

   * - (5 + 3)/2 * 10 = ?
     - "40"

   * - Given the array ``[8, "Orbit", "Trajectory", 45]``, what entry is at index 2?
     - "Trajectory"

   * - Who was the first American woman in space?
     - "Sally Ride"

   * - What is the minimum crew size for the International Space Station (ISS)?
     - "3"

Part 3: Use Iteration to Ask All Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add one or more loops to your code to ask all the questions in the quiz.
Use arrays to collect and check all the candidate's answers.  Finally,
calculate the candidate's score and print the results.

Helpful hint - To calculate the candidate's percentage, use the equation:

   (Number of Correct Answers) / (Number of Questions) * 100

Note that the final report MUST have the format shown in the "Results Output"
section.

Sanity Checks
--------------

Before submitting your solution, make sure your program:

#. Does NOT consider case when checking answers.
#. Includes at least one loop and one conditional.
#. Uses at least one template literal.
#. Correctly accepts or rejects a candidate based on their percentage.

Example Output
^^^^^^^^^^^^^^

The results output should include the candidate's name, the candidate's
responses, the correct answers, the final percentage, and if the candidate
passed the quiz.

::

   Candidate Name: Can Twin
   1) True or false: 5000 meters = 5 kilometers.
   Your Answer: false
   Correct Answer: true

   2) (5 + 3)/2 * 10 = ?
   Your Answer: 45
   Correct Answer: 40

   3) Given the array [8, "Orbit", "Trajectory", 45], what entry is at index 2?
   Your Answer: trajectory
   Correct Answer: trajectory

   4) Who was the first American woman in space?
   Your Answer: sally ride
   Correct Answer: sally ride

   5) What is the minimum crew size for the International Space Station (ISS)?
   Your Answer: 10
   Correct Answer: 3

   >>> Overall Grade: 40% (2 of 5 responses correct) <<<
   >>> Status: FAILED <<<

.. admonition:: Note

   The output will vary slightly based on the candidate's answers to each question.

Submitting Your Work
---------------------

#. From the address bar at the top of the browser window, copy the URL of the
   repl.it that contains your solution.

   .. admonition:: Example

      repl.it project URL: ``https://repl.it/@username/candidate-tester#index.js``

#. Go to the Canvas assignment page and click *Submit Assignment*.
#. Paste the URL into the *Website URL* input.
#. Click *Submit Assignment* again.
#. Notify your TA that your assignment is ready to be graded.
