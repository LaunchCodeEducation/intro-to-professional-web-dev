.. _abs-examples:

``Math.abs`` Examples
======================

The general syntax for this method is:

::

   Math.abs(number)

This method returns the positive value of a number, which can be printed or
stored in a variable. ``abs`` works on both integer and decimal values.

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let num = Math.abs(-3);
      console.log(num);

      console.log(Math.abs(4.44));
      console.log(Math.abs('-3.33'));

      console.log(Math.abs(24/-3));
      // 24/-3 = -8

   **Console Output**
   ::

      3
      4.44
      3.33
      8

``Math.abs`` also works on arrays, but to make the process work, we must
combine it with the :ref:`map array method <map-method>`. The syntax for this
is:

::

   arrayName.map(Math.abs)

Note that ``Math.abs`` takes no argument when applied to an array.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [-2, 3, -4.44, "8.88"];

      let positiveArray = numbers.map(Math.abs);

      console.log(positiveArray);

   **Console Output**
   ::

      [2, 3, 4.44, 8.88]
