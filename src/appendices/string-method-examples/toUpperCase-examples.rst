.. _string-touppercase-examples:

``toUpperCase`` Examples
========================

The general syntax for this method is:

.. sourcecode:: js

   stringName.toUpperCase();

This method returns a copy of ``stringName`` with all lowercase letters replaced by their uppercase counterparts. It leaves non-alphabetic characters unchanged.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log("LaunchCode".toUpperCase());
      console.log("launchcode".toUpperCase());
      console.log("LaunchCode's LC101".toUpperCase());

   **Output**

   ::

      LAUNCHCODE
      LAUNCHCODE
      LAUNCHCODE'S LC101
