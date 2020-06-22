Conditionals
============

.. index:: ! conditional

At the beginning of this chapter, we decided that we wanted to be able to write code that only executes when a given condition is ``true``.

Again, here is our motivating example:

.. admonition:: Example

   Consider a banking application that can remind you when a bill is due. The application will notify you that a bill is due soon, but *only if* the bill has not already been paid.

We summarized the condition as follows: Send a notification of an upcoming bill if the statement "the bill is unpaid" is true.

In such a program, JavaScript uses booleans to represent the conditional "the bill is unpaid". Based on the truth of this statement, the program executes or skips the code for notifying the user.

The JavaScript construct that enables such behavior is a **conditional**.

``if`` Statements
-----------------

.. index:: ! if, code block

The most basic form of a conditional is an **if statement**. Here's how to create one in JavaScript:

.. figure:: figures/if.png
   :height: 400px
   :alt: The structure of a conditional with an if statement

Let's look at each component of this new syntax.

- The ``if`` statement consists of a header line and a body. The header line begins with the keyword ``if`` followed by a boolean expression enclosed in parentheses.
- ``condition`` is a boolean expression (an expression that evaluates to either ``true`` or ``false``).
- The statements that follow the condition, within ``{ }``, make up a **code block**. The code within the brackets ``{ }`` will be executed if the condition evaluates to true. If the condition evaluates to false, the code within the brackets is ignored.

Here is an explicit example that mimics our banking program.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let billHasBeenPaid = false;

      if (!billHasBeenPaid) {
         console.log("Your bill is due soon!");
      }

   **Console Output**

   ::

      Your bill is due soon!

The message prints because ``billHasBeenPaid`` is ``false``, so
``!billHasBeenPaid`` evaluates to ``true``. If we were to change the value of
``billHasBeenPaid`` to be ``true``, then ``!billHasBeenPaid`` would evaluate to
``false`` and the code block would *not* execute.

The condition in an ``if`` statement can be any boolean expression, such as ``name === 'Jack'`` or ``points > 10`` (here, ``name`` and ``points`` are variables). Additionally, the code block associated with a conditional can be of any size. This conditional has a code block with two lines of code:

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      if (num % 2 === 0 && num > 3) {
         console.log(num, "is even");
         console.log(num, "is greater than 3");
      }

While not required, the code within a conditional code block is typically indented to make it more readable. Similarly, it is a common convention to place the opening ``{`` at the end of the first line, and the closing ``}`` on a line of its own following the last line of the code block.

You should follow such conventions, even though ignoring them will not create an error. To see why, compare the readability of this example, which is functionally equivalent to the one above.

.. sourcecode:: js
   :linenos:

   if (num % 2 === 0 && num > 3)
   { console.log(num, "is even");
    console.log(num, "is greater than 3"); }

Aside from being more aesthetically pleasing, the first version also makes it
easier to visually identify the pair of matching curly brackets, which helps
prevent syntax errors.

.. admonition:: Warning

   If the code block associated with a conditional consists of only one
   line, then the enclosing curly brackets can be omitted.

   However, this is NOT a best-practice, as it makes the logic harder to
   follow.

   .. sourcecode:: js
      :linenos:

      if (!billHasBeenPaid)
         console.log("Your bill is due soon!");

   We will use curly brackets for ALL conditional code blocks, and encourage
   you to do so as well, at least until you become comfortable with reading and
   writing more complex JavaScript.

``else`` Clauses
----------------

.. index:: conditional, ! else, ! if-else, branching

An **else clause** can be paired with an ``if`` statement to specify code that should be executed when the condition is false.

.. figure:: figures/if-else.png
   :height: 400px
   :alt: A conditional with an else clause

We can use an ``else`` clause within our bank app to send a message if no bills are currently due.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let billHasBeenPaid = true;

      if (!billHasBeenPaid) {
         console.log("Your bill is due soon!");
      } else {
         console.log("Your payments are up to date.");
      }

   **Console Output**

   ::

      Your payments are up to date.

This structure is known as an **if-else statement**, and it provides a
mechanism for **branching**. The flow of the program can take one of two paths
when it reaches a conditional, depending on whether the condition is ``true``
or ``false``.

.. figure:: figures/conditional-flow.png
   :height: 500px
   :alt: A diagram showing how the flow of a program branches based on the value of the condition in an if-else statement. If the condition is true, one code block executes. If the condition is false, a different code block executes.


``else if`` Statements
----------------------

.. index:: conditional, ! else if

If-else statements allow us to construct two alternative paths. A single condition determines which path will be followed. We can build more complex conditionals using an ``else if`` clause. These allow us to add additional conditions and code blocks, which facilitate more complex branching.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let x = 10;
      let y = 20;

      if (x > y) {
         console.log("x is greater than y");
      } else if (x < y) {
         console.log("x is less than y");
      } else {
         console.log("x and y are equal");
      }

   **Console Output**

   ::

      x is less than y

Let's summarize the flow of execution of this conditional:

#. Line 4 begins the conditional. The boolean expression ``x > y`` evaluates to ``false``, since 10 is not greater than 20. This causes line 5 to be skipped.
#. Line 6 contains an else-if statement. The boolean expression ``x < y`` evaluates to ``true``, since 10 is less than 20. This triggers the execution of line 7.
#. The code block associated with the ``else`` clause on lines 8-10 is skipped, because one of the conditions above was true.

As with a simple ``if`` statement, the ``else`` clause is optional in this context as well. The following example does not print anything, since both conditions evaluate to false and there is no ``else`` clause.

.. sourcecode:: js
   :linenos:

   let x = 10;
   let y = 10;

   if (x > y) {
       console.log("x is greater than y");
   } else if (x < y) {
       console.log("x is less than y");
   }

We can construct conditionals using ``if``, ``else if``, and ``else`` with a lot of flexibility. The only rules are:

#. We may not use ``else`` or ``else if`` without a preceding ``if`` statement.
#. ``else`` and ``else if`` clauses are optional.
#. Multiple ``else if`` statements may follow the ``if`` statement, but they must precede the ``else`` clause, if one is present.
#. Only one ``else`` clause may be used.

Regardless of the complexity of a conditional, *no more than one* of the code blocks will be executed.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let x = 10;
      let y = 20;

      if (x > y) {
         console.log("x is greater than y");
      } else if (x < y) {
         console.log("x is less than y");
      } else if (x % 5 === 0) {
         console.log("x is divisible by 5");
      } else if (x % 2 === 0) {
         console.log("x is even");
      }

   **Console Output**

   ::

      x is less than y

Even though both of the conditions ``x % 5 === 0`` and ``x % 2 === 0`` evaluate to ``true``, neither of the associated code blocks is executed. When a condition is satisfied, the rest of the conditional is skipped.

Check Your Understanding
------------------------

.. admonition:: Question

   What does the following code print?

   .. sourcecode:: js
      :linenos:

      let a = 7;
      if (a % 2 === 1) {
         console.log("Launch");
      } else if (a > 5) {
         console.log("Code");
      } else {
         console.log("LaunchCode");
      }

   #. ``"Launch"``
   #. ``"Code"``
   #. ``"Launch"``

      ``"Code"``
   #. ``"LaunchCode"``
