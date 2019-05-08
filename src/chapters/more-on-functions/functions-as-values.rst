Functions as Values
===================

.. index:: function; as a value

As we have noted, functions are a powerful programming feature. JavaScript in particular allows functions to be used in flexible ways that are not possible in many other languages. This chapter introduces a bit more of the power of functions.

Functions Are Data
------------------

We :ref:`defined a value <def-value>` as "a specific piece of data." Some examples are the number ``42``, the string ``"Hello, World!"``, and the array ``["MO", "FL", "DC"]``. *Functions are also values*, and while they appear to be very different from other values we have worked with, they share many core characteristics.

.. index:: data type

In particular, functions have a data type, just like all other values. Recall that a **data type** is a group of values that share characteristics, such as strings and numbers. All strings have a length, while numbers don't. Numbers can be manipulated in ways that strings cannot be, via operations like division and subtraction. 

.. admonition:: Example

   The data type of the type conversion function ``Number`` is ``function``. In fact, all functions are of type ``function``.

   .. sourcecode:: js
   
      console.log(typeof Number);   

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

We are used to this behavior when a variable holds a number or a string. When a variable holds a function, the variable "points at" or "refers to" the function. When we use the variable name, it is as if we are using the specific value that the variable refers to.

.. todo:: insert named function reference diagram

Again, *functions are values*. They can be used just like general values. Here are a few examples:

- Functions may be assigned to variables.
- Functions may be used in expressions, such as comparisons.
- Functions may be converted to other data types.
- Functions may be printed using ``console.log``.
- Functions may be passed as arguments to other functions.
- Functions may be returned from other functions. 

A few of these are not very useful. You will likely never need to convert a function to a boolean, or ask whether a function is greater than 5. Other items in the list, like passing functions as arguments and assigning them to variables, turn out to be extremely useful, as you will soon learn.
