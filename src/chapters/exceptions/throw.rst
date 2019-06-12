Throw
=====

In most programming languages when the compiler, or interpreter encounters code it doesn't know how to handle it has to notify the programmer that something has gone wrong. We call this act "throwing an exception". This is where the term throw comes from.

JavaScript gives us a throw statement to raise exceptions whenever we need to inform the programmer that something happened that the programming language doesn't know how to handle.

JavaScript gives us the ability to raise exceptions using the **throw** statement.

Default Error
-------------

We can throw a default Error object by using the throw statement, and passing the message in as an argument.

.. admonition:: Example

   .. sourcecode:: js
      :caption: Code

      throw ("You cannot divide by zero!");

   .. sourcecode:: js
      :caption: Output

      Error: You cannot divide by zero!

   We can throw a default Error and define the message.

Pre-existing Error
------------------

JavaScript also gives us the power to throw a more specific type of error.

.. admonition:: Example

   .. sourcecode:: js
      :caption: Code

      throw SyntaxError("That is the incorrect syntax");

   .. sourcecode:: js
      :caption: Output

      SyntaxError: That is the incorrect syntax

   We can throw built in Exceptions, and change the message that is displayed.

JavaScript gives us flexibiltiy by allowing us to raise standard library errors, and to define our own errors. We can use exceptions to allow our program to break, and provide useful information as to why something went wrong.

Custom Error
------------

JavaScript will also let you define new types of Errors, by creating a new Error, and defining it's name, and message, however created our own errors goes beyond the scope of this class.

Check Your Understanding
------------------------

.. admonition:: Question

   What statement do we use to raise an exception?

.. admonition:: Question

   How do we customize the message of an exception?