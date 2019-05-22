Functions as Values
===================

.. index:: function; as a value

Functions are powerful tools in any programming language, and JavaScript uses these tools in some flexible and creative ways. This chapter introduces a bit more of the power of functions.

Functions Are Data
------------------

We :ref:`defined a value <def-value>` as "a specific piece of data." Some examples are the number ``42``, the string ``"LC101"``, and the array ``["MO", "FL", "DC"]``. *Functions are also values*, and while they appear to be very different from other values we have worked with, they share many core characteristics.

.. index:: data type

In particular, functions have a data type, just like all other values. Recall that a **data type** is a group of values that share characteristics, such as strings and numbers. Strings share the characteristice of having a length, while numbers don't. Numbers can be manipulated in ways that strings cannot, via operations like division and subtraction. 

.. admonition:: Example

   The data type of the type conversion function ``Number`` is ``function``. In fact, all functions are of type ``function``.

   .. sourcecode:: js
      :linenos:
   
      console.log(typeof 42);
      console.log(typeof "LC101");
      console.log(typeof Number);   

   **Console Output**

   ::


      number
      string
      function

Like other data types, functions may be assigned to variables. If we create a function named ``hello`` we can assign it to a variable with this syntax:

.. sourcecode:: js
   :linenos:

   function hello() {

      // function body

   }

   let helloFunc = hello;

When a variable refers to a function, we can use the variable name to *call* the function:

.. sourcecode:: js

   helloFunc();

The variable ``helloFunc`` can be thought of as an *alias* for the function ``hello``. When we call the function ``helloFunc``, JavaScript sees that it refers to the function ``hello`` and calls that *specific* function. 

When we use a variable *name*, we are really using its *value*. If the variable ``class`` is assigned the value ``"LC101"``, then ``console.log(class)`` prints ``"LC101"``. When a variable holds a function, it behaves the same way as when it holds a number or a string. The variable *refers to* the function. 

.. figure:: figures/function-var.png
   :alt: The variable helloFunc on the left *referst to* the function hello on the right

   A variable that refers to a function.

Again, *functions are values*. They can be used just like general values. For example:

- Functions may be assigned to variables.
- Functions may be used in expressions, such as comparisons.
- Functions may be converted to other data types.
- Functions may be printed using ``console.log``.
- Functions may be passed as arguments to other functions.
- Functions may be returned from other functions. 

Some of these function behaviors do not prove to be useful. You will probably never need to convert a function to a boolean, or ask whether a function is greater than 5. However, other behaviors, like passing functions as arguments and assigning them to variables, turn out to be *extremely* useful.
