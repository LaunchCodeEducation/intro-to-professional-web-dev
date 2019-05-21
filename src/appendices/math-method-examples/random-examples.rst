.. _random-examples:

``Math.random`` Examples
=========================

The general syntax for this method is:

::

   Math.random()

This method returns a random decimal value between 0 and 1, which can be stored
in a variable or used in a calculation.

Note that 0 is a possible selection, but 1 is NOT.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      for (i=0; i<5; i++){
         let randNum = Math.random();
         console.log(randNum);
      }

   **Console Output**
   ::

      0.34992592600591066
      0.11861535165960668
      0.019710093901842862
      0.7751799992655235
      0.46782849511194136

.. _random-integers:

Generate a Random Integer
--------------------------

If a random integer must be generated, the result of ``Math.random()`` can be
manipulated with operators (``+, -, *, /``) and other ``Math`` methods.

The trick to creating a random integer is to multiply ``Math.random()`` by a
whole number and then round the result to remove the decimal portion. The
choice of using the ``ceil``, ``floor``, or ``round`` method affects the
numbers generated.

Explore the example below:

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      for (i=0; i < 5; i++){
         let num = Math.random()*10;
         console.log(`floor = ${Math.floor(num)}, ceil = ${Math.ceil(num)}, round = ${Math.round(num)}`);
      }

   **Console Output**
   ::

      floor = 0, ceil = 1, round = 0
      floor = 6, ceil = 7, round = 7
      floor = 2, ceil = 3, round = 3
      floor = 8, ceil = 9, round = 8
      floor = 9, ceil = 10, round = 10

After multiplying ``Math.random()`` by 10, applying the ``floor`` method gives
numbers between 0 and 9. Using the ``ceil`` method shifts the range up one
digit, generating values between 1 and 10. Using the ``round`` method gives the
widest range, generating numbers between 0 and 10.

Rather than trying to remember which method to use, one choice is to ALWAYS
use ``floor`` to round to an integer:

#. ``Math.floor(Math.random()*10)`` generates a number from 0 - 9.
#. ``Math.floor(Math.random()*120)`` generates a number from 0 - 119.

To start our range at 1, just add 1 to the rounded value:

#. ``Math.floor(Math.random()*10) + 1``  generates a number from 1 - 10.
#. ``Math.floor(Math.random()*120) + 1``  generates a number from 1 - 120.

By changing the value that multiplies ``Math.random()`` we specify the range
for the numbers we want to generate.

#. ``Math.floor(Math.random()*maxValue)``  generates a number from
   0 to (``maxValue``-1).
#. ``Math.floor(Math.random()*maxValue) + 1``  generates a number from
   1 to ``maxValue``.

.. admonition:: Try It

   Explore generating random numbers at this `repl.it <https://repl.it/@launchcode/RandomNumberPractice>`__.

   #. Generate random integers from 1 - 100.
   #. Generate random integers from -5 - 0, but NOT including 0.
   #. *Challenge*: Generate random integers from 20 - 30.
