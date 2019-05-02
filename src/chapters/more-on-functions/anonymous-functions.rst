Anonymous Functions
===================

.. index::
   single: function, named
   single: function, anonymous

The syntax :ref:`initially introduced <function-syntax>` for writing functions was this:

.. sourcecode:: js

   function myFunction(parameter1, parameter2,..., parameterN) {

      // function body

   }

A function defined in this way is a **named function**, so-called because it has a name (``myFunction`` in the example above).  

Many programming languages, including JavaScript, also us to create **anonymous functions**, which *do not* have names. We can create an anonymous function by leaving off the function name when defining it:

.. sourcecode:: js

   function (parameter1, parameter2,..., parameterN) {

      // function body

   }

You might be asking yourself, *How can I call such a function if it doesn't have a name?!* Good question. Let's address that now.

Anonymous Function Variables
----------------------------

Anonymous functions are often assigned to variables when they are created, which allows them to be called using the variable's name.

.. admonition:: Example

   Let's create and use a simple anonymous function that returns the sum of two numbers.

   .. sourcecode:: js
      :linenos:
   
      let add = function(a, b) {
         return a + b;
      };

      console.log(add(1, 1));

   **Output**

   ::

      2

The variable ``add`` refers to the anonymous function created on lines 1 through 3. We call the function using the variable name, followed by parentheses and arguments.

The visual analogy here is the same as that of a variable referring to a named function.

.. todo:: insert anonymous function reference diagram

.. note:: Like other variable declarations, an assignment statement using an anonymous function should be terminated by a semi-colon, ``;``. This is easy to overlook, since named functions do *not* end with a semi-colon.

Check Your Understanding
------------------------

.. admonition:: Question

   Convert the following named function to an anonymous function that is stored in a variable.

   .. sourcecode:: js
   
      function reverse(str) {
         let lettersArray = str.split('');
         let reversedLettersArray = lettersArray.reverse();
         return reversedLettersArray.join('');
      }

   `Refactor the program at repl.it <https://repl.it/@launchcode/Refactor-to-make-anonymous>`_

.. admonition:: Question

   Consider the code sample below, which declares an anonymous function
   beginning on line 1.

   .. sourcecode:: js

      let f1 = function(str) { 
         console.log(str + str); 
      };

      let f2 = f1;

   Which of the following are valid ways of invoking the anonymous
   function with the argument ``"abcd"``? (Choose all that apply.)

   #. ``f1("abcd");``
   #. ``function("abcd");``
   #. ``f2("abcd");``
   #. It is not possible to invoke the anonymous function, since it
      doesn’t have a name.

.. admonition:: Question

   Complete the following code snippet so that it logs an error message
   if ``userInput`` is negative.

   .. sourcecode:: js

      let logger = function(errorMsg) {
         console.log("ERROR: " + errorMsg);
      };

      if (userInput < 0) {
         ____________("Invalid input");
      }
