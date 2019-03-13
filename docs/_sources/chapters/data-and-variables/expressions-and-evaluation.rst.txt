Expressions and Evaluation
==========================

.. index:: ! expression

An **expression** is a combination of values, variables, operators, and calls to functions. An expression can be thought of as a a formula that is made up of multiple pieces. 

.. index::
   pair: expression; evaluation
   pair: expression; return value

.. index:: ! returns

The *evaluation* of an expression produces a value, known as the **return value**. We say that, "an expression **returns** a value."

Expressions need to be evaluated when the code executes in order to determine the return value, or specific piece of data that should be used. Evaluation is the process of computing the return value.

If you ask JavaScript to *print* an expression using ``console.log()``, the interpreter **evaluates** the expression and displays the result.

.. sourcecode:: js

    console.log(1 + 1);

This code prints not ``1 + 1`` but rather the *result* of calculating ``1 + 1`` mathemtically. In other words, ``console.log(1 + 1)`` prints the value ``2``. This is what we would expect.

Since evaluating an expression produces a value, expressions can appear on the right-hand side of assignment statements. 

.. sourcecode:: js
   :linenos:

   let sum = 1 + 2;
   console.log(sum);

The value of the variable ``sum`` is the result of evaluating the expression ``1 + 2``, so the value ``3`` is printed.

A value all by itself is a simple expression, and so is a variable. Evaluating a variable gives the value that the variable refers to. This means that line 2 of the example above also contains the simple expression ``sum``.
