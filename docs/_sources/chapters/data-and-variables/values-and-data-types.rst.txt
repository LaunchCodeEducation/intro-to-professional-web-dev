Values and Data Types
=====================

.. index:: ! value

Data can be stored in a program in a variety of ways. The most basic unit of data is a value.

A **value** is a specific piece of data, such as a word or a number. Some examples are ``5``, ``5.2``, and ``"Hello, World!"``.

.. index:: ! data type, ! number, ! string, ! type 

Each value belongs to a category called a **data type**. We will see many different data types throughout the course, the first two of which are the **number** and **string** types. Numeric values such as ``4`` and ``3.3`` are a numbers. Sequences of characters encolosed in quotes, such as ``"Hello, World!"``, are strings, so-called because they contain a string of letters. Strings must be enclosed in either single or double quotes. 

.. index:: ! integer, ! float

.. index:: ! typeof

If you are not sure what data type a value falls into, precede the value with ``typeof``.

.. admonition:: Example

   .. sourcecode:: js

      console.log(typeof "Hello, World!");
      console.log(typeof 17);
      console.log(typeof 3.14);

   **Output**

   ::

      string
      number
      number

Not surprisingly, JavaScript reports that the data type of ``"Helo, World!"`` is ``string``, while the data type of both ``17`` and ``3.14`` is ``number``. Note that some JavaScript environments may print types names and strings with single quotes around them, as in ``'string'``, ``'number'``, and ``'hello'``.

.. index:: expression, returns

.. note:: Notice that ``console.log(typeof "Hello, World!");`` prints out ``"Hello, World!`` to the console. The ``typeof`` keyword is not printed to the console because the statement ``typeof "Hellow, World"!`` is an **expression**. Briefly, expressions are code segments that are reduced to a value. We will learn more about expressions soon.

   We say that an expression **returns** a value. That is, ``typeof "Hello, World!"`` returns the value ``string``.

.. index:: operator

.. note::

   ``typeof`` is a JavaScript entity known as an **operator**. It is similar to a function in that it carries out some kind of action, though the syntax is different from that of functions (notice using ``typeof`` does not require parenthses).
   
   We will more about operators in upcoming sections.

There are data types other than string and number, including object and function, which we will learn about in future chapters.

More On Strings
---------------

What about values like ``"17"`` and ``"3.2"``? They look like numbers, but they are in quotation marks like strings.

Run the following code to find out.

.. admonition:: Try It!

   .. sourcecode:: js

      console.log(typeof "17");
      console.log(typeof "3.2");

   `Run this program at repl.it <https://repl.it/@launchcode/Data-Types>`_

.. admonition:: Question

   What is the data type of the values ``"17"`` and ``"3.2"``?

Strings in JavaScript can be enclosed in either single quotes (``'``) or double
quotes (``"``).

.. admonition:: Example

   .. sourcecode:: js

      console.log(typeof 'This is a string');
      console.log(typeof "And so is this");

   **Output**

   ::

      string
      string

Double-quoted strings can contain single quotes inside them, as in ``"Bruce's beard"``, and single quoted strings can have double quotes inside them, as in ``'The knights who say "Ni!"'``.

JavaScript doesn't care whether you use single or double quotes to surround your strings. Once it has parsed the text of your program or command, the way it stores the value is identical in all cases, and the surrounding quotes are not part of the value.

.. warning:: 

   If a string contains a single quote (such as ``"Bruce's beard"``) then surrounding it with single quotes gives unexpected results. 

   What happens if you run the following piece of code? 

   ::
   
      console.log('Bruce's beard');


More On Numbers
---------------

When you type a large integer value, you might be tempted to use commas between groups of three digits, as in ``42,000``. This is not a legal integer in JavaScript, but it does mean something else, which is legal:

.. admonition:: Example

   .. sourcecode:: js

      console.log(42000);
      console.log(42,000);

   **Output**

   ::

      42000
      42 0

Well, that's not what we expected at all! Because of the comma, JavaScript chose to treat ``42,000`` as a *pair* of values. In fact, the ``console.log()`` function can print any number of values as long as you separate them by commas. Notice that the values are separated by spaces when they are displayed.

.. admonition:: Example

   .. sourcecode:: js

      console.log(42, 17, 56, 34, 11, 4.35, 32);
      console.log(3.4, "hello", 45);

   **Output**

   ::

      42 17 56 34 11 4.35 32
      3.4 'hello' 45

Remember not to put commas or spaces in your integers, no matter how big they are. Also revisit what we said in the chapter :ref:`how-programs-work`: formal languages are strict, the notation is concise, and even the smallest change might mean something quite different from what you intend.

Type Systems
------------

.. index:: ! type system

Every programming language has a **type system**, which is the set of rules that determine how the languages deals with data of different types. In particular, how values are divided up into different data types is one characteristic of a type system.

In many programming languages, integers and floats are considered to be different data types. For example, in Python ``42`` is of the ``int`` data type, while ``42.0`` is of the ``float`` data type.

.. note:: While JavaScript does not distinguish between floats and integers, at times we may wish to do so in our programs. For example, consider an inventory-tracking program that stores items along with the number of each item in stock. It would not make sense for there to be float quantities of items (for example, 3.5 shirts), so the program may wish to only allow quantities to be stored as integers.

When discussing the differences between programming languages, the details of type systems are one of the main factors that programmers consider. There are other aspects of type systems beyond just how values are categorized. We will explore these in future lessons.

Check Your Understanding
------------------------

.. admonition:: Question

   Which of these is *not* a data type in JavaScript?

   #. number
   #. string
   #. letter
   #. object
