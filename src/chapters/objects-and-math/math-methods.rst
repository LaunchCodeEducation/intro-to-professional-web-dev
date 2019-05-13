.. _math-methods:

Math Methods
=============

As with strings and arrays, JavaScript provides some built-in *methods* for the
``Math`` object.

Common Math Methods
--------------------

The ``Math`` object contains over 30 methods. Here is a sample of the most
frequently used Math methods. More complete lists can be found here:

#. `W3 Schools Math Reference <https://www.w3schools.com/jsref/jsref_obj_math.asp>`__
#. `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math>`__

To see detailed examples for a particular method, control-click
(or right-click) on its name.

.. list-table:: Ten Common Math Methods
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`abs <abs-examples>`
     - ``Math.abs(number)``
     - Returns the positive value of ``number``.

   * - :ref:`ceil <ceilfloortrunc-examples>`
     - ``Math.ceil(number)``
     - Rounds ``number`` UP to the closest integer value.

   * - :ref:`floor <floor>`
     - ``Math.floor(number)``
     - Rounds ``number`` DOWN to the closest integer value.

   * - :ref:`max <max-and-min-examples>`
     - ``Math.max(x,y,z,...)``
     - Returns the largest value from a set of numbers.

   * - :ref:`min <min>`
     - ``Math.min(x,y,z,...)``
     - Returns the smallest value from a set of numbers.

   * - :ref:`pow <pow-examples>`
     - ``Math.pow(x,y)``
     - Returns the value of x raised to the power of y.

   * - :ref:`random <random-examples>`
     - ``Math.random()``
     - Returns a random decimal value between 0 and 1, NOT including 1.

   * - :ref:`round <round-examples>`
     - ``Math.round(number)``
     - Returns ``number`` rounded to the nearest integer value.

   * - :ref:`sqrt <square-root>`
     - ``Math.sqrt(number)``
     - Returns the square root of ``number``.

   * - :ref:`trunc <trunc>`
     - ``Math.trunc(number)``
     - Removes any decimals and returns the integer part of ``number``.

Check Your Understanding
------------------------

Follow the links in the table above for the ``floor``, ``random``, ``round``
and ``trunc`` methods. Review the content and then answer the following
questions.

.. admonition:: Question

   Which of the following returns ``-3`` when applied to ``-3.87``?

   a. ``Math.floor(-3.87)``
   b. ``Math.random(-3.87)``
   c. ``Math.round(-3.87)``
   d. ``Math.trunc(-3.87)``

.. admonition:: Question

   What is printed by the following program?

   .. sourcecode:: js

      let num = Math.floor(Math.random()*10);

      console.log(num);

   a. A random number between 0 and 9.
   b. A random number between 0 and 10.
   c. A random number between 1 and 9.
   d. A random number between 1 and 10.

.. admonition:: Question

   What is printed by the following program?

   .. sourcecode:: js

      let num = Math.round(Math.random()*10);

      console.log(num);

   a. A random number between 0 and 9.
   b. A random number between 0 and 10.
   c. A random number between 1 and 9.
   d. A random number between 1 and 10.
