Combining ``Math`` Methods
===========================

The ``Math`` methods provide useful actions, but each one is fairly specific in
what it does (e.g. taking a square root). At first glance, this might seem to
limit how often we need to call on ``Math``. However, the methods can be
manipulated or combined to produce some clever results.

.. _random-array-item:

Random Selection From an Array
-------------------------------

To select a random item from the array ``happiness = ['Hope', 'Joy', 'Peace',
'Love', 'Kindness', 'Puppies', 'Kittens', 'Tortoise']``, we need to randomly
generate an index value from 0 to 7. Since ``Math.random()`` returns a
decimal number between 0 and 1, the method on its own will not work.

The :ref:`Math.random <random-integers>` appendix page describes how to
generate random integers by combining the ``random`` and ``floor`` methods. We
will use this functionality now.

Let's define a function that takes an array as a parameter. Since we might not
know how many items are in the array, we cannot multiply ``Math.round()`` by a
specific value.  Fortunately, we have the ``length`` property…

.. admonition:: Example

   .. replit:: js
      :linenos:
      :slug: KindnessSelection

      function randomSelection(arr){
         let index = Math.floor(Math.random()*arr.length);
         return arr[index];
      }

      let happiness = ['Hope','Joy','Peace','Love','Kindness','Puppies','Kittens','Tortoise'];

      for (i=0; i < 8; i++){
         console.log(randomSelection(happiness));
      }

   **Console Output**
   ::

      Tortoise
      Love
      Kindness
      Hope
      Kittens
      Kindness
      Love
      Hope

The ``happiness`` array has a length of 8, so in line 2
``Math.floor(Math.random()*arr.length)`` evaluates as
``Math.floor(Math.random()*8)``, which generates an integer from 0 to 7.
Line 3 then returns a random selection from the array.

.. _rounding-to-decimal-places:

Rounding to Decimal Places
---------------------------

The ``ceil``, ``floor``, and ``round`` methods all take a decimal value and
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

Check Your Understanding
-------------------------

.. admonition:: Question

   Which of the following correctly rounds 12.3456789 to 4 decimal places?

   a. ``Math.round(12.3456789)*100/100``
   b. ``Math.round(12.3456789*100)/100``
   c. ``Math.round(12.3456789*10000)/10000``
   d. ``Math.round(12.3456789)*10000/10000``
