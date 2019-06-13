Exceptions-Control-Flow
=======================

In some instances, we receive input from a user and we cannot always ensure they will type in something that will run with our code.

JavaScript gives us some control flow tools to handle exceptions by catching thrown exceptions.

We may be anticipating an exception, but still want our program to continue running and not experience a runtime error. We can tell JavaScript to **try** to run a block of code and if an exception is thrown, to **catch** the exception and run a different block of code.

.. admonition:: Example

   .. sourcecode:: js
      :caption: Code

      try {
          console.log(x[0]);
      }
      catch(ReferenceError) {
          console.log("We caught a ReferenceError, but our program continues to run!");
          console.log("0");
      }

   .. sourcecode:: js
      :caption: Output

      We caught a ReferenceError, but our program continues to run!
      0

   In this example we attept to print out the first element of our variable ``x``. We forgot to define x, but nested our code inside of a ``try`` statement and specifically **catch** ``ReferenceErrors``. It should be noted that only ReferenceErrors will be caught by the catch statement. However, we can define as many catch statements as we want.

JavaScript also provides us with a ``finally`` statement, a block of code that always runs every time regardless if the ``try``, or ``catch`` blocks run.

.. admonition:: Example

   .. sourcecode:: js
      
      try {
          console.log(x[0]);
      }
      catch(ReferenceError) {
          console.log("We caught a ReferenceError, but our program continues to run!");
          console.log("0");
      }
      finally {
          console.log("In the finally statement!");
      }

   .. sourcecode:: js
      :caption: Output

      We caught a ReferenceError, but our program continues to run!
      0
      In the finally statement!

   This try...catch block is identical to the example above, except this time we have a ``finally`` statement. The finally statement runs upon the conclusion of the try...catch statements. It is often used to remove hanging resources.
     
Errors are a normal part of coding. JavaScript defines the most common errors and provides messages to help us debug. We can extend the functionality around exceptions to further assist us in debugging or to handle expected issues in our code.

Check Your Understanding
------------------------

.. admonition:: Question

   What statement do we use if we want to attempt to run code, but think an exception might be raised?

.. admonition:: Question

   How do you handle an exception that is raised?

.. admonition:: Question

   What statement do you use to ensure a code block is executed regardless if an exception was raised?   
