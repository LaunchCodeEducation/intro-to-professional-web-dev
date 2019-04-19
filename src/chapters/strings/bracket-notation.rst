Bracket Notation
================

Understanding strings as sequential collections of characters gives us much more than just a mental model of how they are structured. JavaScript provides a rich collection of tools---including special syntax and operations---that allows us to work with strings.

.. index:: ! bracket notation

.. index:: 
   single: string; index

**Bracket notation** is the special syntax that allows us to access the individual characters that make up a string. To access a character, we use the syntax ``someString[i]``, where ``i`` is the **index** of the character we want to access. String indices are integers representing the position of a character within a given string, and they start at 0. Thus, the first character of a string has index 0, the second has index 1, and so on.

Consider the string ``"JavaScript"``. The ``"J"`` has index 0, the first ``"a"`` has index 1, ``"v"`` has index 2, and so on.

.. figure:: figures/string-indices.png
   :alt: The string "JavaScript" with indices labeled below each letter

   The indices of a string.

An expression of the form ``someString[i]`` evaluates to the character at index ``i``.

.. admonition:: Example

   Print out the initials of a person's name.

   .. sourcecode:: js
   
      let jsCreator = "Brendan Eich";
      let outputStr = "JavaScript was created by somebody with initials " + 
         jsCreator[0] + "." +
         jsCreator[8] + ".";

      console.log(outputStr);

   **Output**

   ::

      JavaScript was created by somebody with initials B.E.

What happens if we try to access an index that doesn't exist, for example -1 or an index larger than the length of the string?

.. admonition:: Try It!

   .. sourcecode:: js
   
      let jsCreator = "Brendan Eich";

      console.log(jsCreator[-1]);
      console.log(jsCreator[42]);

   `Run this program at repl.it <https://repl.it/@launchcode/Invalid-String-Indices>`_

.. admonition:: Question

   What does an expression using bracket notation evaluate to when the index is invalid (that is, does not correspond to a character in the string)?
