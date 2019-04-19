Introduction
============

You have been using functions throughout your learning so far, without receiving a full explanation of how functions work. This chapter focuses explicitly on the details of how functions work, how they can be used, and how you can create functions of your own. 

.. index:: ! function, method

A **function** is a reusable, callable piece of code. Like variables, functions often have names (though we will see in the next chapter that it is possible to create functions without names). 

Here are some functions that you have become familiar with:

- ``console.log``
- The type conversion functions: ``Number``, ``String``, and ``Boolean``
- String and array methods, such as ``indexOf``

.. note:: When introducing string and array methods, we noted that a **method** is a function that "belongs to" an object. This distinction is important to keep in mind, and will be explored in depth in a later chapter. For now, note that a method is a special type of function.

Each of the functions we have used works in the same way. Using the function's name, followed by parentheses, we can *call* the function, resulting in some action being carried out. Sometimes, as with ``console.log``, we can provide input data within the parenteses, which the function will use to carry out its action. 

.. admonition:: Example

   The function ``console.log`` carries out the action of printing the provided value(s). In this case, ``"Hello, World!"`` is printed to the console.

   .. sourcecode:: js

      console.log("Hello, World!");

   **Output**

   ::

      Hello, World!   
   
In addition to providing input, we may also be given a value in return when calling a function. This is what happened when we have used the type conversion functions, for example. 

.. admonition:: Example

   Type conversion functions *return* a value, that can be used by the calling code. Often, we store the return value of a function in a variable.

   .. sourcecode:: js
   
      let num = Number("42");
      console.log("The variable num is of type", typeof num, "and has value", num);

   **Output**

   ::

      The variable num is of type number and has value 42

.. index:: encapsulation

Functions are extremely powerful in that they allow us to repeat actions without writing out the full code needed to carry out that action each time. They also allow us to be removed from the details of what the function is actually doing. 

When we want to print a message to the console using ``console.log``, we do not need to be concerned with details such as what the console is, or how a string can be displayed on the console. This behavior is wrapped up within the function itself. We reap the benefits of ``console.log`` without needing to know how it works. This is an example of a broader programming concept known as **encapsulation**. Encapsulation is the process of packaging up code in a way that allows it to be resused, with the person or program using the encapsulated code not having to be concerned with the details of how it works.

.. index::
   single: function; machine

A commonly-used analogy for describing the concept of a function is that of a machine that takes input, carries out some action, and gives back some result. This is known as the **function machine** analogy.

.. figure:: figures/function-machine.png
   :alt: A "function machine," consisting of a box which takes inputs, and from which output emerges.

   The function machine

If we want to use a function, we must provide it some input (if needed). It then carries out an action using the input provided, and returns a result. What happens in the middle, when the function is doing its work, is "inside the machine" in a sense. If we know how a function should behave, we simply provide input, and receive output. The rest is up to the function machine itself.

.. note:: You may notice that a function like ``console.log`` doesn't seem to return anything. We will soon learn that *every* function returns a value, regardless of whether or not that value is used, or is even useful.

The programming concept of a function is very similar to the concept of a mathematical function. For example, in high school algebra you learned about functions such as polynomials. These functions used a mathematical variable (the input of the function) and then carried out some procedure using the input, producing a numerical result.

.. admonition:: Example

   Consider the following polynomial:

   ::

      f(x) = x² + 3x - 2

   We can *call* the function by giving it a specific *input*:

   ::

      f(3) = 3² + 3*3 - 2 = 9 + 9 - 2 = 16

   The number 16 is the *output*.

.. todo:: Link to loops chapter after merging

Functions also allow us to keep our code DRY, a concept that you learned about when we introduced loops. If we want to do the same basic task 17 times across a program, we can reduce code repetition by writing one function and calling it 17 times.

Check Your Understanding
------------------------

.. admonition:: Question

   In your own words, explain what a function is.
