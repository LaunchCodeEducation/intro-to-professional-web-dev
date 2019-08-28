.. _string-trim-examples:

``trim`` Examples
=================

The general syntax for this method is:

.. sourcecode:: js

   stringName.trim();

.. index::
   single: whitespace; leading
   single: whitespace; trailing

This method returns a copy of the string with any leading or trailing
whitespace removed. Whitespace characters are those that do not display
anything on the screen, such as spaces and tabs.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log("Saint Louis ".trim());
      console.log(" Saint Louis".trim());
      console.log(" Saint Louis ".trim());

   **Output**

   .. sourcecode:: bash

      Saint Louis
      Saint Louis
      Saint Louis


.. admonition:: Example

   When typing an email address into a web site, a user may inadvertently type a space before and/or after the email address. We can clean up such input using the ``trim`` method.

   This example cleans up user input with ``trim``.

   .. sourcecode:: js

      let input = " fake.email@launchcode.org ";
      let email = input.trim();
      console.log(email);

   **Output**

   .. sourcecode:: bash

      fake.email@launchcode.org
