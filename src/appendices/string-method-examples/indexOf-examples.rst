.. _string-indexof-examples:

``indexOf`` Examples
====================

The general syntax for this method is:

.. sourcecode:: js

   stringName.indexOf(substr);

Given a candidate substring, this method returns the integer index of the *first* occurrence of the substring in the string. If the substring does not occur in the string, -1 is returned.

.. admonition:: Example
   
   .. sourcecode:: js
      :linenos:

      console.log("LaunchCode".indexOf("C"));

      console.log("LaunchCode".indexOf("A"));

      console.log("dogs and dogs and dogs!".indexOf("dog"));

   **Output**

   ::

      6
      -1
      0

.. admonition:: Example

   An email address must contain an ``@`` symbol. Checking for the presence of this symbol is a part of email address verification in most programs.

   .. sourcecode:: js
      :linenos:
   
      let input = "fake.email@launchcode.org";
      let atIndex = input.indexOf("@");
      
      if (atIndex > -1) {
         console.log("Email contains @");
      } else {
         console.log("Invalid email");
      }

   **Output**

   .. sourcecode:: bash

      Email contains @   
