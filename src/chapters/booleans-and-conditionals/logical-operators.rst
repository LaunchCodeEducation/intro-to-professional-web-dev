Logical Operators
=================

.. index:: operators

Recall that an operator is one or more characters that carries out an action on
its operand(s). In :ref:`data-and-variables` we learned about three types of
operators:

- Arithmetic operators, such as ``+``, ``-``, ``*``, ``/``, and ``%``.
- The string operator ``+``.
- Compound assignment operators, such as ``+=`` and ``-=``.

Arithmetic and string operators take number and string operands, respectively,
returning values of the same type. Compound assignment operators work similarly
with numbers or strings while also reassigning the value of the first,
variable operand.

Boolean Operators
-----------------

.. index::
   single: operator; comparison
   single: operator; boolean

In addition to these operators, we learned about comparison operators like
``===``, ``<``, and others. These operators are part of a larger class known as
**boolean operators**, so-called because they return a boolean value (``true``
or ``false``).

Three additional boolean operators allow us to create more complex expressions.
These are described below.

Logical AND
^^^^^^^^^^^

.. index:: ! &&

.. index::
   single: operator; boolean
   single: boolean; expression, compound

A **compound boolean expression** is a boolean expression built out of smaller
boolean expressions. JavaScript allows us to create a compound boolean
expression using the logical AND operator, ``&&``.

The operator takes two operands, and the resulting expression is ``true`` if
*both* operands are ``true`` individually. If either operand is ``false``, the
overall expression is ``false``.

.. admonition:: Example

   In English, the ``&&`` operator mirrors the use of the word "and" (hence the
   name "logical AND"). A sentence like "Roses are red and violets are blue,"
   is true as a whole precisely because roses are actually red, and violets are
   actually blue.

   On the other hand, the sentence "Roses are red and violets are green," is
   false as a whole. While roses are indeed red, violets are not green.

Let's see how this works in code.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(7 > 5 && 5 > 3);
      console.log(7 > 5 && 2 > 3);
      console.log(2 > 3 && 'dog' === 'cat');

   **Console Output**

   ::

      true
      false
      false

In line 1, ``7 > 5 && 5 > 3`` evaluates to ``true`` because both ``7 > 5`` and
``5 > 3`` are ``true`` individually.

The expression ``7 > 5 && 2 > 3`` evaluates to ``false`` because one of the two
expressions, ``2 > 3``, is ``false``.

Like line 2, line 3 returns ``false`` because both sub-expressions are
``false``. Notice that we can mix and match data types however we like, as long
as both sides of the ``&&`` expression are themselves boolean expressions.

Logical OR
^^^^^^^^^^

.. index:: ! ||

.. index::
   single: operator; boolean

JavaScript's logical OR operator, ``||``, also creates compound boolean
expressions. This operator takes two operands, and the resulting expression is
``true`` if *either* of the operands are ``true`` individually. If both
operands are ``false``, the overall expression is ``false``.

.. admonition:: Example

   As with logical AND, logical OR mirrors our experience of English language
   truth values. The sentence "Pigs can fly or dogs can run," is true as a
   whole. Joining the two clauses by "or" requires that only one of them is
   true in order for the full sentence to be true.

   When both of the clauses joined by "or" are false, the statement as a whole is false. For example, "Pigs can fly or dogs can speak Spanish," is a false statement.

Let's look at some examples in JavaScript.

.. sourcecode:: js
   :linenos:

   console.log(7 > 5 || 5 > 3);
   console.log(7 > 5 || 2 > 3);
   console.log(2 > 3 || 'dog' === 'cat');

**Console Output**

::

   true
   true
   false

Lines 1 and 2 both return ``true`` because at least one of the comparison expressions joined by ``||`` is ``true``. Line 3 returns ``false`` because both sub-expressions are ``false``.

.. admonition:: Warning

   The single symbols ``&`` and ``|`` are themselves valid JavaScript operators,
   so accidentally leaving off one symbols when typing ``&&`` or ``||`` will not
   result in an error message.

   The operators ``&`` and ``|`` are `bitwise operators <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators>`__,
   which are beyond the scope of this course.

   Most programmers rarely use ``&`` and ``|``, and it is not important for you
   to understand them at this point. However, you should *never* use them in
   place of ``&&`` and ``||``.

Logical NOT
^^^^^^^^^^^

.. index:: ! !

.. index::
   single: operator; boolean

The logical NOT operator, ``!``, takes only a single operand and reverses its boolean value.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(! true);
      console.log(! false);

   **Console Output**

   ::

      false
      true

The operator ``!`` (sometimes called "bang") has the same semantic role as the word "not" in English.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log( !(5 > 7) );
      console.log( !('dog' === 'cat') );

   **Console Output**

   ::

      true
      true

Operator Precedence
-------------------

.. index::
   single: operator; precedence

We now have a number of operators in our toolkit. It is important to understand how these operators relate to each other with respect to **operator precedence**. Operator precedence is the set of rules that dictate in which order the operators are applied.

JavaScript will always apply the logical NOT operator, ``!``, first. Next, it applies the arithmetic operators, followed by the comparison operators. The logical AND and OR are applied last.

This means that the expression ``x * 5 >= 10 && y - 6 <= 20`` will be evaluated so as to first perform the arithmetic and then check the relationships. The ``&&`` evaluation will be done last. The order of evaluation is the same as if we were to use parentheses to group, as follows:

.. sourcecode:: js

   ((x * 5) >= 10) && ((y - 6) <= 20)

While parentheses are not always necessary due to default operator precedence,
they make expressions much more readable. As a best practice, we encourage you
to use them, especially for more complicated expressions.

The following table lists operators in order of precedence, from highest (applied first) to lowest (applied last). A complete table for the entire language can be found in the `MDN JavaScript Documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#Table>`_.

.. list-table:: Operator Precedence
   :widths: auto
   :header-rows: 1

   * - Precedence
     - Category
     - Operators
   * - (highest)
     - Logical NOT
     - ``!``
   * -
     - Exponentiation
     - ``**``
   * -
     - Multiplication and division
     - ``*``, ``/``, ``%``
   * -
     - Addition and subtraction
     - ``+``, ``-``
   * -
     - Comparison
     - ``<=``, ``>=``, ``>``, ``<``
   * -
     - Equality
     - ``===``, ``!==``, ``==``, ``!=``
   * -
     - Logical AND
     - ``&&``
   * - (lowest)
     - Logical OR
     - ``||``

Truth Tables
------------

.. index:: ! truth table

**Truth tables** help us understand how logical operators work by calculating all of the possible return values of a boolean expression. Let's look at the truth table for ``&&``, which assumes we have two boolean expressions, A and B, joined by ``&&``.

.. admonition:: Example

   .. list-table:: Truth Table for ``&&``
      :widths: auto
      :header-rows: 1

      * - A
        - B
        - A ``&&`` B
      * - ``true``
        - ``true``
        - ``true``
      * - ``true``
        - ``false``
        - ``false``
      * - ``false``
        - ``true``
        - ``false``
      * - ``false``
        - ``false``
        - ``false``

Consider the first row of the truth table. This row states that if A is true and B is true, then A && B is true. This is a fact, regardless of what boolean expressions A and B might actually be. The two middle rows demonstrate that if either A or B is false, then A && B is false. (If this idea is hard to grasp, try substituting actual expressions for A and B.)

Check Your Understanding
------------------------

.. admonition:: Question

   Complete the table below.

   .. list-table:: Truth Table for ``||``
      :widths: auto
      :header-rows: 1

      * - A
        - B
        - A ``||`` B
      * - ``true``
        - ``true``
        -
      * - ``true``
        - ``false``
        -
      * - ``false``
        - ``true``
        -
      * - ``false``
        - ``false``
        -

.. admonition:: Question

   Which of the following properly expresses the order of operations (using parentheses) in the following expression?

   .. sourcecode:: js

      5*3 > 10 && 4 + 6 === 11

   #. ``((5*3) > 10) && ((4+6) === 11)``
   #. ``(5*(3 > 10)) && (4 + (6 === 11))``
   #. ``((((5*3) > 10) && 4)+6) === 11``
   #. ``((5*3) > (10 && (4+6))) === 11``

.. admonition:: Question

   What is returned by the following boolean expression?

   .. sourcecode:: js

      4 < 3 || 2 < 3

   #. ``true``
   #. ``false``
   #. ``"true"``
   #. ``"false"``
