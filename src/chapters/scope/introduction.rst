Introduction
============

.. index:: ! scope

Where variables are declared and initialized in the code can effect how and whether they can be used.
A variable's ability to be accessed and updated is called its **scope**.
Scope refers to the location of the variable's declaration.

Block/Local Scope
-----------------

.. index:: ! local scope

**Local scope** refers to variables declared and initialized inside a function.
Those variables can only be referenced inside of the block or function.
Referencing or attempting to update these variables outside of the function can lead to a scoping error.

Global Scope
------------

.. index:: ! global scope

**Global scope** refers to variables declared and initialized outside of a function and in the main body of the file.
These variables are accessible by any function within a file.
Global scope is the default scope in JavaScript.

Execution Context
-----------------

.. index:: ! execution context

**Execution context** refers to the conditions under which a variable is executed or its scope.
Scoping can affect the variable's behavior at runtime.

