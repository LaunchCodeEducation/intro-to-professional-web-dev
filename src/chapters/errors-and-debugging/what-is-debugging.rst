What is Debugging?
==================

.. index:: ! debugging, ! bug

Programming is a complex process. Since it is done by human beings, errors often occur. Programming errors are called **bugs** and the process of tracking them down and correcting them is called **debugging**.  

Some claim that in 1947, a dead moth caused a problem in one of the first computers. The term "bug" has remained in use since, to refer to any issue that prevents a program from working as intended. Wikipedia even has an image of the supposed `first bug <http://en.wikipedia.org/wiki/File:H96566k.jpg>`_.

.. index::
   single: error; syntax
   single: error; runtime
   single: error; logic

Three kinds of errors can occur in a program: **syntax errors**, **runtime errors**, and **logic errors**. We will first learn about each type of error, and then we will discuss strategies for debugging code and reducing errors.

Beginning Tips for Debugging
----------------------------

Debugging a program requires a different approach compared to writing the original code. As you debug, think of yourself as a detective. Something has gone wrong, and you must use clues, experience, intuition, trial and error, and an inquisitive spirit to solve the problem.

Oftentimes, you will find it tempting to blame errors on JavaScript itself. However, it is far, far more likely that the error is due to an issue with your code. We encourage you to think critically about the code you have written, and whether you may have made an error in writing your code. Even senior developers make basic errors on occasion!

In this chapter, we will discuss in detail common types of bugs, along with some effective strategies for debugging. You will learn to rely on error messages and ``console.log`` for clues and insight, and over time you will sharpen your debugging skills. We will also discuss how to approach writing code so as to prevent bugs from occurring in the first place.
