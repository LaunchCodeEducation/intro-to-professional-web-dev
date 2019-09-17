Functions in TypeScript
=======================

Functions in TypeScript are very similar to functions in JavaScript, however, in the declaration, you have to include the return type.

.. sourcecode:: typescript

   function myFunction(a: number): number {
      return a*2;
   }

Here you can see that we provided the type of the parameters and the type of the value that is returned.

For an anonymous function, you still need to provide types for the value returned and the parameters.

.. sourcecode:: typescript

   let myFunction = function(a: number): number { return a*2; };

TypeScript can also figure out the return type so you may not need it.
If the function doesn't have a return value, then you use ``void`` for its type.

.. sourcecode:: typescript

   let myFunction: (a: number) => number = function(a: number): number { return a*2; };

If you want to have a parameter be optional, you need to use ``?``.
Optional parameters must follow the required parameters.
You can add default parameters.

Rest parameters????