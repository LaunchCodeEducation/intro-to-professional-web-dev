Throw
=====
.. index:: ! throws

In most programming languages, when the compiler or interpreter encounters code it doesn't know how to handle, it
**throws** an exception. This is how the compiler notifies the programmer that something has gone wrong. Throwing
an exception is also known as *raising* an exception.

JavaScript gives us the ability to raise exceptions using the ``throw`` statement. One reason to throw an exception
is if your code is being used in an unexpected way.

Throw Default Error
-------------------

We can throw a default Error by using the ``throw`` statement and passing in a string description as a argument.

.. admonition:: Example

   .. replit:: js
      :slug: throw-example
      :linenos:

      throw Error("You cannot divide by zero!");

   **Console Output**

   ::

      Error: You cannot divide by zero!
      at evalmachine.<anonymous>:1:7
      at Script.runInContext (vm.js:133:20)
      at Object.runInContext (vm.js:311:6)
      at evaluate (/run_dir/repl.js:133:14)

   The error text displays the error name, and it contains details about where the error was thrown.
   The text ``at evalmachine.<anonymous>:1:7`` indicates that the error as thrown from line 1, which we know is
   true because our example only has one line of code.

.. _exception-expectations:

.. admonition:: Note

   With all that we have learned about unit testing, you might be wondering how you test if an error is thrown when it should be.
   To do so, let's imagine our example above is inside a function called ``checkThrow()``. We need can then use the ``toThrow()`` matcher like so:

   .. sourcecode:: js

      expect( function() { checkThrow() }).toThrow(new Error('You cannot divide by zero!'));

Pre-existing Error
------------------

JavaScript also gives us the power to throw a more specific type of error.

.. admonition:: Example

   .. sourcecode:: js

      throw SyntaxError("That is the incorrect syntax");

   **Console Output**

   ::

      SyntaxError: That is the incorrect syntax

   JavaScript gives us flexibility by allowing us to raise standard library errors and to define our own errors. We can use exceptions to allow our program to break and provide useful information as to why something went wrong.


Custom Error
------------

JavaScript will also let you define new types of Errors. You may find this helpful in the future, however, that goes beyond the scope of this class.

Check Your Understanding
------------------------

.. admonition:: Question

   What statement do we use to raise an exception?

.. admonition:: Question

   How do we customize the message of an exception?
