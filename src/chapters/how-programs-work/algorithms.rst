Introduction
=============

   "It'll take a few moments to get the coordinates from the navicomputer."
   - Han Solo

.. index:: ! program

Given a set of inputs, Han's computer analyzes the data and returns information
about safely navigating a hyperspace jump. The computer does this by running a
**program**.

At the most basic level, a *program* is a set of instructions that tell a
computer or other machine what to do. These instructions consist of a set of
commands, calculations, and manipulations that achieve a specific result.
However, the computer cannot solve the problem on its own. Someone---a
programmer---had to figure out a series of steps for the computer to follow.
Also, the programmer had to write these steps in a way the computer can
understand.

Algorithms
----------

Imagine following a recipe for baking a batch of cookies. After the list of
ingredients comes a series of step-by-step instructions for producing the
treats. If you want to make something else, like a cake or a roast, you follow
a different set of steps using a different set of ingredients.

.. index:: ! algorithm

An **algorithm** is like a recipe. It is a systematic series of steps that,
when followed, produce a specific result to help solve a problem. Programmers
design algorithms to solve these small steps in a carefully planned way. The
results then get combined to produce a final answer or action.

Let's take a look at an example of an algorithm---alphabetizing a list of
words:

``apple, pear, zebra, box, rutabaga, fox, banana, socks, foot``

One possible set of steps for solving the task could be:

#. Arrange the words from a - z based only on the first letter:

   ``apple, box, banana, fox, foot, pear, rutabaga, socks, zebra``

#. If more than one word starts with 'a', rearrange those words based on the
   second letter. Repeat for the words that start with 'b', then 'c', etc.:

   ``apple, banana, box, fox, foot, pear, rutabaga, socks, zebra``

#. If multiple words start with 'a' and have the same second letter, rearrange
   those words based on the third letter. Repeat for the 'b' words, then the
   'c' words, etc.:

   ``apple, banana, box, foot, fox, pear, rutabaga, socks, zebra``

#. If other repeats exist, continue sorting the list by comparing the 4th, 5th,
   6th letters (etc.) until all the words are properly arranged.

This is not the ONLY way to solve the task, but it provides a series of steps
that can be used in many different situations to organize different lists of
words.

Alphabetizing is a process we can teach a computer to do, and the algorithm
will complete the process much more rapidly than a human. However, unlike the
alphabet song that many of us still sing in our heads when arranging a list of
words, programmers must use a different method to train the computer.

Check Your Understanding
-------------------------

.. admonition:: Question

   Select ALL of the following that can be solved by using an algorithm:

   a. Answering a math problem.
   b. Sorting numbers in decreasing order.
   c. Making a peanut butter and jelly sandwich.
   d. Assigning guests to tables at a wedding reception.
   e. Creating a grocery list.
   f. Suggesting new music for a playlist.
   g. Making cars self-driving.
