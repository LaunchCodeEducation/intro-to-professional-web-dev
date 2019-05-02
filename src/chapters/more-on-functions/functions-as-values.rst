Functions as Values
===================

We noted previously that functions are a powerful programming feature. This is particularly true in JavaScript, which allows functions to be used in flexible ways that are not possible in many other languages. This chapter introduces a bit more of the power of functions.

Functions Are Data
------------------

We :ref:`previously defined a value <def-value>` as "a specific piece of data." The examples we gave were things like the number ``42`` or the string ``"Hello, World!"``. While functions appear to be very different from such values, JavaScript treats them the same in many respects. 

.. index:: data type

In particular, functions have a data type, just like all other values. Recall that a **data type** is a group of values that share characteristics. All strings have a length, while numbers don't. Numbers can be manipulated in ways that strings can not be, via operations like division and subtraction.

.. admonition:: Example

   The data type of ``console.log`` is ``function``. In fact, all functions are of type ``function``.

   .. sourcecode:: js
   
      console.log(typeof console.log);   

   **Output**

   ::

      'function'

Like other data types, functions may be assigned to variables. Suppose we define a function named ``hello``. We can assign it to a variable as follows:

.. sourcecode:: js

   function hello() {

      // function body

   }

   let helloFunc = hello;

When a variable refers to a function, we can call the function using the variable name:

.. sourcecode:: js

   helloFunc();

The variable ``helloFunc`` can be thought of as an *alias* for the function ``hello``. When we use the name ``helloFunc``, JavaScript sees that it refers to the function ``hello`` and will use that *specific* function. 

This is the same behavior we have become used to when a variable holds a number or a string. The variable "points at" or "refers to" the function. When we use the variable name, it is as if we are using the specific value that the variable refers to.

.. todo:: insert named function reference diagram

*Functions are values.* In fact, functions can be used in all of the ways that other values may be used. Here are a few examples:

- Functions may be assigned to variables.
- Functions may be used in expressions, such as comparisons.
- Functions may be converted to other data types.
- Functions may be printed using ``console.log``.
- Functions may be passed as arguments to other functions.
- Functions may be returned from other functions. 

A few of these are not very useful. You will likely never need to convert a function to a boolean, or ask whether a function is greater than 5. Other items in the list, like passing functions as arguments and assigning them to variables, turn out to be extremely useful, as you will soon learn.
