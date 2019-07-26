Choosing Which Loop to Use
==========================

.. index::
   single: iteration; definite
   single: iteration; indefinite

The ``for`` loop is typically used to iterate through a fixed set of values that can be determined before the loop executes. This is why we say that a ``for`` loop exhibits **definite iteration**.

On the other hand, the ``while`` loop is more flexible, as we saw with the example of validating user input. In that case, we could not determine in advance how many times the loop would iterate; it depended entirely on the values provided by the user during program execution. For this reason, a ``while`` loop is often described as **indefinite iteration**. We expect that *eventually* the condition controlling the iteration will evaluate to ``false`` and the iteration will stop. (Unless we have an infinite loop, which is a problem we want to avoid.)

While we saw that any ``for`` loop can be written as a ``while`` loop by manually creating and updating a loop variable, it is preferable to use a ``for`` loop when iterating over a collection or iterating a fixed number of times. Manually updating the variable in a ``while`` loop is more work for you, the programmer, and can lead to infinite loops if not handled properly.

Check Your Understanding
------------------------

.. admonition:: Question

   You are asked to program a robot to move tennis balls from one box (Box #1) to another (Box #2), one-by-one. The robot should continue moving balls until Box #1 is empty, and balls may be added to the box after the robot begins its work.

   Which type of loop should you use to write the program?

   #. ``while`` loop
   #. ``for`` loop

.. admonition:: Question

   You are asked to write a program similar to the one above, with the modification that a user may give the robot a specific number of balls to move from Box #1 to Box #2. (You can assume there will always be more balls than the user has asked the robot to move.)

   Which type of loop should you use to write the program?

   #. ``while`` loop
   #. ``for`` loop
