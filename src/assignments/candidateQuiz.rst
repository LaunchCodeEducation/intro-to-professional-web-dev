.. _candidateQuiz:

Assignment #1: Candidate Testing
================================

OK, staff, we received many applications for our astronaut training program,
and we need to do an initial evaluation of the candidates.  Management needs
you to create a quick quiz to help select the best candidates.

Requirements
------------

#. Ask the candidate to enter their name
#. Use a loop to ask five questions, one at a time, to the candidate
#. Collect the candidate's answers
#. Check those answers for accuracy (case insensitive equality check)
#. Calculate the candidate's overall percentage
#. Determine if the candidate did well enough to enter our program (need >= 80%
   to pass)
#. Display the results. Example output is listed below.

Results Output
^^^^^^^^^^^^^^

The results output should include the candidate's name, the candidate's
responses, the correct answers, the final percentage, and if the candidate
passed the quiz.

You are expected to match this format.
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

.. note:: The output will vary slightly based on the candidate's answers to each question.

Take It Step by Step
--------------------

When starting any project, it's best to approach it as a series of smaller,
testable parts. The goal is to get simple parts working first and then expand
the code in a systematic way. The following is NOT the only way to complete
this assignment, but it provides a framework for thinking through the project.

Part 1: Minimum Viable Quiz
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Define variables for:

   a. candidate's name
   b. a quiz question (pick any question from the table in step 2)
   c. the correct answer
   d. the candidate's response

#. Ask for the candidate's name. Before moving to the next step, use
   ``console.log`` to verify that your code correctly stores the information.
#. Display the question and prompt the candidate for an answer. As before, use
   ``console.log`` to verify that your program correctly stored the answer.
#. Check the candidate's answer to see if it is correct.
#. Provide basic feedback to the student. This should include their name and
   whether their answer was correct.

.. note:: If not already done, remove the extra ``console.log`` statements from steps 2 & 3. Make sure your small app works properly before moving on to part 2.

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

.. note:: Checking for the correct answer should be case insensitive (e.g. "Orbit" is the same as "orbit").

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

a. Does not consider case when checking answers.
b. Includes at least one loop and one conditional.
c. Uses at least one template literal.
d. Correctly accepts or rejects a candidate based on their percentage.

Submitting Your Work
---------------------

Lorem ipsum...
