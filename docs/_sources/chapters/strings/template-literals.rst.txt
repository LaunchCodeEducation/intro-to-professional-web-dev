Template Literals
=================

.. index:: ! template literal

The ECMAScript specifications define the standard for JavaScript. The 6th edition, known as ES2015, added **template literals**, which allow for the automatic insertion of expressions (including variables) into strings.

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

To achieve the same output with string concatenation would have required concatenation, which can get cumbersome:

.. sourcecode:: js

   console.log("Next year, " + name + " will be " + (currentAge + 1));

In addition to allowing us to include data in strings in a cleaner, more readable way, template literals also allow us to easily create milti-line strings without using string concatenation.

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
