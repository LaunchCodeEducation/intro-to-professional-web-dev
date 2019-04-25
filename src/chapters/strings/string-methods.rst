.. _string-methods:

String Methods
==============

JavaScript provides many useful methods for string objects. Recall that a method is a function that "belongs to" a specific object. Methods will typically result in some operation being carried out on the data within an object. For strings, this means that our methods will typically transform the characters of the given string in some way.

As we have learned, strings are immutable. Therefore, string methods will not change the value of a string itself, but instead will *return* a new string that is the result of the given operation.

We saw this behavior in our first example of a string method, at the beginning of this chapter.

.. admonition:: Example

   .. sourcecode:: js
   
      let nonprofit = "LaunchCode";

      console.log(nonprofit.toLowerCase());
      console.log(nonprofit);

   **Output**

   ::

      launchcode
      LaunchCode

While ``nonprofit.toLowerCase()`` evaluated to ``"launchcode"``, the value of ``nonprofit`` was left unchanged. This will be case for each of the string methods.


Common Methods
--------------

.. index::
   single: string; methods

Here we present the most commonly-used string methods. There are `other string methods documentated at MDN <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#Methods_2>`_.

.. list-table:: Common String Methods
   :header-rows: 1

   * - Method
     - Description
     - Example
   * - ``indexOf``
     - Given a character, returns the integer index of the first occurence of the character in the string. If the character does not occur in the string, -1 is returned.
     - 
         .. sourcecode:: js
         
            // returns 6
            "LaunchCode".indexOf("C");

            // returns -1
            "LaunchCode".indexOf("A");

   * - ``charAt``
     - Given an index, returns the character at the given index. If the index is out of range, the empty string is returned.
     - 
         .. sourcecode:: js
         
            // returns "n"
            "LaunchCode".charAt(3);

            // returns ""
            "LaunchCode".charAt(37);

   * - ``toLowerCase``
     - Returns a copy of the given string, with all uppercase letters converted to lowercase.
     - 
         .. sourcecode:: js
         
            // returns "launchcode"
            "LaunchCode".toLowerCase();

   * - ``toUpperCase``
     - Returns a copy of the given string, with all lowercase letters converted to uppercase.
     - 
         .. sourcecode:: js
         
            // returns "LAUNCHCODE"
            "LaunchCode".toUpperCase();
            
   * - ``trim``
     - Returns a copy of the given string with a leading and trailing whitespace removed.
     - 
         .. sourcecode:: js

            // returns "The LaunchCode Foundation"
            "  The LaunchCode Foundation     ".trim();

   * - ``replace``
     - Given a search string ``s`` and a replacement value ``r``, ``str.replace(s, r)`` returns a copy of ``str`` with the first occurence of ``s`` replaced by ``r``. *Note:* The ``replace`` method can be used in more powerful ways utilizing regular expressions. We will not cover those here, but you can `read more at MDN <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace>`_.
     - 
         .. sourcecode:: js
         
            // returns "cat"
            "car".replace("r", "t");

            // returns "LaunchCode"
            "Launch Code".replace(" ", "");

   * - ``slice``
     - Given a starting index ``i`` and an optional ending index ``j``, return the substring consisting of characters from index ``i`` through index ``j-1``. If the ending index is ommitted, the returned substring includes all characters from the starting index through the end of the string. 
     - 
         .. sourcecode:: js

            // returns "Launch"
            "LaunchCode".slice(0, 6);
         
            // returns "Code"
            "LaunchCode".slice(6);

Examples
--------

To illustrate how string methods can be used, we will look at various validation checks that could be used when working with email addresses.

In each example, we will manually initialize a variable named ``input`` for ease of illustration. In a real program, the value of this variable would come from user input.

**trim**
^^^^^^^^

When typing an email address into a web site, a user may inadvertently type a space before and/or after the email address. We can clean up such input using the ``trim`` method.

.. admonition:: Example

   Cleaning up user input with ``trim``.

   .. sourcecode:: js
   
      let input = " fake.email@launchcode.org ";
      let email = input.trim();
      console.log(email);

   **Output**

   ::

      fake.email@launchcode.org
   

**toLowerCase**
^^^^^^^^^^^^^^^

The domain portion of an email address (the portion after the ``@`` symbol) is case-insensitive. Emails with domain ``launchcode.org`` are the same as those with domain ``LAUNCHCODE.ORG``. By convention, the all-lowercase version is typically used by an application.

.. admonition:: Example

   Standardizing an email address by converting to all lowercase characters.

   .. sourcecode:: js
   
      let input = "fake.email@LAUNCHCODE.ORG";
      let email = input.toLowerCase();
      console.log(email);

   **Output**

   ::

      fake.email@launchcode.org

.. warning:: This example is a bit crude, since the portion of an email address *before* the ``@`` symbol can be case-sensitive. If standardizing the case of an email in a real application, we would want to be more precise and only convert the domain portion to lowercase characters.

**indexOf**
^^^^^^^^^^^

An email address must contain an ``@`` symbol. Checking for the presence of this symbol is a part of email address verification in most programs.

.. admonition:: Example

   Checking for the symbol ``@``.

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

**replace**
^^^^^^^^^^^

Some email providers, including Gmail, allow users to put a ``.`` anywhere before the ``@`` symbol. This means that ``fake.email@launchcode.org`` is the same as ``fakeemail@launchcode.org``.

.. admonition:: Example

   Remove the ``.`` before the ``@`` symbol in an email address.

   .. sourcecode:: js
   
      let input = " fake.email@launchcode.org ";
      let email = input.replace(".", "");
      console.log(email);

   **Output**

   ::

      fakeemail@launchcode.org

This example illustrates a common use case of ``replace``, which is to *remove* a character by replacing it with the empty string.

.. warning:: Notice in this example that if there is not a ``.`` before the ``@`` symbol, the ``.`` that is part of the domain, ``launchcode.org`` would be inadvertently removed. In a real application, we would want to isolate the portion in front of ``@`` using ``slice``.

**slice**
^^^^^^^^^

On some websites, the portion of an email address before the ``@`` symbol is used as a username. We can extract this portion of an email address using ``slice`` in conjunction with ``indexOf``.

.. admonition:: Example

   .. sourcecode:: js
   
      let input = "fake.email@launchcode.org";
      let atIndex = input.indexOf("@");
      let username = input.slice(0, atIndex);
      console.log(username);

   **Output**

   ::

      fake.email

.. tip:: String methods can be combined in a process called **method chaining**. Given ``word = 'JavaScript';``, word.toUpperCase() returns ``JAVASCRIPT``. What would ``word.slice(4).toUpperCase()`` return?  TRY IT!  (`Repl.it <https://repl.it/@launchcode/Intro-To-Method-Chaining>`_).


Check Your Understanding
------------------------

.. admonition:: Question

   What is printed by the following code?

   .. sourcecode:: javascript

      let language = "JavaScript";
      language.replace('J', 'Q');
      language.slice(0,5);
      console.log(language);

   #. ``"JavaScript"``
   #. ``"QavaScript"``
   #. ``"QavaSc"``
   #. ``"QavaS"``

.. admonition:: Question

   Given ``language = 'JavaScript';``, what does ``language.slice(1,6)`` return?

   #. ``"avaScr"``
   #. ``"JavaSc"``
   #. ``"avaSc"``
   #. ``"JavaS"``
