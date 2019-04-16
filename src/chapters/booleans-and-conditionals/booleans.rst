.. _booleans:

Booleans
========

.. index:: data type

One of the core features of any programming language is the ability to conditionally execute a segment of code. This means that a program will run a segment of code *only if* a given condition is met. Another way to say this is that the segment of code runs *only if* the program is in a particular state.

.. admonition:: Example

   Consider a banking application that can remind you when a bill is due. The application will notify you that a bill is due soon, but *only if* the bill has not already been paid.

In this example, we can phrase the condition as follows: Send a notification if "the bill is unpaid" is true. In order to formalize such a statement in code, we need a notion of what it means to be true or false.

Boolean Values
--------------

.. index:: ! true, ! false, ! boolean

.. index::
   single: boolean; value

The JavaScript data type for storing true and false values is called ``boolean``, named after the British mathematician, George Boole. George Boole created `Boolean Algebra <https://en.wikipedia.org/wiki/Boolean_algebra>`_ which is the basis of all modern computer arithmetic.

There are only two **boolean values**---``true`` and ``false``. As always, JavaScript is case-sensitive, so ``True`` and ``False`` are not valid boolean values.

.. admonition:: Example

   .. sourcecode:: js

      console.log(true);
      console.log(typeof true);
      console.log(typeof false);

   **Output**

   ::

      true
      boolean
      boolean

It is extremely important to realize that ``true`` and ``false`` are **not** strings. Surrounding the words "true" and "false" in quotes in JavaScript will result in string values rather than boolean values. 

.. admonition:: Example

   .. sourcecode:: js

      console.log(typeof true);
      console.log(typeof "true");

   **Output**

   ::

      boolean
      string

Boolean Conversion
------------------

.. index:: ! Boolean(), type conversion

As with the number and string data types, the boolean type also has a conversion function, ``Boolean()``. It works similarly to ``Number()`` and ``String()``, attempting to convert a non-boolean value to a boolean.

.. admonition:: Try It!

   Explore how ``Boolean()`` converts various non-boolean values.

   .. sourcecode:: js

      console.log(Boolean("true"));
      console.log(Boolean("TRUE"));
      console.log(Boolean(0));
      console.log(Boolean(1));
      console.log(Boolean(''));
      console.log(Boolean('LaunchCode'));

   `Run this program at repl.it <https://repl.it/@launchcode/Boolean-Type-Conversion>`_

   Under which conditions does ``Boolean()`` convert a string to ``true``?

   #. Only when the string is ``"true"``.
   #. Whenever the string contains any non-whitespace character.
   #. Whenever the string is non-empty.
   #. Never. It converts all strings to ``false``.


Boolean Expressions
-------------------

.. index::
   single: boolean; expression

.. index::
   single: operator; equality

.. index:: ! ==

A **boolean expression** is an expression that evaluates to a boolean value. The equality operator, ``==``, compares two values and produces a boolean value related to whether the two values are equal to one another.

.. admonition:: Example

   .. sourcecode:: js

      console.log(5 == 5);
      console.log(5 == 6);

   **Output**

   ::

      true
      false

In the first statement, the two operands are equal, so the expression evaluates to ``true``. In the second statement, 5 is not equal to 6, so we get ``false``.

We can also use ``==`` to see that ``true`` and ``"true"`` are not equal.

.. admonition:: Example

   .. sourcecode:: js

      console.log(true == "true");

   **Output**

   ::

      false

Comparison Operators
^^^^^^^^^^^^^^^^^^^^

.. index::
   single: operator; comparison

The ``==`` operator is one of six common **comparison operators**.

.. index:: ==, ! !=, ! <, ! >, ! <=, ! >=

.. list-table:: Comparison Operators
   :widths: auto
   :header-rows: 1

   * - Operator
     - Description
     - Examples Returning ``true``
   * - Equal (``==``)
     - Returns ``true`` if the two operands are equal, and ``false`` otherwise.
     - ``7 == 7``

       ``"dog" == "dog"``
   * - Not equal(``!=``)
     - Returns ``true`` if the two operands are not equal, and ``false`` otherwise.
     - ``7 != 5``

       ``"dog" != "cat"``
   * - Greater than (``>``)
     - Returns ``true`` if the left-hand operand is greater than the right-hand operand, and ``false`` otherwise.
     - ``7 > 5``

       ``'b' > 'a'``
   * - Less than (``<``)
     - Returns ``true`` if the left-hand operand is less than the right-hand operand, and ``false`` otherwise.
     - ``5 < 7``

       ``'a' < 'b'``
   * - Greater than or equal (``>=``)
     - Returns ``true`` if the left-hand operand is greater than or equal to the right-hand operand, and ``false`` otherwise.
     - ``7 >= 5``

       ``7 >= 7``

       ``'b' >= 'a'``
       
       ``'b' >= 'b'``
   * - Less than or equal (``<=``)
     - Returns ``true`` if the left-hand operand is less than or equal to the right-hand operand, and ``false`` otherwise.
     - ``5 <= 7``

       ``5 <= 5``

       ``'a' <= 'b'``

       ``'a' <= 'a'``


Although these operations are probably familiar, the JavaScript symbols are different from the mathematical symbols. A common error is to use a single equal sign (``=``) instead of a double equal sign (``==``). Remember that ``=`` is an *assignment* operator and ``==`` is a *comparison* operator. Also note that ``=<`` and ``=>`` are not recognized operators.

An equality test is symmetric, meaning that we can swap the places of the operands and the result is the same.  For a variable ``a``, if ``a == 7`` is ``true`` then ``7 == a`` is also ``true``. However, an assignment statement is not symmetric: ``a = 7`` is legal while ``7 = a`` is not.

.. warning:: If you explore the equality operator in more depth, you will find some suprises. For example, the following comparisons return ``true``:

   - ``7 == "7"``
   - ``0 == false``
   - ``0 == ''``

   We will explore the nuances of ``==`` in the upcoming section :ref:`equality`, and introduce two new operators, ``===`` and ``!==``, that will align more closely with our intuitive notion of equality.

Check Your Understanding
------------------------

.. admonition:: Question

   Which of the following is a Boolean expression? Select all that apply.

   #. ``3 == 4``
   #. ``3 + 4``
   #. ``3 + 4 === 7``
   #. ``"false"``
