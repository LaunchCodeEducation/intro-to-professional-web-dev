Functions in TypeScript
=======================

When creating functions in TypeScript, we have many of the same options as in JavaScript.
We can make anonymous functions, give it a different number of parameters and so on.
However, when working with functions in TypeScript, we have to keep *type* in mind.

Declaring Functions
-------------------

Named Functions
^^^^^^^^^^^^^^^

Let's take a look at a TypeScript function declaration.

.. sourcecode:: typescript

   function myFunction(a: number): number {
      return a*2;
   }

Here you can see that we provided the type of the parameters and the type of the value that is returned.
If the function doesn't have a return value, then you use ``void`` for its type.

.. note::

   While in many cases, it is possible to determine the return type during compilation, if you know the return type, you should give it. 

Anonymous Functions
^^^^^^^^^^^^^^^^^^^

For an anonymous function, you still need to provide types for the value returned and the parameters.

.. sourcecode:: typescript

   let myFunction = function(a: number): number { return a*2; };

The above code looks very much like an anonymous function declaration with the types included!
However, TypeScript has arrow notation and here we use the **fat arrow**, ``=>``.

.. sourcecode:: typescript

   let myFunction: (a: number) => number = function(a: number): number { return a*2; };

In TypeScript, the keywords that come after the colon are the type. The ``=>`` operator then indicates the return type of the function.

Optional Parameter
------------------

In JavaScript, you can declare a function with 5 parameters and only give it 2 when it comes time to use it.
In TypeScript, that is not the case. When you declare a function with 5 parameters, you have to give the function 5 arguments when calling it.
However, in TypeScript, you can make parameters optional. This means that when you are calling the function, you can leave off the optional parameter.

To denote a parameter as optional, you can use ``?`` notation. Any parameters that are optional must follow the required parameters.

.. admonition:: Example

   .. sourcecode:: typescript

      function myFunction(a: number, b?:number): number {
         return a+b;
      }

      console.log(myFunction(1,2));
      console.log(myFunction(1));
      console.log(myFunction(3,5));
      console.log(myFunction(3));

   ::

      3
      1
      8
      3

In this example, the ``myFunction`` function has two parameters, ``a`` and ``b``. ``a`` is required and ``b`` is optional. When only one argument is provided to the function, then the value of ``a`` is returned.
When both arguments are provided, then the sum of the 2 arguments is returned.

Another way to deal with a parameter you need to be optional is to give it a default value.

Let's say that in the example above, we wanted to give ``b`` a default value of 5. That way, if no argument is supplied for ``b``, then the value returned is that of ``a+5``.

.. admonition:: Example

   .. sourcecode:: typescript

      function myFunction(a: number, b = 5): number {
         return a+b;
      }

      console.log(myFunction(1,2));
      console.log(myFunction(1));
      console.log(myFunction(3,6));
      console.log(myFunction(3));      

   :: 

      3
      6
      9
      8

Because ``b`` has a default value of ``5``, when the user does not pass a value to the second argument of ``myFunction``, 5 is used as the value of ``b``.

Check Your Understanding
------------------------

.. admonition:: Question

   What is wrong with this function declaration? NOTE there are 3 things that are wrong here.

   .. sourcecode:: typescript

      let myFunction (a:number, b/:number) -> string = function(a:number,b?:number) {return a*b;};

