Nested Conditionals
===================

We can write code with more complex branching behavior by combining
conditionals and, in particular, by nesting conditionals. Let's see how this
works by tackling the following problem.

.. admonition:: Example

    Write code that prints different messages based on the value of a number variable. If the number is odd, print nothing. If it is even, print "EVEN". If it is also positive print "POSITIVE".

Our first attempt at a solution might look like this:

.. sourcecode:: js
   :linenos:

   let num = 7;

   if (num % 2 === 0) {
      console.log("EVEN");
   }

   if (num > 0) {
      console.log("POSITIVE");
   }

**Console Output**

::

   POSITIVE

We find that the output is ``POSITIVE``, even though 7 is odd and so nothing
should be printed. This code doesn't work as desired because we only want to
test for positivity when we already know that the number is even. We can
enable this behavior by putting the second conditional *inside* the first.

.. replit:: js
   :linenos:
   :slug: Positive-and-Even

   let num = 7;

   if (num % 2 === 0) {
       console.log("EVEN");

       if (num > 0) {
           console.log("POSITIVE");
       }
   }

.. admonition:: Try It!

   Run the previous example with several different values for ``num`` (even,
   odd, positive, negative) to ensure it works as desired. Nice, huh?

Notice that when we put one conditional inside another, the body of the nested
conditional is indented by two tabs rather than one. This convention provides
an easy, visual way to determine which code is part of which conditional.

Check Your Understanding
------------------------

.. admonition:: Question

   What is printed when the following code runs?

   .. sourcecode:: js
      :linenos:

      let num = 7;

      if (num % 2 === 0) {
          if (num % 2 === 1) {
              console.log("odd");
          }
      }

   #. The code won't run due to invalid syntax
   #. ``odd``
   #. ``even``
   #. The code runs but doesn't print anything


.. admonition:: Question

   Considering the same conditional used in the previous question, which values of ``num`` would result in ``"odd"`` being printed?

   .. sourcecode:: js
      :linenos:

      if (num % 2 === 0) {
          if (num % 2 === 1) {
              console.log("odd");
          }
      }

   #. Even values of ``num``.
   #. Odd values of ``num``.
   #. No values. It is impossible for the call to ``console.log`` to ever run, given the two conditions.
   #. ``num`` is 0.
