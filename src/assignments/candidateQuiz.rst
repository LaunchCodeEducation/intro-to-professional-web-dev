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
#. Check those answers for accuracy

   a. Case insensitive equality check

#. Calculate the candidate's overall percentage
#. Determine if the candidate did well enough to enter our program (need >= 80% to pass)
#. Display the results

   a. Example output is listed below

Results Output
^^^^^^^^^^^^^^

The results output should include the candidate's name, the candidate's responses, and
whether each answer was correct or incorrect.  If incorrect, provide the right answer in the
feedback.

You are expected to match this output format.
::

   Candidate Name: Can Twin
   1) True or false: 5000 meters = 5 kilometers.
      Your Answer: false (incorrect)
      Correct Answer: True

   2) (5 + 3)/2 * 10 = ?
      Your Answer: 45 (incorrect)
      Correct Answer: 40

   3) Given the array [8, "Orbit", "Trajectory", 45], what entry is at index 2?
      Your Answer: trajectory (correct)

   4) Who was the first American woman in space?
      Your Answer: Sally ride (correct)

   5) What is the minimum crew size for the International Space Station (ISS)?
      Your Answer: 10 (incorrect)
      Correct Answer: 3

   >>> Overall Grade: 40% <<<
   >>> Status: FAILED <<<

.. note:: The output will vary slightly based on the user's answers to each question.

Take It Step by Step
--------------------

When starting any project, it's best to approach it as a series of smaller,
testable parts. The goal is to get smaller, simpler parts working and then expand the code in a systematic way.
The following is NOT the only way to complete this assignment, but it provides a framework for thinking through the project.

Step 1: Minimum Viable Quiz
^^^^^^^^^^^^^^^^^^^^^^^^^^^

a. Define variables for:

   1. candidate's name
   2. a quiz question (pick any question from the table in step 2)
   3. the correct answer
   4. the candidate's response

b. Ask for the candidate's name
c. Display the question and prompt the candidate for an answer
d. Check the candidate's answer to see if it is correct
e. Provide basic feedback to the student

   1. This should include their name and whether their answer was correct

.. note:: Make sure your small app works properly before moving on to step 2.

Step 2: Use Arrays
^^^^^^^^^^^^^^^^^^

Now that your small app is working, expand it to deal with multiple questions.

a. Fill two arrays with the questions and answers listed in the table below.
b. You still need to ask for the candidate's name.
c. Using bracket notation, select one question and use that to prompt the
   candidate.
d. Compare the candidate's response to the proper entry in the answers array.
e. Replace the basic feedback with a template literal.

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

Step 3: Use Iteration to Ask All Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add one or more loops to your code to ask all the questions in the quiz.
Collect and check all the candidate's answers, then calculate the final
percentage.


Submitting Your Work
--------------------

Lorem ipsum...
