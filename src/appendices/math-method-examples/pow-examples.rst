.. _pow-examples:

``Math.pow`` and ``Math.sqrt`` Examples
=======================================

``Math.pow``
-------------

The general syntax for this method is:

::

   Math.pow(x, y)

This method calculates and returns the value of x raised to the power of y
(x :sup:`y`), and it is identical to the ``x**y`` operation. The *pow* name
refers to the operation *to the power of*.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(3**4);
      console.log(Math.pow(3,4));
      //3 raised to the power of 4 = 3*3*3*3

   **Console Output**
   ::

      81
      81

.. _square-root:

``Math.sqrt``
--------------

The general syntax for this method is:

::

   Math.sqrt(number)

This method calculates and returns the square root of ``number``, and it is a
shortcut for using the fraction 1/2 in the ``pow`` method.

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.sqrt(81));
      console.log(Math.pow(81,1/2));

      console.log(Math.sqrt(111));
      console.log(Math.sqrt("36"));

   **Console Output**
   ::

      9
      9
      10.535653752852738
      6

``Math.sqrt`` also works on arrays, but must be combined with the
:ref:`map array method <map-method>`. The syntax for this is:

::

   arrayName.map(Math.sqrt)

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [2, 16, 100, 121];

      console.log(numbers.map(Math.sqrt));

   **Console Output**
   ::

      [ 1.4142135623730951, 4, 10, 11 ]
