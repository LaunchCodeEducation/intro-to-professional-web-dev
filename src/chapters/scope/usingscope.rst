Using Scope
===========

Execution context is everything.
Some variables you want to set as constants that can be accessed globally like pi.
Others you want to keep secure to minimize the danger of accidental updates to the variable's value.
For example, a variable holding someone's username should be kept secure.

Shadowing
---------

.. index:: ! variable shadowing, ! shadowing

**Variable shadowing** is where two variables in different scopes have the same name.
The variables can then be access under different context, however, it can effect the variable visibility.

.. note::

	Though we don't use the ``var`` keyword in this book, you will see it a lot in other JavaScript resources.
	We do not use ``var`` because of **variable hoisting**



