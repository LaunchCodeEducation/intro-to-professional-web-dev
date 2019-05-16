.. _ceilfloortrunc-examples:

``Math.ceil``, ``floor``, and ``trunc`` Examples
=================================================

``Math.ceil``
--------------

The general syntax for this method is:

::

   Math.ceil(number)

This method rounds a decimal value UP to the next integer (hence the
*ceiling* reference in the name). Integer values remain the same.

``ceil`` also operates on arrays (:ref:`see below <cft-array>`).

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.ceil(8.88));

      console.log(Math.ceil(8.1));

      console.log(Math.ceil(-3.9));

      console.log(Math.ceil(5));

   **Console Output**
   ::

      9
      9
      -3
      5

.. _floor:

``Math.floor``
--------------

The general syntax for this method is:

::

   Math.floor(number)

This method is the opposite of ``Math.ceil``. It rounds a decimal value DOWN to
the previous integer. Integer values remain the same.

``floor`` also operates on arrays (:ref:`see below <cft-array>`).

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.floor(8.88));

      console.log(Math.floor(8.1));

      console.log(Math.floor(-3.9));

      console.log(Math.floor(5));

   **Console Output**
   ::

      8
      8
      -4
      5

.. _trunc:

``Math.trunc``
--------------

The general syntax for this method is:

::

   Math.trunc(number)

This method removes any decimals and returns only the integer part of ``number``.

``trunc`` also operates on arrays (:ref:`see below <cft-array>`).

Numerical strings can also be evaluated, but should be avoided as a best
practice.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.trunc(8.88));

      console.log(Math.trunc(10.000111));

   **Console Output**
   ::

      8
      10

.. note::

   At first glance, ``Math.floor`` and ``Math.trunc`` appear to do exactly the
   same thing. However, a closer look shows that the two methods treat negative numbers
   differently.

   .. sourcecode:: js
      :linenos:

      console.log(Math.floor(-15.88));

      console.log(Math.trunc(-15.88));

   **Console Output**
   ::

      -16
      -15

.. _cft-array:

Combine with ``map``
---------------------

When combined with the :ref:`map array method <map-method>`, ``ceil``, ``floor``, and ``trunc``
will operate on each entry in an array. The syntax for this is:

::

   arrayName.map(Math.method)

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [-2, 3.33, -4.44, 8.88];

      console.log(numbers.map(Math.ceil));
      console.log(numbers.map(Math.floor));
      console.log(numbers.map(Math.trunc));

   **Console Output**
   ::

      [ -2, 4, -4, 9 ]
      [ -2, 3, -5, 8 ]
      [ -2, 3, -4, 8 ]
