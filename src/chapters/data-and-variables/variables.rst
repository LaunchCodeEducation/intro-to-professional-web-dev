Variables
=========

.. index:: ! variable

One of the most powerful features of a programming language is the ability to manipulate variables. A **variable** is a name that refers to a value. Recall that a value is a single, specific piece of data, such as a specific number or string. Variables allow us to store values for later use.

A useful visual analogy for how a variable works is that of a label that *points to* a piece of data. 

.. figure:: figures/variable.png
   :alt: A label, programmingLanguages, pointing to a the string value "JavaScript"

   A variable can be visualized as a label pointing to a specific piece of data.

In this figure, the name ``programmingLanguage`` points to the string value ``"JavaScript"``. This is more than an analogy, since it also is representative of how a variable and its value are stored in a computer's memory.

With this analogy in mind, let's look at how we can formally create variables in JavaScript.

Declaring and Initializing Variables With ``let``
-------------------------------------------------

.. index:: 
   pair: variable; declaration

.. index:: ! declaration

To create a variable in JavaScript, create a new name for the variable and precede it with the keyword ``let``:

.. sourcecode:: js
    
    let programmingLanguage;

This creates a variable named ``programmingLanguage``. The act of creating a variable is referred to as **variable declaration**, or simply **declaration**.

.. index:: 
   pair: variable; assignment
   pair: variable; initialization

.. index:: ! assignment, ! initialization

Once a variable has been declared, it may be given a value using an **assignment statement**, which uses ``=`` to give a variable a value.

.. sourcecode:: js
   :linenos:

   let programmingLanguage;
   programmingLanguage = "JavaScript";

The act of assigning a variable a value for the first time is called **initialization**.

The first line creates a variable that does not yet have a value. The variable is a label that does not point to any data.

.. figure:: figures/unassigned-variable.png
   :height: 250px
   :alt: The name "programmingLanguage" with no arrow connecting it to data.

   The result of ``let programmingLanguage;``

The second line assigns the variable a value, which connects the name to the given piece of data.

.. figure:: figures/variable.png
   :alt: A label, programmingLanguages, pointing to a the string value "JavaScript"

   The result of ``programmingLanguage = "JavaScript";``

It is possible to declare *and* initialize a variable with a single line of code. This is the most common way to create a variable.

.. sourcecode:: js

   let programmingLanguage = "JavaScript";

.. admonition:: Warning

   You will see some programmers use ``var`` to create a variable in JavaScript, like this:

   .. sourcecode:: js

      var programmingLanguage = "JavaScript";

   While this is valid syntax, you should NOT use ``var`` to declare a variable. Using ``var`` is old JavaScript syntax, and it differs from ``let`` in important ways that we will learn about later. When you see examples using ``var``, use ``let`` instead.

   If you're curious, read about `the differences between var and let <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#The_difference_between_var_and_let>`_.


To give a variable a value, use the **assignment operator**, ``=``. This operator should not be confused with the concept of *equality*, which expresses whether two things are the "same" (we will see later that equality uses the ``===`` operator).  The assignment statement links a *name*, on the left-hand side of the operator, with a *value*, on the right-hand side. This is why you will get an error if you try to run:

.. sourcecode:: js

    "JavaScript" = programmingLanguage;

An assignment statement must have the name on the left-hand side, and the value on the right-hand side.

.. admonition:: Tip

   To avoid confusion when reading or writing code, say to yourself:

   ``programmingLanguage`` is assigned ``'JavaScript'``

   or

   ``programmingLanguage`` gets the value ``'JavaScript'``.

   Don't say: 
   
   ``programmingLanguage`` equals ``'JavaScript'``.

.. index::
   pair: variable; global

.. _global-var-intro:

.. admonition:: Warning

   What if, by mistake, you leave off ``let`` when declaring a variable?

   .. sourcecode:: js

      programmingLanguage = "JavaScript";

   Contrary to what you might expect, JavaScript will not complain or throw an error. In fact, creating a variable without ``let`` is valid syntax, but it results in very different behavior. Such a variable will be a **global variable**, which we will discuss later. 

   The main point to keep in mind for now is that you should *always* use ``let`` unless you have a specific reason not to do so.

Evaluating Variables
--------------------

.. index:: variable; evaluation

After a variable has been created, it may be used later in a program anywhere a value may be used. For example, ``console.log`` prints a value, we can also give ``console.log`` a variable.

.. admonition:: Example

   These two examples have the exact same output.

   .. sourcecode:: js

      console.log("Hello, World!");

   .. sourcecode:: js
      :linenos:

      let message = "Hello, World!";
      console.log(message);

When we refer to a variable name, we are **evaluating** the variable. The effect is just as if the value of the variable is substituted for the variable name in the code when executed.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let message = "What's up, Doc?";
      let n = 17;
      let pi = 3.14159;

      console.log(message);
      console.log(n);
      console.log(pi);

   **Console Output**

   ::

      What's up, Doc?
      17
      3.14159

In each case, the printed result is the value of the variable. 

Like values, variables also have types. We determine the type of a variable the same way we determine the type of a value, using ``typeof``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:
      
      let message = "What's up, Doc?";
      let n = 17;
      let pi = 3.14159;

      console.log(typeof message);
      console.log(typeof n);
      console.log(typeof pi);

   **Console Output**

   ::

      string
      number
      number

The type of a variable is the type of the data it currently refers to.

Reassigning Variables
---------------------

We use variables in a program to "remember" things, like the current score at the football game. As their name implies, variables can change over time, just like the scoreboard at a football game. You can assign a value to a variable, and later assign it a different value.

To see this, read and then run the following program in a code editor. You'll notice that we change the value of ``day`` three times, and on the third assignment we even give it a value that is of a different data type.

.. sourcecode:: js
   :linenos:

    let day = "Thursday";
    console.log(day);

    day = "Friday";
    console.log(day);

    day = 21;
    console.log(day);

A great deal of programming involves asking the computer to remember things. For example, we might want to keep track of the number of missed calls on your phone. Each time another call is missed, we can arrange to update a variable so that it will always reflect the correct total of missed calls.

.. note:: We only use ``let`` when *declaring* a variable, that is, when we create it. We do NOT use ``let`` when reassigning the variable to a different value. In fact, doing so will result in an error.

Check Your Understanding
------------------------

.. admonition:: Question

   What is printed when the following code executes?

   .. sourcecode:: js
      :linenos:

       let day = "Thursday";
       day = 32.5;
       day = 19;
       console.log(day);

   1. Nothing is printed. A runtime error occurs.
   2. ``Thursday``
   3. ``32.5``
   4. ``19``

    
.. admonition:: Question

   How can you determine the type of a variable?

   1. Print out the value and determine the data type based on the value printed.
   2. Use ``typeof``.
   3. Use it in a known equation and print the result.
   4. Look at the declaration of the variable. 

.. admonition:: Question

   Which line is an example of variable initialization? (*Note: only one line is such an example.*)

   .. sourcecode:: js
      :linenos:
      
      let a;
      a = 42;
      a = a + 3;
