Exercises
=========

Zero Division: Throw
--------------------

Write a function called divide that takes two parameters: a numerator and a denominator.

Your function should return the result of numerator / denominator.

However, if the denominator is zero you should throw an error informing the user they attempted to divide by zero.

.. hint::

   You should use an if and throw statement to complete this exercise.

Catch Undefined Grades
----------------------

A teacher is compiling their end of semester grades and wants to use JavaScript to help automate the process. The teacher has created the following function to convert an assignment grade to a percentage:

.. sourcecode:: js

   function convertGrade(assignmentScore, assignmentTotal) {
       return ((assignmentScore) / assignmentTotal);
   }

   let score = 22;
   let total = 25;

   convertGrade(score, total);

This code works for the majority of the grades the teacher needs to convert. However, in some cases the student didn't turn in the assignment and the teacher attempts this code:

.. sourcecode:: js

   function convertGrade(assignmentScore, assignmentTotal) {
       return ((assignmentScore) / assignmentTotal);
   }

   let total = 25;

   convertGrade(score, total);

Upon running this code the teacher gets a ReferenceError: score is not defined. The teacher has hundreds of students and changing all of the missing grades to zeroes would take a long time.

We can help by using a try...catch statement. Add a try...catch statement for the ReferenceError and substitue a zero for any missing grades.