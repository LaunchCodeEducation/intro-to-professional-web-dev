.. _string-touppercase-examples:

**toUpperCase** Examples
========================

The general syntax for this method is:

.. sourcecode:: js

   stringName.toUpperCase();

This method returns a copy of ``stringName`` with all lowercase letters replaced by their uppercase counterparts. It leaves non-alphabetic characters unchanged.

.. admonition:: Example

   .. sourcecode:: js
         
      // returns "LAUNCHCODE"
      "LaunchCode".toUpperCase();

      // returns "LAUNCHCODE"
      "launchcode".toUpperCase();

      // returns "LAUNCHCODE'S LC101"
      "LaunchCode's LC101".toUpperCase();
