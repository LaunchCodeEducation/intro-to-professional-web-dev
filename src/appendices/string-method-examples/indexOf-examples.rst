.. _string-indexof-examples:

**indexOf** Examples
====================

The general syntax for this method is:

.. sourcecode:: js

   stringName.indexOf(character);

Given a character (a string of length 1), this method returns the integer index of the *first* occurence of the character in the string. If the character does not occur in the string, -1 is returned.

.. admonition:: Example
   
   .. sourcecode:: js

      // returns 6
      "LaunchCode".indexOf("C");

      // returns -1
      "LaunchCode".indexOf("A");

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
