Introduction
============

.. index:: ! scope

Where variables are declared and initialized in the code can effect whether or not they can be used.
**Scope** refers to the ability to access and use the variable.

.. admonition:: Example 

	.. sourcecode:: js

		let a = 0;

		function coolFunction() {
			let b = 0;
		}

	``a`` is accessible *inside* and *outside* of ``coolFunction()``. 
	``b`` is only accessible *inside* of ``coolFunction()``.

Block/Local Scope
-----------------

.. index:: ! local scope

**Local scope** refers to variables declared and initialized inside a function.
Those variables can only be referenced inside of the block or function.
In the example above, ``b`` has local scope.
Referencing or attempting to update these variables outside of the function can lead to a scoping error.

Global Scope
------------

.. index:: ! global scope

**Global scope** refers to variables declared and initialized outside of a function and in the main body of the file.
These variables are accessible by any function within a file.
In the example above, ``a`` has local scope.
Global scope is the default scope in JavaScript.

**TRY IT FOR BROKEN CODE**

Execution Context
-----------------

.. index:: ! execution context

**Execution context** refers to the conditions under which a variable is executed or its scope.
Scoping can affect the variable's behavior at runtime.
When the code is run in the browser, everything is first run at a global context.
As the compiler processes the code, it may run into a function, in which case it moves through the function context before returning to global execution context.

Let's consider this code:

.. sourcecode:: js

	let a = 0;

	function coolFunction() {
		let b = 0;
		return a + b;
	}

	function coolerFunction() {
		let c = 0;
		c = coolFunction();
		return c;
	}

Now, let's consider the execution context for each step.

1. First, the global execution context is entered as the compiler executes the code.
2. Once coolFunction() is hit, the compiler creates and executes coolFunction() under the coolFunction() execution context.
3. Upon completion, the compiler returns to the global execution context.
4. The compiler stays at the global execution context until the creation and execution of coolerFunction().
5. Inside of coolerFunction() is a call to coolFunction(). The compiler will go up in execution context to coolFunction() before returning down to coolerFunction()'s execution context and upon completion of the function, down to the global execution context.

Check Your Understanding
------------------------

Both of the concept checks refer to the following code block:

.. sourcecode:: js

	function myFunction(n) {
		let a = 100;
		return a + n;
	}
	
	let x = 0;

	x = myFunction(x);
	
.. admonition:: Question

	What scope is variable ``x``?

	a. Global
	b. Local

.. admonition:: Question

	In what order will the compiler execute the code?