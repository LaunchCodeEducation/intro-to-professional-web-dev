Introduction
============

.. index:: ! scope

Errors are a part of coding. Occasionally, we make mistakes as programmers. However, we are always trying to fix those mistakes by reading different resources, the stacktrace, or asking for help.

Earlier in this course, we learned about two different types of errors: runtime and logic. A logic error is when your program executes without breaking, but doesn't behave the way you thought it would. These logic errors usually require you to consider how you are going about solving the issue to resolve. Runtime errors are when your program does not run correctly, and an exception is raised.

An **exception** is a runtime error in which a name and message are displayed to provide more information about the error.

Exceptions and Errors
---------------------

In JavaScript a runtime error and an exception are the same thing and can be used interchangeably. This can cause confusion because a logic error is not an exception!

Error Object
------------

When a runtime error, also known as an execption, is raised JavaScript returns an ``Error`` object. An Error Object has two properties: a name and a message. The name refers to the type of error that occured, while the message gives the user information on why that exception occured. 

JavaScript has built-in exceptions with pre-defined names and messages, however, JavaScript also gives you the ability to create your own error messages.

You have undoubtedly experienced various Exceptions already throughout this class. Let's look at a few common Exceptions.

Common Exceptions
-----------------

JavaScript has some built-in Exceptions you may have already encountered in this class.

One of the most common errors in Javascript is a ``SyntaxError`` which is thrown when we include a symbol JavaScript is not expecting.

.. admonition:: Example

   .. sourcecode:: js

      console.log("This is" an example);

   **Console Output**

   ::

      SyntaxError: missing ) after argument list

   We put our second quotation mark in the incorrect place. JavaScript does not know what to do with the second half of our phrase and throws a ``SyntaxError`` with the message: ``missing ) after argument list``.


A ``ReferenceError`` is thrown when we try to use a variable that has not yet been defined.

.. admonition:: Example

   .. sourcecode:: js

      console.log(x[0]);

   **Console Output**

   ::

      ReferenceError: x is not defined

   We attempt to print out the first element in the variable x, but we never declared x. JavaScript throws a ``ReferenceError`` with the message: ``x is not defined``.

A ``TypeError`` is thrown when JavaScript expects something to be one type, but the provided value is a different type.

.. admonition:: Example

   .. sourcecode:: js

      const a = "Launch";
      
      a = "Code";

   **Console Output**

   ::

      TypeError: invalid assignment to const 'a'

In this case, we declare a constant as the string "Launch", and then try to change the immutable variable to "Code". JavaScript throws a ``TypeError`` with the message: ``invalid assignment to const 'b'``.

Exceptions give us a way to provide more information on how something went wrong. JavaScript's built-in Exceptions are regularly used in the debugging process.

There are more built-in Exceptions in Java, you can read more by referencing the `MDN Errors Documentation <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors>`_ or `W3Schools JavaScript Error <https://www.w3schools.com/js/js_errors.asp>`_.

In the next section we will learn how to raise our own exceptions using the ``throw`` statement.

Check Your Understanding
------------------------

.. admonition:: Question

   What is the difference between a runtime error, and a logic error?

.. admonition:: Question

   What are some of the common errors included in JavaScript?
