Functions in TypeScript
=======================

When creating functions in TypeScript, we have many of the same options as in JavaScript.
We can make anonymous functions, give them a different number of parameters, and so on.
However, when working with functions in TypeScript, we have to keep *data types* in mind.

Declaring Functions
-------------------

Named Functions
^^^^^^^^^^^^^^^

Let's take a look at a TypeScript function declaration.

.. admonition:: Example

   We want to declare a function called ``myFunction``.
   ``myFunction`` has one parameter, a number called ``x``.
   ``myFunction`` returns the value of ``x`` multiplied by 2.

   With this in mind, the declaration in TypeScript would look like:

   .. sourcecode:: typescript

      function myFunction(x: number): number {
         return x*2;
      }

   Here you can see that we provided the type of the parameter and the type of the value that is returned after the colons.
   If ``x`` were a string or a boolean, then we would replace ``number`` with the data type of ``x``.

What if the function doesn't return a value? In these cases, we use ``void`` as the return type.

.. admonition:: Example

   Let's change up ``myFunction`` a little bit!
   ``myFunction`` still has one parameter, our number called ``x``, however, it doesn't return a specific value.

   .. sourcecode:: typescript

      let y: number = 0;

      function myFunction(x: number): void {
         y = x*2;
      }

   Instead of returning the value of ``x`` multiplied by 2, ``myFunction`` now assigns the value of ``x`` multiplied by 2 to another variable, ``y``.
   We can now use ``void`` to specify that no value is returned.

Anonymous Functions
^^^^^^^^^^^^^^^^^^^

For an anonymous function, you still need to provide types for the value returned and the parameters.

.. admonition:: Example

   Now we want to declare an anonymous function, ``myFunction``, which has one parameter, a number called ``x``, and returns the value of ``x`` multiplied by 2.

   .. sourcecode:: typescript

      let myFunction = function(x: number): number { return x*2; };

Just as we did above with the named function, we need to make sure that we include the data type for the parameters and the return type of the function.

Optional Parameter
------------------

When declaring a function in TypeScript, you may make some of your parameters optional.
This means that when you are calling the function, you can leave off the optional parameter(s).

To denote a parameter as optional, we use the ``?`` notation. Any parameters that are optional must follow the required parameters.

.. admonition:: Example

   .. sourcecode:: typescript
      :linenos:

	   function myFunction(a: number, b?:number): number {
		   if (typeof b !== 'undefined'){
			   return a+b+5;
			} else {
				return a+5;
			}
		}

      console.log(myFunction(1,2));
      console.log(myFunction(1));
      console.log(myFunction(3,5));
      console.log(myFunction(3));

   ::

      8
      6
      13
      8

In this example, the ``myFunction`` function has two parameters, ``a`` and ``b``.
``a`` is required and ``b`` is optional. When both arguments are provided, then the sum of the 2 arguments and 5 is returned.
When only one argument is provided to the function, then the value of ``a+5`` is returned.

Another way to deal with a parameter you need to be optional is to give it a default value.

Let's say that in the example above, we wanted to give ``b`` a default value of 5.
That way, if no argument is supplied for ``b``, then the value returned is that of ``a+10``.

.. admonition:: Example

   .. sourcecode:: typescript
      :linenos:

      function myFunction(a: number, b = 5): number {
         return a+b+5;
      }

      console.log(myFunction(1,2));
      console.log(myFunction(1));
      console.log(myFunction(3,5));
      console.log(myFunction(3));      

   :: 

      8
      11
      13
      13

Because ``b`` has a default value of ``5``, when the user does not pass a value to the second argument of ``myFunction``, 5 is used as the value of ``b``.

Check Your Understanding
------------------------

.. admonition:: Question

   What is wrong with this function declaration? NOTE there are at least 3 things that should be changed.

   .. sourcecode:: typescript

      let myFunction = function(a:number,b? = 3) {return a*b};

.. ans: let myFunction = function(a:number, b=3): number {return a*b;};

