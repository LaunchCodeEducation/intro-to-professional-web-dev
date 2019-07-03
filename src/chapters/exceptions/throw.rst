Throw
=====

In most programming languages, when the compiler or interpreter encounters code it doesn't know how to handle, it throws an exception. This is how the compiler notifies the programmer that something has gone wrong.

JavaScript gives us the ability to raise exceptions using the ``throw`` statement.

Default Error
-------------

We can throw a default Error object by using the ``throw`` statement and passing the message in as an argument.

.. admonition:: Example

   .. sourcecode:: js

      throw ("You cannot divide by zero!");

   **Console Output**

   ::

      Error: You cannot divide by zero!

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