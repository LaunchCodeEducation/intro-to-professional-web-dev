``Math`` Wrap-Up
=================

The ``Math`` methods provide useful actions, but each one is fairly specific in
what it does (e.g. taking a square root). At first glance, this might seem to
limit how often we need to call on ``Math``. However, the methods can be
manipulated to produce some clever results - as we saw when we selected random
entries from an array.

Another Clever Trick
---------------------

The ``ceil``, ``floor`` and ``round`` methods all take a decimal value and
return an integer, but what if we wanted to round 5.56789123 to two decimal
places? Let's explore how to make this happen by starting with a simpler
example.

``Math.round(1.23)`` returns 1, but what if we want to round to one decimal
place (1.2)? We cannot alter what ``round`` does---it *always* returns an
integer. However, we CAN change the number used as the argument.

Let's multiply 1.23 by 10 (1.23*10  = 12.3) and then apply the method.
``Math.round(12.3)`` returns 12. Why do this? Well, if we divide 12 by 10
(12/10 = 1.2) we get the result of *rounding 1.23 to one decimal place*.

Combining these steps gives us ``Math.round(1.23*10)/10``, which returns the
value 1.2.

Let's return to 5.56789123 and step through the logic for rounding to two
decimal places:

.. list-table::
   :header-rows: 1

   * - Step
     - Description
   * - ``Math.round(5.56789123*100)/100``
     - Evaluate the numbers in () first: 5.56789123\*100 = 556.789123

   * - ``Math.round(556.789123)/100``
     - Apply the ``round`` method to 556.789123

   * - ``557/100``
     - Perform the division 557/100 = 5.57

The clever trick for rounding to decimal places is to multiply the original
number by some factor of 10, ``round`` the result, then divide the integer by
the same factor of 10. The number of digits we want after the decimal are
shifted in front of the '.' before rounding, then moved back into place by the
division.

.. list-table:: Rounding to Decimal Places
   :header-rows: 1

   * - Decimal Places In Answer
     - Multiply & Divide By
     - Syntax
   * - 1
     - 10
     - ``Math.round(number*10)/10``

   * - 2
     - 100
     - ``Math.round(number*100)/100``

   * - 3
     - 1000
     - ``Math.round(number*1000)/1000``

   * - etc.
     - etc.
     - etc.

``Math`` Redundancy
--------------------

2**4 vs. Math.pow(2,4).

``Math.round()`` to decimals vs. ``toFixed``.

   Do we want to include these examples?

Check Your Understanding
-------------------------

.. admonition:: Question

   Which of the following correctly rounds 12.3456789 to 4 decimal places?

   a. ``Math.round(12.3456789)*100/100``
   b. ``Math.round(12.3456789*100)/100``
   c. ``Math.round(12.3456789*10000)/10000``
   d. ``Math.round(12.3456789)*10000/10000``
