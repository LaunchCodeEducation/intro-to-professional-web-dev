Receiving Function Arguments
============================

The previous section illustrates how a function can be passed to another function as an argument. This section takes the opposite perspective to *write* functions that can take other functions as arguments.

Example: A Generic Input Validator
----------------------------------

Our first example will be a generic input validator. It will prompt a user for input, using a parameter to the function to do the actual work of validating the input. 

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      const input = require('readline-sync');

      function getValidInput(prompt, isValid) {
         
         // Prompt the user, using the prompt string that was passed
         let userInput = input.question(prompt);

         // Call the boolean function isValid to check the input
         while (!isValid(userInput)) {
            console.log("Invalid input. Try again.");
            userInput = input.question(prompt);
         }

         return userInput;
      }

      // A boolean function for validating input
      let isEven = function(n) {
         return Number(n) % 2 === 0;
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

.. admonition:: Example

   This example uses the same ``getValidInput`` function defined above with a different prompt and validator function. In this case, we check that a potential password has at least 8 characters.

   .. sourcecode:: js
      :linenos:

      const input = require('readline-sync');

      function getValidInput(prompt, isValid) {
         
         let userInput = input.question(prompt);

         while (!isValid(userInput)) {
            console.log("Invalid input. Try again.");
            userInput = input.question(prompt);
         }

         return userInput;
      }

      let isValidPassword = function(password) {

         // Passwords should have at least 8 characters
         if (password.length < 8) {
            return false;
         }

         return true;
      };

      console.log(getValidInput('Create a password:', isValidPassword));

   **Sample Output**

   ::

      Create a password: launch
      Invalid input. Try again.
      Create a password: code
      Invalid input. Try again.
      Create a password: launchcode
      launchcode

.. admonition:: Try It!

   #. Use our ``getValidInput`` function to ensure user input starts with "a".
   #. Create another validator that ensures user input is a vowel.

   `Try it at repl.it <https://repl.it/@launchcode/Validator-check>`_


Example: A Logger
-----------------

Another common example of a function using another function to customize its behavior is that of logging. Real-world applications are capable of logging messages such as errors, warnings, and statuses. Such applications allow for log messages to be sent to one or more destinations. For example, the application may log messages to both the console and to a file.

We can write a logging function that relies on a function parameter to determine the logging destination.

A Simple Logger
^^^^^^^^^^^^^^^

.. admonition:: Example

   The ``logError`` function outputs a standardized error message to a location determined by the parameter ``logger``.

   .. sourcecode:: js
      :linenos:
   
      let fileLogger = function(msg) {

         // Put the message in a file

      }

      function logError(msg, logger) {
         let errorMsg = 'ERROR: ' + msg;
         logger(errorMsg);
      }

      logError('Something broke!', fileLogger);

Let's examine this example in more detail.

There are three main program components:

#. Lines 1-5 define ``fileLogger``, which takes a string argument, ``msg``. We have not discussed writing to a file, but Node.js is capable of doing so. 
#. Lines 7-10 define ``logError``. The first parameter is the message to be logged. The second parameter is the logging function that will do the work of sending the message somewhere. ``logError`` doesn't know the details of how the message will be logged. It simply formats the message, and calls ``logger``.
#. Line 12 logs an error using the ``fileLogger``.

This is the flow of execution:

#. ``logError`` is called, with a message and the logging function ``fileLogger`` passed as arguments.
#. ``logError`` runs, passing the constructed message to ``logger``, which refers to ``fileLogger``.
#. ``fileLogger`` executes, sending the message to a file.

A More Complex Logger
^^^^^^^^^^^^^^^^^^^^^

This example can be made even more powerful by enabling multiple loggers.

.. admonition:: Example

   The call to ``logError`` will log the message to both the console and a file.

   .. sourcecode:: js
      :linenos:
   
      let fileLogger = function(msg) {

         // Put the message in a file

      }

      let consoleLogger = function(msg) {
      
         console.log(msg);
      
      }

      function logError(msg, loggers) {

         let errorMsg = 'ERROR: ' + msg;

         for (let i = 0; i < loggers.length; i++) {
            logger[i](errorMsg);
         }

      }   

      logError('Something broke!', [fileLogger, consoleLogger]);

The main change to the program is that ``logError`` now accepts an *array* of functions. It loops through the array, calling each logger with the message string.

As with the validation example, these programs separate behaviors in a way that makes the code more flexible. To add or remove a logging destination, we can simply change the way that we call ``logError``. The code *inside* ``logError`` doesn't know about how each logging function does it's job. It is concerned merely with creating the message string and passing it to the logger(s).

A Word of Caution
-----------------

What happens if a function expects an argument to be a function, but it isn't?

.. admonition:: Try It!

   .. sourcecode:: js
      :linenos:
   
      function callMe(func) {
         func();
      }

      callMe("Al");

   `Run this program at repl.it <https://repl.it/@launchcode/TypeError-Example>`_

.. admonition:: Question

   What type of error occurs when attempting to use a value that is NOT a function as if it were one? 

   