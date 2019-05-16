.. _round-examples:

``Math.round`` Examples
========================

The general syntax for this method is:

::

   Math.round(number)

This method returns ``number`` rounded to the nearest integer value.

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.round(1.33));
      console.log(Math.round(-28.7));
      console.log(Math.round(8.5));
      console.log(Math.round("101.45"));

   **Console Output**
   ::

      1
      -29
      9
      101

``Math.round`` also works on arrays, but must be combined with the
:ref:`map array method <map-method>`. The syntax for this is:

::

   arrayName.map(Math.round)

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [1.33, 4, 8.5, -15.523, 8.49];

      console.log(numbers.map(Math.round));

   **Console Output**
   ::

      [ 1, 4, 9, -16, 8 ]
