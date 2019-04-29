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
testable parts.  The following is not the ONLY way to complete this assignment,
but it provides a nice framework for thinking through the project. Start small
with a working piece of code, and then expand the code in a systematic way.

Step 1: Code a minimum viable quiz app
--------------------------------------

a. Define variables to hold the candidate's name, a question, the correct
   answer and the candidate's response.
b. Ask for the candidate's name.
c. Print the question on the screen and prompt the candidate for an answer.
d. Check the candidate's answer to see if it is correct.
e. Print basic feedback to the student including their name and whether their
   answer was correct.

Make sure your small app works properly before moving on to step 2.

Quiz Questions
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Question
     - Answer
   * - ``What is your name?``
     - This answer will be part of the candidate's score, but it must be part of the final report.

Step 2: Update the quiz app to use arrays
------------------------------------------

a. Fill two arrays with the required questions and answers.
b. You still need to ask for the candidate's name.
c. Using bracket notation, select one question and use that to query the
   candidate.
d. Compare the candidate's response to the proper entry in the answers array.
e. Replace the basic feedback with a template literal.

Note that checking for the correct answer should be case insensitive (e.g.
"Orbit" is the same as "orbit").

The output should include the candidate's name, the candidate's response, and
whether that answer was correct.  If incorrect, provide the right answer in the
feedback.
