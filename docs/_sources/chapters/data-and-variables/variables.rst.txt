Variables
=========

.. index:: ! variable

One of the most powerful features of a programming language is the ability to manipulate variables. A **variable** is a name that refers to a value. Recall that a value is a single, specific piece of data, such as a specific number or string. Variables allow us to store values for later use.

A useful visual analogy for how a variable works is that of a label that "points to" a piece of data. 

.. figure:: figures/variable.png
   :alt: A label, programmingLanguages, pointing to a the string value "JavaScript"

   A variable can be visualized as a label pointing to a specific piece of data.

In this figure, the name "programmingLanguage" points to the string value "JavaScript." This is more than an analogy, since it also is representative of how a variable and the associated value are stored in a computer's memory, as we will learn later.

With this analogy in mind, let's look at how we can formaly create variables in JavaScript.

Declaring and Initializing Variables With ``let``
-------------------------------------------------

.. index:: 
   pair: variable; declaration

.. index:: ! declaration

To create a variable in JavaScript, create a new name for the variable and precede it with ``let``:

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

The act of assigning a variable a value for the first time is called **initialization**. 

We can visualize the action of the two lines of code above as follows. The first line creates a variable that does not yet have a value. It is a name that does not point to any data.

.. figure:: figures/unassigned-variable.png
   :height: 250px
   :alt: The name "programmingLanguage" with no arrow connecting it to data.

   The result of ``let programmingLanguage;``

The second line assigns the variable a value, which connects the name to the given piece of data.

.. figure:: figures/variable.png
   :alt: A label, programmingLanguages, pointing to a the string value "JavaScript"

   The result of ``programmingLanguage = "JavaScript";``

It is possible to both declare and initialize a variable with a single line of code. This is the best way to create a variable when its value is known.

.. sourcecode:: js

   let programmingLanguage = "JavaScript";

.. warning:: You will see some programmers use ``var`` to create a variable in JavaScript, like this:

   .. sourcecode:: js

      var programmingLanguage = "JavaScript";

   While this is valid syntax, **use of** ``var`` **should be avoided**. It differs from ``let`` in some important ways that we will learn about later. If you see any examples online using ``var``, for now you should use ``let`` instead.

   **🚀 Bonus Mission:** Read about `the differences between var and let <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#The_difference_between_var_and_let>`_.

To give a variable a value, we use the **assignment operator**, ``=``. This operator should not be confused with the concept of *equality*, which expresses whether two things are the "same" (we will see later that equality uses the ``===`` operator).  The assignment statement links a *name*, on the left-hand side of the operator, with a *value*, on the right-hand side. This is why you will get an error if you try to run:

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

.. warning:: What if, by mistake, you leave off ``let`` when declaring a variable?

   .. sourcecode:: js

      programmingLanguage = "JavaScript";

   Contrary to what you might expect, JavaScript will not complain or throw an error. In fact, creating a variable without ``let`` is valid syntax, but is results in very different behavior. Such a variable will be a **global variable**, which we will learn more about in a later lesson. The main point to keep in mind for now is that you should always use ``let`` unless you have a specific reason not to do so.

Evaluating Variables
--------------------

.. index:: variable; evaluation

After a variable has been created, it may be used later in a program in any place where a value may be used. For example, we know that ``console.log`` prints a value, so we can also give ``console.log`` a variable.

.. sourcecode:: js

   console.log("Hello, World!");

.. sourcecode:: js

   let message = "Hello, World!";
   console.log(message);

These two examples have the exact same same output.

When we refer to a variable name, we are **evaluating** the variable. The effect is just as if the value of the variable is substituted for the variable name in the code when executed.

.. admonition:: Example

   .. sourcecode:: js

      let message = "What's up, Doc?";
      let n = 17;
      let pi = 3.14159;

      console.log(message);
      console.log(n);
      console.log(pi);

   **Output**

   ::

      What's up, Doc?
      17
      3.14159

In each case, the printed result is the value of the variable. 

Like values, variables also have types. We determine the type of a variable the same way we determine the type of a value, using ``typeof``.

.. admonition:: Example

   .. sourcecode:: js
      
      let message = "What's up, Doc?";
      let n = 17;
      let pi = 3.14159;

      console.log(typeof message);
      console.log(typeof n);
      console.log(typeof pi);

   **Output**

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

    let day = "Thursday";
    console.log(day);
    day = "Friday";
    console.log(day);
    day = 21;
    console.log(day);

A great deal of programming is about having the computer remember things. For example, we might want to keep track of the number of missed calls on your phone. Each time another call is missed, we can arrange to update a variable so that it will always reflect the correct total of missed calls.

.. note:: We only use ``let`` when *declaring* a variable, that is, when we create it. We do not use ``let`` when reassigning the variable to a different value. In fact, doing so will result in an error.

Check Your Understanding
------------------------

.. admonition:: Question

   What is printed when the following code executes?

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
      :linenos:
      
      let a;
      a = 42;
      a = a + 3;
