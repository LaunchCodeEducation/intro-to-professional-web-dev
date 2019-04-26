.. _string-trim-examples:

**trim** Examples
=================

The general syntax for this method is:

.. sourcecode:: js

   stringName.trim();

.. index::
   single: whitespace; leading
   single: whitespace; trailing

This method returns a copy of the string with any leading or trailing whitespace removed. **Leading whitespace** consists of all whitespace characters---such as spaces or tabs---appearing *before* the first non-whitespace character. **Trailing whitespace** consists of all whitespace characters appearing *after* the last non-whitespace character.

.. admonition:: Example

   
   .. sourcecode:: js

      // returns "Saint Louis"
      "Saint Louis ".trim();

      // returns "Saint Louis"
      " Saint Louis".trim();

      // returns "Saint Louis"
      " Saint Louis ".trim();

.. admonition:: Example

   When typing an email address into a web site, a user may inadvertently type a space before and/or after the email address. We can clean up such input using the ``trim`` method.

   This example cleans up user input with ``trim``.

   .. sourcecode:: js
   
      let input = " fake.email@launchcode.org ";
      let email = input.trim();
      console.log(email);

   **Output**

   ::

      fake.email@launchcode.org
