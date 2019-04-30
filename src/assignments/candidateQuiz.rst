.. _candidateQuiz:

Assignment #1: Candidate Testing
=================================

OK, staff, we received many applications for our astronaut training program,
and we need to do an initial evaluation of the candidates.  Management needs
you to create a quick quiz to help select the best people.

The quiz will consist of 5 questions, and the minimum passing score is 80%.
You must design your code to do the following:

#. Use a loop to present one question at a time to the candidate,
#. Collect the candidate's answers,
#. Check those answers for accuracy,
#. Calculate the candidate's overall percentage,
#. Determine if the candidate did well enough to enter our program,
#. Display the results.

Since this your first big task, you should approach it as a series of smaller,
testable parts.  The following is NOT the only way to complete this assignment,
but it provides a nice framework for thinking through the project. Start small
with a working piece of code, and then expand the code in a systematic way.

Step 1: Code a minimum viable quiz app
--------------------------------------

a. Define variables to hold the candidate's name, a quiz question chosen from
   the table below, the correct answer and the candidate's response.
b. Ask for the candidate's name.
c. Display the selected question and prompt the candidate for an answer.
d. Check the candidate's answer to see if it is correct.
e. Provide basic feedback to the student. This should include their name and
   whether their answer was correct.

Make sure your small app works properly before moving on to step 2.

.. list-table::
   :header-rows: 1

   * - Question
     - Answer
   * - What is your name?
     - This answer will NOT be scored, but it must be part of the final report.

   * - True or false: 5000 meters = 5 kilometers.
     - "True"

   * - (5 + 3)/2 * 10 = ?
     - "40"

   * - Given the array ``[8, "Zebra", "apple", 45]``, what entry is at index 2?
     - "apple"

   * - Who was the first American woman in space?
     - "Sally Ride"

   * - What is the minimum crew size for the International Space Station (ISS)?
     - "3"

Step 2: Update the quiz app to use arrays
------------------------------------------

Now that your small app is working, expand it to deal with multiple questions.

a. Fill two arrays with the required questions and answers.
b. You still need to ask for the candidate's name.
c. Using bracket notation, select one question and use that to prompt the
   candidate.
d. Compare the candidate's response to the proper entry in the answers array.
e. Replace the basic feedback with a template literal.

Note that checking for the correct answer should be case insensitive (e.g.
"Orbit" is the same as "orbit").

The output should include the candidate's name, the candidate's response, and
whether that answer was correct.  If incorrect, provide the right answer in the
feedback.

Step 3: Use iteration to make the app better
-----------------------------------------------

Add one or more loops to your code to ask all the questions in the quiz.
Collect and check all the candidate's answers, then calculate the final
percentage.

The format for the score report is shown below. (Note that the answers and
percentage will vary for different candidates).

::

   Candidate Name: Can Twin
   1) True or false: 5000 meters = 5 kilometers.
      Your Answer: false (incorrect)
      Correct Answer: True

   2) (5 + 3)/2 * 10 = ?
      Your Answer: 45 (incorrect)
      Correct Answer: 40

   3) Given the array [8, "Zebra", "apple", 45], what entry is at index 2?
      Your Answer: Apple (correct)

   4) Who was the first American woman in space?
      Your Answer: Sally ride (correct)

   5) What is the minimum crew size for the International Space Station (ISS)?
      Your Answer: 10 (incorrect)
      Correct Answer: 3

   >>> Overall Grade: 40% <<<
   >>> Status: FAILED <<<

Step 4: Submitting your work
-----------------------------

Lorem ipsum...
