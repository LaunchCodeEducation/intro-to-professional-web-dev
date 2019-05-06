Introduction
============

You have been using functions throughout your learning so far, without receiving a full explanation of how functions work. This chapter focuses explicitly on the details of how functions work, how they can be used, and how you can create functions of your own. 

.. index:: ! function, method

A **function** is a reusable, callable piece of code. Like variables, functions often have names (though the next chapter shows us that we can create functions without names). 

You have already become familiar with several functions:

- ``console.log``
- The type conversion functions: ``Number``, ``String``, and ``Boolean``
- String and array methods, such as ``indexOf``

.. note:: When learning about strings and arrays, we noted that a **method** is a function that "belongs to" an object. This distinction is important to keep in mind, and will be explored in depth in a later chapter. For now, think of a method as a *special type* of function.

Each of the functions we have used works in the same way. By typing the function's name, followed by parentheses, we can *call* the function, resulting in an action being carried out. Sometimes, as with ``console.log``, we can provide input data between the parentheses, which the function will use to carry out its action. 

.. admonition:: Example

   The function ``console.log`` prints the provided value or values (the input data). 

   .. sourcecode:: js

      console.log("Hello, World!");

   **Output**

   ::

      Hello, World!   
   
This is an example of a function receving *input*. Functions may also provide *output*. For example, the type conversion functions give back the result of converting a value.

.. admonition:: Example

   Type conversion functions *return* a value, that can be used by the calling code. Often, we store the return value of a function in a variable.

   .. sourcecode:: js
   
      let num = Number("42");
      console.log("The variable num is of type", typeof num, "and has value", num);

   **Output**

   ::

      The variable num is of type number and has value 42

.. admonition:: Example

   Many array and string methods also return values. This program uses the string method ``split`` to break a string into separate components.

   .. sourcecode:: js
   
      let commaSeparatedValues = "Smith,Jane,100 Cherry Blossom Lane";
      let values = commaSeparatedValues.split(',');
      console.log(values);

   **Output**

   ::

      [ 'Smith', 'Jane', '100 Cherry Blossom Lane' ]

.. index:: encapsulation

Functions are extremely powerful. They allow us to repeat actions without repeating each individual step of code that the actions are built from. By grouping actions together, functions allow us to be removed from the details of what they are actually doing. 

When we want to print a message to the console using ``console.log``, we don't have to know what the console is, or how a string can be displayed on it. The behavior is wrapped up within the function itself. This is an example of a broader programming concept known as **encapsulation**. Encapsulation is the process of packaging up code in a reusable way, without the programmer needing to be concerned with how it works.

.. index::
   single: function; machine

.. _function-machine:

A commonly-used analogy for describing the concept of a function is that of a machine that takes input, carries out an action, and gives back a result. This is known as the **function machine** analogy.

.. figure:: figures/function-machine.png
   :alt: A "function machine," consisting of a box which takes inputs, and from which output emerges.

   The function machine

If we want to use a function, we must provide it some input (if needed). It carries out an action on the input and returns a result. The action occurs within the function, or "inside the machine". If we know the purpose of a function, we simply provide it input and receive the output. The rest is up to the machine itself.

.. note:: You may notice that a function like ``console.log`` doesn't seem to return anything. We will soon learn that *every* function returns a value, regardless of whether or not that value is used, or is even useful.

The programming concept of a function is very similar to the concept of a mathematical function. For example, in high school algebra you learned about functions like ``y = 4x + 7``. These functions used a mathematical input (``x``) and carried out a procedure to return a numerical result (``y``).

.. admonition:: Example

   Consider the following mathematical function:

   ::

      f(x) = x² + 4x - 2

   We can *call* the function by giving it a specific *input*:

   ::

      f(3) = 3² + 4*3 - 2 = 9 + 12 - 2 = 19

   The number 19 is the *output*.

.. todo:: Link to loops chapter after merging

Functions also allow us to keep our code DRY, a concept that you learned about when we introduced loops. If we want to do the same basic task 17 times across a program, we can reduce code repetition by writing one function and calling it 17 times.

Check Your Understanding
------------------------

.. admonition:: Question

   In your own words, explain what a function is.
