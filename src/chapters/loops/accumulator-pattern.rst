The Accumulator Pattern
=======================

.. index:: ! pattern

A **pattern** is a commonly-used approach to solve a group of similar programming problems.

This section introduces your first pattern, which we will explore in-depth after looking at a motivating example.

Adding 1...n
------------

Let's write a program that adds up the integers 1...n, where ``n`` is an integer variable that we will create.

If you were to do this with pen and paper, you would write out a single formula and compute the answer. For example, for n = 6 you would write:

::

   1 + 2 + 3 + 4 + 5 + 6

To get the result, you would first add 1 and 2 to get 3. Then you would add 3 and 3 to get 6. Then you would add 6 and 4 to get 10, and so on. The final result is 21.

We can carry out this same procedure in code using a loop.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let n = 6;
      let total = 0;

      for (let i = 1; i <= n; i++) {
         total += i;
      }

      console.log(total);

   **Console Output**

   ::

      21

The variable ``total`` is initialized to 0. The loop executes once each for the values of ``i`` from 1 to 6. Each time the loop body executes, the next value of ``i`` is added to ``total``.

The loop carries out the same basic algorithm that we used to compute the sum
``1 + 2 + 3 + 4 + 5 + 6`` by hand. The only step that may seem different to you
is the use of the variable ``total`` to keep track of the running total. When
calculating the sum using pen and paper, we rarely write down this part,
keeping track of the running total in our head. With programming, however, we
must explicitly store such a value in a variable.

.. index:: ! accumulator, ! accumulator pattern

.. index::
   single: pattern, accumulator

This pattern of initializing a variable to some basic, or empty value, and
updating it within a loop is commonly referred to as the
**accumulator pattern**. We refer to the variable as the **accumulator**. In
the example above, ``total`` is the accumulator, and it "accumulates" the
individual integers one by one.

The accumulator pattern comes up regularly in programming. The key to using it successfully is to initialize the accumulator variable before you start the iteration. Once inside the loop, update the accumulator.

.. _reverse-string:

Reversing a String
------------------

While some programming languages have a string method that will reverse a given string, JavaScript does not. Let's see how we can write our own program that reverses a string using the accumulator pattern.

We'll start by initializing two variables: the string we want to reverse, and a variable that will eventually store the reversed value of the given string.

.. sourcecode:: js
   :linenos:

   let str = "blue";
   let reversed = "";

Here, ``reversed`` is our accumulator variable. Our approach to reversing the string will be to loop over ``str``, adding each subsequent character to the *beginning* of ``reversed``, so that the first character becomes the last, and the last character becomes the first.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let str = "blue";
      let reversed = "";

      for (let i = 0; i < str.length; i++) {
         reversed = str[i] + reversed;
      }

      console.log(reversed);

   **Console Output**

   ::

      eulb

Notice that we don't use the ``+=`` operator within the loop, since ``reversed += str[i]`` is the same as ``reversed = reversed + str[i]``.

Let's break this down step-by-step. This table shows the values of each of our variables *after* each loop iteration.

.. list-table:: The accumulator pattern, step by step
   :header-rows: 1

   * - Loop iteration
     - ``i``
     - ``str[i]``
     - ``reversed``
   * - (before first iteration)
     - not defined
     - not defined
     - ``""``
   * - 1
     - 0
     - ``"b"``
     - ``"b"``
   * - 2
     - 1
     - ``"l"``
     - ``"lb"``
   * - 3
     - 2
     - ``"u"``
     - ``"ulb"``
   * - 4
     - 3
     - ``"e"``
     - ``"eulb"``

.. admonition:: Try It!

   What happens if you reverse the order of the assignment statement within the ``for`` loop, so that ``reversed = reversed + str[i];``?

   `Try it at repl.it. <https://repl.it/@launchcode/Reversing-a-string>`_

Summing an Array
----------------

Another common use of the accumulator pattern is to compute some value using each of the elements of an array. This is similar to adding 1...n as we did above, with the difference being we will use the items in an array rather than 1...n.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [2, -5, 13, 42];
      let total = 0;

      for (let i = 0; i < numbers.length; i++) {
         total += numbers[i];
      }

   **Console Output**

   ::

      52

