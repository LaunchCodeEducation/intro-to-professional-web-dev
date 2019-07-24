.. _string-tolowercase-examples:

``toLowerCase`` Examples
========================

The general syntax for this method is:

.. sourcecode:: js

   stringName.toLowerCase();

This method returns a copy of ``stringName`` with all uppercase letters
replaced by their lowercase counterparts. It leaves non-alphabetic characters
unchanged.

.. sourcecode:: js

   "LaunchCode".toLowerCase();

**Output**

.. sourcecode:: bash

   launchcode

.. admonition:: Example

   The domain portion of an email address (the portion after the ``@`` symbol) is case-insensitive. Emails with domain ``launchcode.org`` are the same as those with domain ``LAUNCHCODE.ORG``. By convention, the all-lowercase version is typically used by an application.

   This program standardizes an email address by converting it to all lowercase characters.

   .. sourcecode:: js

      let input = "fake.email@LAUNCHCODE.ORG";
      let email = input.toLowerCase();
      console.log(email);

   **Output**

   .. sourcecode:: bash

      fake.email@launchcode.org

.. admonition:: Warning

   This example is a bit crude, since the portion of an email address *before*
   the ``@`` symbol is allowed to be case-sensitive. When standardizing the
   case of an email in a real application, we would want to be more precise and
   only convert the domain portion to lowercase characters.
