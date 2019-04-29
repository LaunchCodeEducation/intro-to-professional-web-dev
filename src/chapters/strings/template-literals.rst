Template Literals
=================

.. index:: ! template literal

**Template literals** allow for the automatic insertion of expressions (including variables) into strings.

While normal strings are enclosed in single or double quotes (``'`` or ``"``), template literals are encolsed in back-tick characters, `````. Within a template literal, any expression surrounded by ``${ }`` will be evaluated, with the resulting value included in the string.

.. admonition:: Example

   Template literals allow for variables and other expressions to be directly included in strings.

   .. sourcecode:: js
   
      let name = "Jack";
      let currentAge = 9;

      console.log(`Next year, ${name} will be ${currentAge + 1}`);

   **Output**

   ::

      Next year, Jack will be 10

Using string concatenation to achieve the same output can get cumbersome:

.. sourcecode:: js

   console.log("Next year, " + name + " will be " + (currentAge + 1));

In addition to allowing us to include data in strings in a cleaner, more readable way, template literals also allow us to easily create multi-line strings without using string concatenation or special characters.

.. admonition:: Example

   .. sourcecode:: js
   
      let poem = `The mind chases happiness.
      The heart creates happiness.
      The soul is happiness
      And it spreads happiness
      All-where.

      – Sri Chinmoy`;

      console.log(poem);

   **Output**

   ::

      The mind chases happiness.
      The heart creates happiness.
      The soul is happiness
      And it spreads happiness
      All-where.

      – Sri Chinmoy

.. note:: The ECMAScript specifications define the standard for JavaScript. The 6th edition, known as ES2015, added template literals. Not only are template literals relatively new to JavaScript, but you may enounter environments---such as older web browsers---where they are not supported.


Check Your Understanding
------------------------

.. admonition:: Question

   Mad Libs are games where one player asks the group to supply random words (e.g. "Give me a verb," or, "I need a color"). The words are substituted into blanks within a story, which is then read for everyone's amusement. In elementary school classrooms, giggles and hilarity often ensue. TRY IT! Refactor the following code to replace the awkward string concatenation with template literals. Be sure to add your own choices for the variables. (`Repl.it <https://repl.it/@launchcode/String-Mad-Lib>`_)

   .. sourcecode:: javascript

      let pluralNoun = ;
      let name = ;
      let verb = ;
      let adjective = ;
      let color = ;
      
      console.log("JavaScript provides a "+ color +" collection of tools — including " + adjective + " syntax and " + pluralNoun + " — that allows "+ name +" to "+ verb +" with strings.")
