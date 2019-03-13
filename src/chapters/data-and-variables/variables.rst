Variables
=========

.. index:: ! variable

One of the most powerful features of a programming language is the ability to manipulate variables. A **variable** is a name that refers to a value. Recall that a value is a single, specific piece of data, such as a specific number or string.

A useful visual analogy for how a variable works is that of a label that "points to" a piece of data. 

.. figure:: figures/variable.png
   :height: 400px
   :alt: A label, programmingLanguages, pointing to a piece of data, "JavaScript"

   A variable can be visualized as a label poinging to a specific piece of data.

In this figure, the name/label "programmingLanguage" points to the string value "JavaScript". This is more than an analogy, as it also is representative of how a variable and the associate value are stored in a computer's memory, as we will learn later.

With this analogy in mind, let's look at how this formaly works in JavaScript.

Declaring and Initializing Variables With ``let``
-------------------------------------------------

.. index:: 
   pair: variable; declaration

.. index:: ! declaration

To create a variable in JavaScript, create a new name, or label, for the variable and precede it with ``let``:

.. sourcecode:: js
    
    let programmingLanguage;

This creates a variable named ``programmingLanguage``, and the act of creating a variable is referred to as **variable declaration**, or simply **declaration**.

.. index:: 
   pair: variable; assignment
   pair: variable; initialization

.. index:: ! assignment, ! initialization

Once a variable has been declared, it may be given a value using an **assignment statement**, which uses the ``=`` to give a variable a value.

.. sourcecode:: js
   :linenos:

   let programmingLanguage;
   programmingLanguage = "JavaScript";

The act of assigning a variable a value for the first time is called **initialization**. It is possible to both declare and initialize a variable with a single line of code.

.. sourcecode:: js

   let programmingLanguage = "JavaScript";

.. warning:: While ``let`` is the preferred way to create a variable in JavaScript, you will also see programmers sometimes use ``var`` to create a variable, like this:

   .. sourcecode:: js

      var programmingLanguage = "JavaScript";

   While this is valid syntax, **use of** ``var`` **should be avoided**. It differs from ``let`` in some important ways that we will learn about later. If you see any examples online using ``var``, for now you should use ``let`` instead.

   **🚀 Bonus Mission:** Read about `the differences between var and let <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#The_difference_between_var_and_let>`_.

The **assignment operator**, ``=``, should not be confused with *equality* (we will see later that equality uses the ``==`` operator).  The assignment statement links a *name*, on the left-hand side of the operator, with a *value*, on the right-hand side. This is why you will get an error if you try to run:

.. sourcecode:: js

    "JavaScript" = programmingLanguage;

.. tip::

   To avoid confusion when reading or writing code, say to yourself 
   
        ``programmingLanguage`` is assigned ``'JavaScript'``

   or 
    
        ``programmingLanguage`` gets the value ``'JavaScript'``. 
    
   Don't say 
    
        ``programmingLanguage`` equals ``'JavaScript'``.

.. index:: 
   pair: variable; global

.. warning:: What if, by mistake, you left off ``let`` when declaring a variable 

   .. sourcecode:: js

      programmingLanguage = "JavaScript";

   Contrary to what you might expect, JavaScript will not complain or throw an error. In fact, creating a variable without ``let`` is valid syntax, but is results in very different behavior. Such a variable will be a **global variable**, which we will learn more about in a later lesson. The main point to keep in mind now is that you always use ``let`` unless you have a specific reason not to do so.

Evaluating Variables
--------------------

If you ask JavaScript to evaluate a variable, it will produce the value that is currently linked to the variable. In other words, evaluating a variable will give you the value that is referred to by the variable.

.. sourcecode:: js

    let message = "What's up, Doc?";
    let n = 17;
    let pi = 3.14159;

    console.log(message);
    console.log(n);
    console.log(pi);

In each case the printed result is the value of the variable. Here is the output of the code above:

::

    What's up, Doc?
    17
    3.14159

Like values, variables also have types. We determine the type of a variable the same way we determine the type of a value, using ``typeof``.

.. sourcecode:: js
    
    let message = "What's up, Doc?";
    let n = 17;
    let pi = 3.14159;

    console.log(typeof message);
    console.log(typeof n);
    console.log(typeof pi);


The type of a variable is the type of the data it currently refers to.

.. index:: expression, returns

.. note:: Notice that ``console.log(typeof message);`` prints not ``typeof message`` but something else entirely. In fact, ``typeof message`` is an example of an **expression**, which we will learn about shortly. Briefly, expressions are code segments that can be reduced to a value. 

   We say that an expression **returns** a value. That is, ``typeof message`` returns ``'string'``.

Reassigning Variables
---------------------

We use variables in a program to "remember" things, like the current score at the football game. But variables are *variable*. This means they can change over time, just like the scoreboard at a football game. You can assign a value to a variable, and later assign a different value to the same variable.

To see this, read and then run the following program in a code editor. You'll notice that we change the value of ``day`` three times, and on the third assignment we even give it a value that is of a different data type.

.. sourcecode:: js

    let day = "Thursday";
    console.log(day);
    day = "Friday";
    console.log(day);
    day = 21;
    console.log(day);

A great deal of programming is about having the computer remember things. For example, we might want to keep track of the number of missed calls on your phone. Each time another call is missed, we can arrange to update or change a variable so that it will always reflect the correct total of missed calls.

.. note:: We only use ``let`` when *declaring* a variable, that is, when we create it. We do not use ``let`` when reassigning the variable to a different value. In fact, doing so will result in an error.

Check Your Understanding
------------------------

.. admonition:: Question

   What is printed when the following statements execute?

   .. sourcecode:: js

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
      
      let a;
      a = 42;
      a = a + 3;
