.. _string-indexof-examples:

**indexOf** Examples
====================

The general syntax for this method is:

.. sourcecode:: js

   stringName.indexOf(substr);

Given a candidate substring, this method returns the integer index of the *first* occurence of the subtring in the string. If the substring does not occur in the string, -1 is returned.

.. admonition:: Example
   
   .. sourcecode:: js

      // returns 6
      "LaunchCode".indexOf("C");

      // returns -1
      "LaunchCode".indexOf("A");

      // returns 0
      "dogs and dogs and dogs!".indexOf("dog");

.. admonition:: Example

   An email address must contain an ``@`` symbol. Checking for the presence of this symbol is a part of email address verification in most programs.

   .. sourcecode:: js
   
      let input = "fake.email@launchcode.org";
      let atIndex = input.indexOf("@");
      
      if (atIndex > -1) {
         console.log("Email contains @");
      } else {
         console.log("Invalid email");
      }

   **Output**

   ::

      Email contains @   
