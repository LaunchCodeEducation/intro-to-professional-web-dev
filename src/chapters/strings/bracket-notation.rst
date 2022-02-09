Bracket Notation
================

Understanding strings as sequential collections of characters gives us much more than just a mental model of how they are structured. JavaScript provides a rich collection of tools---including special syntax and operations---that allows us to work with strings.

.. index:: ! bracket notation, ! index

.. index:: 
   single: string; index

**Bracket notation** is the special syntax that allows us to access the individual characters that make up a string. To access a character, we use the syntax ``someString[i]``, where ``i`` is the **index** of the character we want to access. String indices are integers representing the position of a character within a given string, and they start at 0. Thus, the first character of a string has index 0, the second has index 1, and so on.

Consider the string ``"JavaScript"``. The ``"J"`` has index 0, the first ``"a"`` has index 1, ``"v"`` has index 2, and so on.

.. figure:: figures/string-indices.png
   :alt: The string "JavaScript" with indices labeled below each letter

   The indices of a string.

An expression of the form ``someString[i]`` gives the character at index ``i``.

.. admonition:: Example

   This program prints out the initials of the person's name.

   .. sourcecode:: js
      :linenos:
   
      let jsCreator = "Brendan Eich";
      let firstInitial = jsCreator[0];
      let lastInitial = jsCreator[8];

      let outputStr = "JavaScript was created by somebody with initials " + 
         firstInitial + "." +
         lastInitial + ".";

      console.log(outputStr);

   **Console Output**

   ::

      JavaScript was created by somebody with initials B.E.

What happens if we try to access an index that doesn't exist, for example -1 or an index larger than the length of the string?

.. admonition:: Try It!

   .. replit:: js
      :linenos:
      :slug: Invalid-String-Indices
   
      let jsCreator = "Brendan Eich";

      console.log(jsCreator[-1]);
      console.log(jsCreator[42]);

.. admonition:: Question

   What does an expression using bracket notation evaluate to when the index is invalid (the index does not correspond to a character in the string)?

Check Your Understanding
------------------------

.. admonition:: Question

   If ``phrase = 'Code for fun'``, then ``phrase[2]`` evaluates to:

   #. ``"o"``
   #. ``"d"``
   #. ``"for"``
   #. ``"fun"``

.. admonition:: Question

   Which of the following returns ``true`` given ``myStr = 'Index'``?  Choose all correct answers.

   #. ``myStr[2] === 'n';``
   #. ``myStr[4] === 'x';``
   #. ``myStr[6] === ' ';``
   #. ``myStr[0] === 'I';``

.. admonition:: Question

   What is printed by the following code?

   .. sourcecode:: js
      :linenos:

      let phrase = "JavaScript rocks!";
      console.log(phrase[phrase.length - 8]);

   #. ``"p"``
   #. ``"i"``
   #. ``"r"``
   #. ``"t"``