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
   If ``x`` was a string or a boolean, then we would replace ``number`` with the data type of ``x``.

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

In JavaScript, you can declare a function with 5 parameters and only give it 2 when it comes time to use it.
In TypeScript, that is not the case.
In TypeScript when you declare a function with 5 parameters, you have to give the function 5 arguments when calling it, unless you make some of those parameters optional.
As with JavaScript functions, optional parameters can be omitted.
This means that when you are calling the function, you can leave off the optional parameter(s).

To denote a parameter as optional, you can use ``?`` notation. Any parameters that are optional must follow the required parameters.

.. admonition:: Example

   .. sourcecode:: typescript

      function myFunction(a: number, b?:number): number {
         return a+b+5;
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
``a`` is required and ``b`` is optional.
When only one argument is provided to the function, then the value of ``a+5`` is returned.
When both arguments are provided, then the sum of the 2 arguments and 5 is returned.

Another way to deal with a parameter you need to be optional is to give it a default value.

Let's say that in the example above, we wanted to give ``b`` a default value of 5.
That way, if no argument is supplied for ``b``, then the value returned is that of ``a+10``.

.. admonition:: Example

   .. sourcecode:: typescript

      function myFunction(a: number, b = 5): number {
         return a+b+5;
      }

      console.log(myFunction(1,2));
      console.log(myFunction(1));
      console.log(myFunction(3,6));
      console.log(myFunction(3));      

   :: 

      8
      11
      14
      13

Because ``b`` has a default value of ``5``, when the user does not pass a value to the second argument of ``myFunction``, 5 is used as the value of ``b``.

Check Your Understanding
------------------------

.. admonition:: Question

   What is wrong with this function declaration? NOTE there are 3 things that are wrong here.

   .. sourcecode:: typescript

      let myFunction = function(a:string,b??:number) {return a*b};

