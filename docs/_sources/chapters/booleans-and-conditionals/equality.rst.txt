.. _equality:

Equality
========

Loose Equality With ``==``
--------------------------

.. index:: equality, ==

In the section :ref:`booleans`, we learned about the comparison operators ``==`` and ``!=``, which test whether two values are equal or not equal, respectively. We also tipped you off to some quirks of the ``==`` operator. Specifically, when its operands are of different types, then the returned boolean value may not be what you expect.

.. admonition:: Example

   .. sourcecode:: js

      console.log(7 == "7");
      console.log(0 == false);
      console.log(0 == '');

   **Output**

   ::

      true
      true
      true

.. index::
   single: equality; loose

When we give ``==`` operands of different data types, it will still try to make a comparison. In order to properly do so, the values must be both be of the same type. JavaScript will implicitely convert the operands so that they are of the same type, and then compare the converted values to generate ``true`` or ``false``. For this reason, the ``==`` operator is often said to measure **loose equality**.

Type conversions with ``==`` are carried out according to a `complex set of rules <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#Loose_equality_using>`_, and while many of these conversions make some sense, others do not. 

For example, ``Number("7")`` returns ``7``, so it makes some sense that ``7 == "7"`` returns ``true``. However, the following example leaves us scratching our heads.

.. admonition:: Example

   .. sourcecode:: js
    
      console.log('0' == 0);
      console.log(0 == '');
      console.log('0' == '');

   **Output**

   ::

      true
      true
      false

.. index::
   single: equality; non-transitive

This example demonstrates that ``==`` is **non-transitive**. We intuitively think of the concept of equality as being transitive. In other words, if A and B are equal, and B and C are equal, then A and C should also be equal. The example above demonstrates that this is **not** the case for the ``==`` operator. 

Since ``==`` does not follow rules that we typically associate with quality, unexpected results can occur when relying on it in our programs. Thankfully, JavaScript provides another operator that returns more predictable results.

Strict Equality With ``===``
----------------------------

.. index:: ! ===

The operator ``===`` compares two operands *without* converting their data types. In other words, if ``a`` and ``b`` are of different data types (say, ``a`` is a string and ``b`` is a number) then ``a === b`` will always be false.

.. admonition:: Example

   .. sourcecode:: js

      console.log(7 === "7");
      console.log(0 === false);
      console.log(0 === '');

   **Output**

   ::

      false
      false
      false

.. index::
   single: equality; strict

For this reason, the ``===`` operator is often said to measure **strict equality**.

.. index:: ! !==

Just as equality operator ``==`` has the inequality operator ``!=``, there is also a strict inquality operator, ``!==``. The boolean expression ``a !== b`` returns ``true`` when the two operands are of different types, or if they are of the same type and have different values. 

.. tip:: Use ``===`` and ``!==`` whenever possible. In this book we will use these strict operators over the loose operators from now on.

Check Your Understanding
------------------------

.. admonition:: Question

   What is the result of the following boolean expression?
   
   .. sourcecode:: js

      4 == "4"

   #. ``true``
   #. ``false``
   #. ``"true"``
   #. ``"false"``

.. admonition:: Question

   What is the difference between ``==`` and ``===``?

   #. There is no difference; they work exactly the same
   #. Only ``===`` throws an error if its arguments are of different types
   #. ``==`` will try to convert values of different types to be the same type, while ``===`` does no such conversion
   #. ``==`` works with all data types, while ``===`` works only with strings
