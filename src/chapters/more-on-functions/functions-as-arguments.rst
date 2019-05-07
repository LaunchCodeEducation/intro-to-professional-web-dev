Functions as Arguments
======================

You now know that *functions are data*, and therefore can be passed around just like other values. In particular, this means a function can be *passed to another function* as an argument. This turns out to be extremely useful. 

Passing Functions as Arguments
------------------------------

Lots of JavaScript functions allow you pass a function as an argument. A function passed in this way can be called later, potentially multiple times. It allows the function being called to use the function argument to carry out its action.

Examples best illustrate this technique.

Example: **setTimeout**
^^^^^^^^^^^^^^^^^^^^^^^

.. index:: ! setTimeout

The built-in function ``setTimeout`` allows a programmer to specify that a function should be called a later point in time. Its basic syntax is:

::

   setTimeout(func, delayInMilliseconds);

.. admonition:: Example

   Suppose we want to log a message with a 5 second delay. Since five seconds is 5000 milliseconds (1 second = 1000 milliseconds), we can do so like this:

   .. sourcecode:: js
   
      function message() {
         console.log("The future is now!");
      }

      setTimeout(message, 5000);

   **Output**

   ::

      "The future is now!"

.. admonition:: Try It!

   Don't just take our word for it, try this yourself. `Play with our example <https://repl.it/@launchcode/setTimeout-Example>`_ to change the delay.

The function ``message`` is *passed into* ``setTimeout`` the same way any other argument is passed to a function. 

A common pattern used by JavaScript programmers is to use an anonymous function passing a function as an argument.

.. admonition:: Example

   This program has the same behavior as the one above. Instead of creating a named function and passing it to ``setTimeout``, it creates an anonymous function within ``setTimeout``'s argument list.

   .. sourcecode:: js
   
      setTimeout(function () {
         console.log("The future is now!");
      }, 5000);

Examples like this can look odd when first working with functions in this way. However, you will find that they become easier to read over time. Additionally, code that passes anonymous functions in this way is ubiquitous in JavaScript. You have probably already seen examples in documentation or on sites like Stack Overflow without recognizing them.

Example: The Array Method **map**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The array method ``map`` allows for every element in an array to be *mapped* or *translated*, using a given function. Here's how to use it generally:

::

   let mappedArray = someArray.map(func);

The argument ``func`` should take a single value from the array and return a new value. The returned array, ``mappedArray``, contains each of the return values from the mapping function, ``func``.

.. admonition:: Example

   .. sourcecode:: js
   
      let nums = [3.14, 42, 4811];

      let timesTwo = function (n) {
         return n*2;
      };

      let doubled = nums.map(timesTwo);

      console.log(doubled);

   **Output**

   ::

      [ 6.28, 84, 9622 ]

When using ``map``, many programmers will define the mapping function in the same statement as the call to ``map``.

.. admonition:: Example

   This program has the same output as the one immediately above. The mapping function is defined anonymously within the call to ``map``.

   .. sourcecode:: js
      
      let nums = [3.14, 42, 4811];

      let doubled = nums.map(function (n) {
         return n*2;
      });

      console.log(doubled);

   **Output**

   ::

      [ 6.28, 84, 9622 ]

Using Parameters as Functions
-----------------------------

The previous section illustrates how a function can be passed into another function. This section takes the opposite perspective to *write* functions that can take other functions as arguments. This technique allows a function's action to be customized by the code that calls it.

Example: A Generic Input validator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Our first example will be a generic input validator. It will prompt a user for input, using a parameter to the function to do that actual work of validating the input. 

.. admonition:: Example

   .. sourcecode:: js

      const input = require('readline-sync');

      function getValidInput(prompt, isValid) {
         
         let userInput = input.question(prompt);

         while (!isValid(userInput)) {
            console.log("Invalid input. Try again.");
            userInput = input.question(prompt);
         }

         return userInput;
      }

      let isEven = function(n) {
         return n % 2 === 0;
      };

      console.log(getValidInput('Enter an even number:', isEven));

   **Sample Output**

   ::

      Enter an even number: 3
      Invalid input. Try again.
      Enter an even number: 5
      Invalid input. Try again.
      Enter an even number: 4
      4

The function ``getValidInput`` handles the work of interacting with the user, while allowing the validation logic to be customized. This separates the different concerns of validation and user interaction, sticking to the idea that *a function should do only one thing*. It also enables more reusable code. If we need to get different input from the user, we can simply call ``getValidInput`` with different arguments.

Example: A Logger
^^^^^^^^^^^^^^^^^

Another common example in which a function uses another function to customize its behavior is that of logging. A real-world application is typically capable of logging messages such as errors, warnings, and statuses. Many such applications allow for log messages to be sent to one or more destinations, which can often be customized. For example, the application may log messages to both the console and to a file.

We can write a logging function that relies on a function parameter to determine the logging destination.

.. admonition:: Example

   The ``logError`` implemented here outputs a standardized error message to a location determined by the parameter ``logger``.

   .. sourcecode:: js
   
      let fileLogger = function(msg) {

         // Put the message in a file

      }

      function logError(msg, logger) {
         logger('ERROR: ' + msg);
      }

      logError('Something broke!', fileLogger);

This example can be made even more powerful by enabling multiple loggers.

.. admonition:: Example

   The call to ``logError`` will log the message to both the console and a file.

   .. sourcecode:: js
   
      let fileLogger = function(msg) {

         // Put the message in a file

      }

      let consoleLogger = function(msg) {
      
         console.log(msg);
      
      }

      function logError(msg, loggers) {

         for (let i = 0; i < loggers.length; i++) {
            logger[i]('ERROR: ' + msg);
         }

      }   

      logError('Something broke!', [fileLogger, consoleLogger]);

.. admonition:: Try It!

   What happens if a function expects an argument to be a function, but it isn't?

   .. sourcecode:: js
   
      function callMe(func) {
         func();
      }

      callMe("Al");

   `Run this program at repl.it <https://repl.it/@launchcode/TypeError-Example>`_

.. admonition:: Question

   What type of error occurs when attempting to use a value that is NOT a function as if it were one? 

   