Iterating Over Collections
==========================

One of the most common uses of a ``for`` loop is to carry out a task once for each item in a collection. We have learned about two types of collections, strings and arrays. When using a loop with a collection in this way, we say that the loop *iterates over* the collection.

Iterating Over Strings
----------------------

The following example prints each of the characters of the string ``"LaunchCode"`` on a separate line.

.. admonition:: Example

   .. sourcecode:: js
   
      let name = "LaunchCode";

      for (let i = 0; i < name.length; i++) {
         console.log(name[i]);
      }

   **Output**

   ::

      L
      a
      u
      n
      c
      h
      C
      o
      d
      e

Since ``name.length`` is 10, the loop executes once each for the values of ``i`` from 0 to 9. The loop body, ``console.log(name[i]);``, will print ``name[i]`` each time. In each case, ``name[i]`` is one of the characters of ``name``.

.. admonition:: Try It!

   Write a program that prints each character of your name on a different line.

   .. sourcecode:: js
   
      // create a string variable containing your name

      // write a for loop that prints each character in your name on a different line

   `Practice looping over strings at repl.it <https://repl.it/@launchcode/for-Loop-Practice-With-Strings>`_

Iterating Over Arrays
---------------------

The following example prints each of the programming languages in the array ``languages`` on a separate line.

.. admonition:: Example

   .. sourcecode:: js
   
      let languages = ["JS", "Java", "C#", "Python"];

      for (let i = 0; i < languages.length; i++) {
         console.log(languages[i]);
      }

   **Output**

   ::

      JS
      Java
      C#
      Python

Similar to the string example, this loop executes 4 times because ``launguages.length`` is 4. For each iteration, ``languages[i]`` is one of the items in the array and the given language is printed.

.. admonition:: Try It!

   Write a program that prints the name of each member of your family on a different line.

   .. sourcecode:: js
   
      // create an array variable containing the names

      // write a for loop that prints each name on a different line

   `Practice looping over arrays at repl.it <https://repl.it/@launchcode/for-Loop-Practice-With-Arrays>`_
