Recursion
==========

Quick Review
-------------

In the previous chapter, we learned how to define a function and its
parameters.

.. admonition:: Example

   .. sourcecode:: js

      function addTwoToNumber(num){
         return num += 2;
      }

      console.log(addTwoToNumber(12));

   **Console Output**

   ::

      14

When called, the parameter ``num`` is passed an argument, which in this case is
the number ``12``. The function executes and returns the value ``14``, which
the ``console.log`` statement prints.

Functions Can Call Other Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions should only accomplish one (preferably simple) task. To solve more
complicated tasks, one small function must call other functions.

.. admonition:: Example

   .. sourcecode:: js

      function addTwoToNumber(num){
         return num += 2;
      }

      function addFiveToNumber(value){
         let result = addTwoToNumber(value) + 3;
         return result;
      }

      console.log(addFiveToNumber(12))

   **Console Output**

   ::

      17

Of course, there is no need to write a function to add 5 to a value, but the
example demonstrates calling a function from within another function.

.. index:: ! recursion

What Is Recursion?
-------------------

In programming, the *divide and conquer* strategy solves a problem by breaking
it down into smaller, simpler pieces. If these pieces *can all be solved in
exactly the same way*, then we gain an additional advantage. Solving the big
problem becomes a process of completing and combining the smaller parts.

Splitting up a large task into smaller, identical pieces allows us to reuse a
single function rather than coding several different functions. We accomplish
this by either:

a. Setting up a loop to call one function lots of times, OR
b. Building a function that splits up the large problem for us, until a *simplest
   case* is found and solved.

**Recursion** is the process of solving a larger problem by breaking it into
smaller pieces that *can all be solved in exactly the same way*. The clever
idea behind recursion is that instead of using a loop, a function simply
calls *itself* over and over again, with each step reducing the size of the
problem.

Through recursion, a problem eventually gets reduced to a very simple task,
which can be immediately solved. This small answer sets up the solution for the
previous step, which in turn solves the next bigger step. Properly built, the
function combines all of the small answers to solve the original problem.

Many new programmers (and even veteran ones) find recursion an abstract and
tricky concept. One helpful way to approach the idea is to walk through an
example.
