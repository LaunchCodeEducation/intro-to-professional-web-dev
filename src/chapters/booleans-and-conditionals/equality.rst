.. _equality:

Equality
========

Loose Equality With ``==``
--------------------------

.. index:: equality, ==

In the section :ref:`booleans`, we learned about the comparison operators ``==`` and ``!=``, which test whether two values are equal or not equal, respectively. However, there are some quirks with using the ``==`` operator, which occur when we use ``==`` to compare different data types.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(7 == "7");
      console.log(0 == false);
      console.log(0 == '');

   **Console Output**

   ::

      true
      true
      true

.. index::
   single: equality; loose


In order to properly make a comparison, the two operands must be the same type. If the two operands to ``==`` are of different data types, JavaScript will implicitly convert the operands so that the values are of the same data type before comparing the two. For this reason, the ``==`` operator is often said to measure **loose equality**.

Type conversions with ``==`` are carried out according to a `complex set of rules <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#Loose_equality_using>`_, and while many of these conversions make some sense, others do not. 

For example, ``Number("7")`` returns ``7``, so it makes some sense that ``7 == "7"`` returns ``true``. However, the following example leaves us scratching our heads.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:
    
      console.log('0' == 0);
      console.log(0 == '');
      console.log('0' == '');

   **Console Output**

   ::

      true
      true
      false

.. index::
   single: equality; non-transitive

The ``==`` operator is **non-transitive**. We think of equality as being transitive; for example, if A and B are equal and B and C are equal, then A and C are also equal. However, the example above demonstrates that that is *not* the case for the ``==`` operator.

Since ``==`` does not follow rules that we typically associate with equality, unexpected results may occur if ``==`` is used in a program. Thankfully, JavaScript provides another operator that returns more predictable results.

Strict Equality With ``===``
----------------------------

.. index:: ! ===

The operator ``===`` compares two operands *without* converting their data types. In other words, if ``a`` and ``b`` are of different data types (say, ``a`` is a string and ``b`` is a number) then ``a === b`` will always be false.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(7 === "7");
      console.log(0 === false);
      console.log(0 === '');

   **Console Output**

   ::

      false
      false
      false

.. index::
   single: equality; strict

For this reason, the ``===`` operator is often said to measure **strict equality**.

.. index:: ! !==

Just as equality operator ``==`` has the inequality operator ``!=``, there is also a strict inequality operator, ``!==``. The boolean expression ``a !== b`` returns ``true`` when the two operands are of different types, or if they are of the same type and have different values. 

.. tip:: USE ``===`` AND ``!==`` WHENEVER POSSIBLE. In this book we will use these strict operators over the loose operators from now on.

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

   #. There is no difference. They work exactly the same.
   #. Only ``===`` throws an error if its arguments are of different types.
   #. ``==`` converts values of different types to be the same type, while ``===`` does not.
   #. ``==`` works with all data types, while ``===`` does not.
