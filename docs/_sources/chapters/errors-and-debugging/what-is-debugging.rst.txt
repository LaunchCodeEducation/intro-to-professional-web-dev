What is Debugging?
==================

.. index:: ! debugging, ! bug

Programming is a complex process. Since it is done by human beings, errors often occur. Programming errors are called **bugs** and the process of tracking them down and correcting them is called **debugging**.  

Some claim that in 1945, a dead moth caused a problem on relay number 70, panel F, of one of the first computers at Harvard, and the term bug has remained in use since. Wikipedia even has an image of the supposed `first bug <http://en.wikipedia.org/wiki/File:H96566k.jpg>`_.

.. index::
   single: error; syntax
   single: error; runtime
   single: error; logic

Three kinds of errors can occur in a program: syntax errors, runtime errors, and logic errors. We will learn about each kind of error before discussing strategies for debugging code and reducing errors.

Beginning Tips for Debugging
----------------------------

Debugging a program is a different way of thinking than writing a program. The process of debugging is much more like being a detective. Something has gone wrong and you must rely on clues, experience, intuition, and an inquisitive spirit to solve the problem.

Everyone is a suspect (except JavaScript)!  It's common for beginner programmers to blame JavaScript, but that should be your last resort. Remember that JavaScript has been used to solve introductory coding problems millions of times by millions of other programmers. So, JavaScript is probably not the problem.

In this chapter, we will discuss in detail common types of bugs, along with some strategies that can be affective for debugging. You will learn to rely on error messages and ``console.log`` statements for clues and insight, and over time you will sharpen your debugging skills. We will also discuss how to approach writing code so as to prevent bugs from occuring in the first place.
