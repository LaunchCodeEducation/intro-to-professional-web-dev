Error Types
===========

.. index::
   single: error; syntax
   single: error; type
   single: error; runtime
   single: object; built-in

An **error type** is the classification that JavaScript uses to group errors based on their cause. In future lessons, we will learn that an error type is actually something called a **built-in object**. For now, understanding the different types of errors will help us become faster at debugging.

Each error that JavaScript reports has an error type, and the type is included in the error message. For example, :ref:`an earlier message <syntax-error>` reported the error type as ``SyntaxError``.

::

   /Users/chris/dev/sandbox/js/syntax.js:2
   console.log("Hello, name);
               ^^^^^^^^^^^^^^

   SyntaxError: Invalid or unexpected token
      at new Script (vm.js:85:7)
      at createScript (vm.js:266:10)
      at Object.runInThisContext (vm.js:314:10)
      at Module._compile (internal/modules/cjs/loader.js:698:28)
      at Object.Module._extensions..js (internal/modules/cjs/loader.js:749:10)
      at Module.load (internal/modules/cjs/loader.js:630:32)
      at tryModuleLoad (internal/modules/cjs/loader.js:570:12)
      at Function.Module._load (internal/modules/cjs/loader.js:562:3)
      at Function.Module.runMain (internal/modules/cjs/loader.js:801:12)
      at internal/main/run_main_module.js:21:11

We have now seen two error types, ``ReferenceError`` and ``SyntaxError``. There are several other `error types in JavaScript <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#Fundamental_objects>`_, such as ``TypeError`` and ``RangeError``. 

The following table describes all JavaScript error types. Some of these relate to coding concepts we have not covered yet, but we include them here as a reference for future use.

.. list-table:: JavaScript Error Types
   :header-rows: 1

   * - Error Type
     - Description
     - Example of code triggering the error
     - Example description
   * - ``SyntaxError``
     - Occurs when trying to parse syntactically invalid code.
     -
       .. sourcecode:: js

          console.log("hello";

     - The call to ``console.log`` does not have a required close parenthesis.
   * - ``ReferenceError``
     - Occurs when a non-existent variable is used/referenced.
     -
       .. sourcecode:: js
         :linenos:

          let firstName = "Jack";
          console.log(firstname);

     - The variable ``firstname`` does not exist; it is a misspelling of ``firstName``.
   * - ``TypeError``
     - Occurs when trying to use a value in an invalid way.
     -
       .. sourcecode:: js

          1();

     - The numeric value ``1`` is not a function, so trying to use it as one results in ``TypeError: 1 is not a function``.
   * - ``RangeError``
     - Occurs when passing an invalid value to a function.
     -
       .. sourcecode:: js

          let nums = Array(-1);

     - The constructor function ``Array(n)`` creates an empty array of length ``n``. It is not possible to create an array with negative length, so the code results in ``RangeError: Invalid array length``.
   * - ``URIError``
     - Occurs when improperly using a global URI-handling function. ('URI' = Uniform Resource Identifier)
     -
       .. sourcecode:: js

          decodeURI('%');

     - The ``%`` character is used to encode characters not otherwise allowed in URIs, such as spaces (``%20``). If an invalid character encoding is given, a ``URIError`` results.
   * - ``Error``
     - The type from which all other errors are built. It can be used to generate programmer-triggered and programmer-defined errors.
     -
       .. sourcecode:: js

          throw Error("Something bad happened!");

     - Manually triggers an error with the given message.

Each time you encounter a new error type, take the time to understand what it is, and what JavaScript is trying to tell you. Remember, **error messages are your friends!**
