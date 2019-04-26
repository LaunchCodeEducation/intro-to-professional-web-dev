Breaking Down the **for** Statement
===================================

Having seen several examples, we will now explore the syntax of a ``for`` loop in more depth. 

Recall the first example of a ``for`` loop that we looked at.

.. sourcecode:: js

   for (let i = 0; i < 51; i++) {
      console.log(i);
   }

We broke down the flow of execution of this loop, noting that the loop executes once for each of the values of ``i`` from 0...50. The three components of the loop---loop variable, loop condition, and update expression---dictate exactly how this loop executes. So far, we have only seen ``for`` loops with this exact form:

.. sourcecode:: js

   for (let i = 0; i < upperBound; i++) {
      // loop body
   }   

However, the three components of a ``for`` loop statement can take different forms to create more complex looping behavior.

**for** Loop Anatomy
--------------------

The general form of a ``for`` loop is:

::

   for (initial expression; loop condition; update expression) {
      loop body
   }

Let's look at each of the three components that affect how this loop iterates.

Initial Expression
^^^^^^^^^^^^^^^^^^

.. index::
   single: for loop; initial expression
   single: for loop; variable

The **initial expression** is executed once, before any iterations of the loop. It can be any expression, even the **empty expression** (which contains no code). However, it almost always declares and initializes a variable, known as the **loop variable**.

The loop variable can be initialized to any value.

.. admonition:: Examples

   This loop prints 3...9.

   .. sourcecode:: js
   
      for (let i = 3; i < 10; i++) {
         console.log(i);
      }

   This loop prints each of the letters ``C``, ``o``, ``d``, and ``e`` on a separate line.

   .. sourcecode:: js
   
      let name = "LaunchCode";

      for (let i = 6; i < name.length; i++) {
         console.log(name[i]);
      }

To avoid confusion and bugs, you should give your loop variable a unique name, one that you have not used elsewhere in your program. In cases where the loop variable is serving as a "counter" for iterations of a loop, it is conventional to use ``i`` for the variable name. In the case of nested ``for`` loops (loops inside of loops), the variables ``j``, ``k``, etc. are often used.

.. note:: The loop variable is typically used by the loop body, but this is not required. The following example is a valid ``for`` loop that prints ``"LaunchCode"`` 42 times.

   .. sourcecode:: js
   
      for (let i = 0; i < 42; i++) {
         console.log("LaunchCode");
      }

Loop Condition
^^^^^^^^^^^^^^

.. index::
   single: for loop; condition

The **loop condition** is executed before each loop iteration. It is *always* a boolean expression, evaluating to ``true`` or ``false``. If the contion is true, the loop body executes. If the condition is false, loop execution stops and the program continues with the next line of code below the loop.

.. admonition:: Example

   This loop does not iterate at all, because its condition is false to start with.

   .. sourcecode:: js
   
      for (let i = 0; i < -1; i++) {
         console.log("LaunchCode");
      }

It is critical that the loop condition *eventually* becomes false. A loop for which the condition is never false is known as an **infinite loop**, because it never stops iterating. A program that contains an infinite loop will only stop after running out of memory or being manually stopped (for example, using control+c in a terminal). 

.. admonition:: Example

   This is an infinite loop, because its condition will always be true.

   .. sourcecode:: js
   
      for (let i = 0; i > -1; i++) {
         console.log("LaunchCode");
      }

You will accidentally write an infinite loop at some point; doing so is a right of passage for new programmers. When this happens, don't panic. Stop your program and figure out why your loop condition never became false. 

Update Expression
^^^^^^^^^^^^^^^^^

.. index::
   single: for loop; update expression

The final component in a for loop definition is the **update expression**, which executes after *every* iteration of the loop. While this expression may be anything, it most often updates the value of the loop variable. 

In all of the examples we have seen so far, the update expression has been ``i++``, incrementing the loop variable by 1. However, it can update the loop variable in other ways.

.. admonition:: Example

   This loop prints *even* integers from 0...50.

   .. sourcecode:: js
   
      for (let i = 0; i < 51; i = i + 2) {
         console.log(i);
      }

A bad choice of update expression can also cause an infinite loop.

.. admonition:: Example

   This loop repeates indefinitely, since ``i`` becomes smaller with each iteration and thus is never greater than or equal to 51.

   .. sourcecode:: js

      for (let i = 0; i < 51; i--) {
         console.log(i);
      }

Check Your Understanding
------------------------

Consider the program:

.. sourcecode:: js

   let phrase = "LaunchCode's LC101";

   for (let i = 0; i < phrase.length - 3; i = i + 3) {
      console.log(phrase[i]);
   }

.. admonition:: Question

   How many times does the loop body execute?

   #. 0
   #. 18
   #. 16
   #. 9

.. admonition:: Question

   Which set of characters is printed by the loop? (We have placed characters for the choices below on the same line, but they would be on separate lines in the actual program output.)

   #. LaunchCode's LC101
   #. LaunchCode's LC1
   #. LucCd' C
   #. LucCd' C0
