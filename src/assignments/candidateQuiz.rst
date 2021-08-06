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

Get the Starter Code
^^^^^^^^^^^^^^^^^^^^

Fork `this replit <https://replit.com/@launchcode/Candidate-Testing-Autograded#candidate-testing.js>`__.


Part 1: Minimum Viable Quiz
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1 ``candidateName``
~~~~~~~~~~~~~~~~~~~~~

a. Ask for the candidate's name. Look for ``TODO 1.1a`` in the starter code. 
   On the line below this TODO comment, define a variable called ``candidateName``
   with an initial value of the empty string.

#. Look for ``TODO 1.1b``. Inside of the function ``askForName()``, write code
   asking the user to enter their name into the program and store the value as
   ``candidateName``.

#. Look for ``TODO 1.1c``. Underneath it, write a message to the console greeting 
   the user using the name they just provided.


1.2 Single Question Quiz
~~~~~~~~~~~~~~~~~~~~~~~~

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

Part 2: Multiple Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that your small app is working, expand it to deal with multiple questions.
This time, you only have one ``TODO`` item in the starter code. You will need
to determine which lines need to be modified.

#. Define ``questions`` and ``correctAnswers`` variables as arrays. Use the table below to fill these arrays.
#. Replace your code from ``TODO 1.2b`` with a loop that programmatically asks each question in the array and stores 
   the user's responses.
#. Replace the basic feedback from ``TODO 1.2c`` with a template literal that displays each of the candidate's responses in 
   addition to the corresponding correct answers.

.. list-table::
   :header-rows: 1

   * - Question
     - Answer

   * - Who was the first American woman in space?
     - "Sally Ride"

   * - True or false: 5 kilometer == 5000 meters?
     - "true"

   * - (5 + 3)/2 * 10 = ?
     - "40"

   * - Given the array ``[8, 'Orbit', 'Trajectory', 45]``, what entry is at index 2?
     - "Trajectory"

   * - What is the minimum crew size for the ISS?
     - "3"

.. admonition:: Warning

   Keep the questions and correct answers stored in this exact order.

Part 3: Grade the Quiz
^^^^^^^^^^^^^^^^^^^^^^

Finally, calculate the candidate's score and print the results. There are no ``TODOs`` in this section, 
just be sure to only modify code that you have written, or add code. Don't remove anything in the file 
that you haven't written. Doing so may cause your program to behave unexpectedly - and we might not be able to grade it!

Your task here is to:

#. Compare the candidate answers with the correct answers,
#. Calculate the candidate's score as a percentage,
#. Convey to the candidate if they have passed the quiz with an 80% or if they have failed.

Some tips:

#. Checking for the correct answer should be case insensitive (e.g. "Orbit" is the same as "orbit").
#. Somewhere below ``TODO 1.2c`` you should see a variable declaration for ``grade``. Use this to calculate the candidate's
   score.
#. To calculate the candidate's percentage, use the equation:

   **(Number of Correct Answers) / (Number of Quiz Questions) * 100**


Example Output
^^^^^^^^^^^^^^

The results output should include the candidate's name, the candidate's
responses, the correct answers, the final percentage, and if the candidate
passed the quiz.

::

   Candidate Name: Can Twin
   1) Who was the first American woman in space?
   Your Answer: sally ride
   Correct Answer: Sally Ride

   2) True or false: 5000 meters = 5 kilometers.
   Your Answer: false
   Correct Answer: true

   3) (5 + 3)/2 * 10 = ?
   Your Answer: 45
   Correct Answer: 40

   4) Given the array [8, "Orbit", "Trajectory", 45], what entry is at index 2?
   Your Answer: trajectory
   Correct Answer: Trajectory

   5) What is the minimum crew size for the ISS?
   Your Answer: 10
   Correct Answer: 3

   >>> Overall Grade: 40% (2 of 5 responses correct) <<<
   >>> Status: FAILED <<<

.. admonition:: Note

   The output will vary slightly based on the candidate's answers to each question.

