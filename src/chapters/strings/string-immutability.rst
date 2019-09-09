String Immutability
===================

.. index::
   pair: string; immutable

If an object cannot be changed, we say that it is **immutable**. Strings are
immutable, which means we cannot change the individual characters within a
given string. While we can access individual characters using bracket
notation, attempting to change individual characters simply does not work.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let nonprofit = "Launchcode";

      console.log(nonprofit);
      nonprofit[6] = "C";
      console.log(nonprofit);

   **Console Output**

   ::

      Launchcode
      Launchcode

We attempted to change the value of the character at index 6 from ``'c'`` to ``'C'``, by using an assignment statement along with bracket notation on line 4 (perhaps to align with official LaunchCode branding guidelines). However, this change clearly did not take place. In many programming languages strings are immutable, and while trying to change a string in some languages results in an error, JavaScript simply ignores our request to alter a string.

It is important to notice that immutability applies to string *values* and not string variables.

.. admonition:: Example

   We can set a variable containing a string to a different value.

   .. sourcecode:: js
      :linenos:

      let nonprofit = "Launchcode";
      nonprofit = "LaunchCode";

      console.log(nonprofit);

   **Console Output**

   ::

      LaunchCode

In this example, the change made on line 2 is carried out. The difference between this example and the one above is that here we are modifying the value that the variable is storing, and not the string itself. Using our visual analogy of a variable as a label that "points at" a value, the second example has the following effect:

.. figure:: figures/string-var-reassignment.png
   :alt: A variable, nonprofit, pointing at "LaunchCode" with a lowercase-c.
   :height: 300px

   When the value of a variable storing a string is changed, the variable then points to a new value, with the old value remaining unchanged.

Check Your Understanding
------------------------

.. admonition:: Question

   Given ``pet = 'cat'``, why do the statements ``console.log(pet + 's');`` and ``pet += 's';`` NOT violate the immutability of strings?
