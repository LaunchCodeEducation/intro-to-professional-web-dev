Using Scope
===========

Scope allows programmers to control the flow of information through the
variables in their program. Some variables you want to set as constants (like
pi), which can be accessed globally. Others you want to keep secure to minimize
the danger of accidental updates. For example, a variable holding someone's
username should be kept secure.

Shadowing
---------

.. index:: ! variable shadowing, ! shadowing

**Variable shadowing** is where two variables in different scopes have the same
name. The variables can then be accessed under different contexts. However,
shadowing can affect the variable's accessibility. Not to mention, it also 
causes confusion for anyone reviewing the code.

.. admonition:: Example

   .. sourcecode:: JavaScript
      :linenos:

      const input = require('readline-sync');

      function hello(name) {
         console.log('Hello,', name);
         name = 'Ruth';
         return doubleName(name);
      }

      function doubleName(name){
         console.log(name+name);
         return name+name;
      }

      let name = input.question("Please enter your name: ");

      hello(name);
      doubleName(name);
      console.log(name);

   So, what is the value of ``name`` in line 4, 10, 16, 17, and 18?

Yikes! This is why shadowing is NOT a best practice in coding. Whenever
possible, use different global and local variable names.

.. admonition:: Try It!

   If you are curious about the ``name`` values in the example, feel free to
   run the code `here <https://repl.it/@launchcode/ShadowingExample>`__.

Variable Hoisting
-----------------

.. index:: ! variable hoisting

**Variable hoisting** is a behavior in JavaScript where variable declarations
are raised to the top of the current scope. This results in a program being able
to use a variable before it has been declared. Hoisting occurs when the ``var``
keyword is used in the declaration, but it does NOT occur when ``let`` and
``const`` are used in the declaration.

.. admonition:: Note

   Although we don't use the ``var`` keyword in this book, you will see it a
   lot in other JavaScript resources. Variable hoisting is an important concept
   to keep in mind as you work with JavaScript.

Check Your Understanding
------------------------

.. admonition:: Question

   What keyword allows a variable to be hoisted?

   a. ``let``
   b. ``var``
   c. ``const``

.. admonition:: Question

   Consider this code:

   .. sourcecode:: js
      :linenos:

      let a = 0;

      function myFunction() {
         let a = 10;
         return a;
      }

   Because there are two separate variables with the name, ``a``, under the two different scopes, ``a`` is being shadowed.

   a. True
   b. False
