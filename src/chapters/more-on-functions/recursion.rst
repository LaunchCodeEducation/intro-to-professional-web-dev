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

   **Output**

   .. sourcecode:: js

      14

When called, the parameter ``num`` is passed an argument, which in this case is
the number 12. The function executes and returns the value 14, which is then
printed by the ``console.log`` statement.

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

   **Output**

   .. sourcecode:: js

      17

Of course, there is no need to write a function to add 5 to a value, but the
example demonstrates calling a function from within another function.

Next Step: What is 'Recursion'?
--------------------------------

.. index:: ! recursion

**Recursion** is the process of solving a larger problem by breaking it into
small, easy steps that *can all be solved in exactly the same way*.

Splitting a large task into small, identical pieces allows us to reuse a single
function rather than coding several different functions.

Solving the big problem involves completing and combining the smaller parts.
We accomplish this either by setting up a loop to call one function lots of
times or by using the strength of recursion.

Here is the clever idea behind recursion.  Instead of a loop, a function simply
calls *itself* over and over again until the larger problem is solved.

.. admonition:: **Recursion in a nutshell:**

   a. Split a big problem into small, identical pieces.
   b. Build a single function to solve those pieces.
   c. The function repeatedly calls itself until all the pieces are solved.

Many new programmers (and even veteran ones) find recursion an abstract and
tricky concept. One helpful way to approach the idea is to walk through an
example.
