Choosing Which Loop to Use
==========================

.. index::
   single: iteration; definite
   single: iteration; indefinite

The ``for`` loop is typically used to iterate through a fixed set of values that can be determined before the loop executes. This is why it is often said that a ``for`` loop exhibits **definite iteration**.

On the other hand, the ``while`` loop is more flexible, as we saw with the example of validating user input. In that case, we could not determine in advance how many times the loop would iterate; it depended entirely on the values provided by the user during program execution. For this reason, a ``while`` loop is often described as **indefinite iteration**. We expect that *eventually* the condition controlling the iteration will evaluate to ``false`` and the iteration will stop. (Unless we have an infinite loop, which is a problem we want to avoid.)

While we saw that any ``for`` loop can be written as a ``while`` loop, by manually creating and updating a loop variable, it is preferable to use a ``for`` loop when iterating over a collection or iterating a fixed number of times. Manually updating the loop variable in a ``while`` loop is more work for you, the programmer, and can lead to infinite loops if not handled properly.

Check Your Understanding
------------------------

.. admonition:: Question

   You want to write a program that will run until January 1, 2050, redgardless of when it is started. Which loop should you use?

   #. ``while`` loop
   #. ``for`` loop
