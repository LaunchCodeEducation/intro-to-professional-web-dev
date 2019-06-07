Using Scope
===========

Scope allows programmers to control the flow of information through the variables in their program.
Some variables you want to set as constants that can be accessed globally like pi.
Others you want to keep secure to minimize the danger of accidental updates to the variable's value.
For example, a variable holding someone's username should be kept secure.

Shadowing
---------

.. index:: ! variable shadowing, ! shadowing

**Variable shadowing** is where two variables in different scopes have the same name.
The variables can then be accessed under different contexts, however, shadowing can effect the variable's visibility.

Variable Hoisting
-----------------

.. index:: ! variable hoisting

**Variable hoisting** is a behavior in JavaScript where variable declarations are "hoisted" to the top of the current scope.
Hoisting occurs when the ``var`` keyword is used in the declaration, but does not occur when ``let`` and ``const`` keywords are used in the declaration.

.. note::

	Though we don't use the ``var`` keyword in this book, you will see it a lot in other JavaScript resources.
	Variable hoisting is an important concept to keep in mind as you work with JavaScript.



