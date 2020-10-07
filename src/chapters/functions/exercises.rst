Exercises: Functions
=====================

To become good at solving problems with code you need to be able to break large
problems into small ones. Usually, these smaller problems will take the form of
functions that are used to solve the larger problem. Therefore, to become good
at solving problems you need to become good at writing functions. And to master
functions, you need to write a *lot* of them.

These exercises ask you to write lots of relatively small functions, which
combine to form larger, more complicated ones.

At the end, you will be able to create strings of shapes, like this nifty
diamond:

::

       #
      ###
     #####
    #######
   #########
   #########
    #######
     #####
      ###
       #

There is no starter code for these exercises, so create a new Node.js project
at `repl.it <https://repl.it/>`_ to get started.

Rectangles
----------

#. Write a function ``makeLine(size)`` that returns a line with exactly ``size``
   hashes.

   .. sourcecode:: js

      console.log(makeLine(5));

   **Console Output**

   ::

      #####

#. Write a function ``makeSquare(size)`` that returns an ``size`` by ``size``
   square of hashes. Use your ``makeLine`` function to do this.

   .. sourcecode:: js

      console.log(makeSquare(5));

   **Console Output**

   ::

      #####
      #####
      #####
      #####
      #####

   .. tip::

      The newline character, ``\n``, will be helpful to you.

   .. warning::

      For this and all other functions in these exercises, make sure you do NOT have a newline character at the end of your string. Not only will ``console.log`` add a newline there for you, but having an extra newline at the end will make life harder for you toward the end of the exercises.


#. Write a function ``makeRectangle(width, height)`` that returns a
   rectangle with the given width and height. Use your ``makeLine`` function to
   do this.

   .. sourcecode:: js

      console.log(makeRectangle(5, 3));

   **Console Output**

   ::

      #####
      #####
      #####

#. Now, go back and rewrite ``makeSquare`` to use ``makeRectangle``.

Triangles
----------

#. Write a function ``makeDownwardStairs(height)`` that prints the staircase
   pattern shown below, with the given height. Use your ``makeLine`` function
   to do this.

   .. sourcecode:: js

      console.log(makeDownwardStairs(5));

   **Console Output**

   ::

      #
      ##
      ###
      ####
      #####

2. Write a function ``makeSpaceLine(numSpaces, numChars)`` that returns a line
   with exactly the specified number of spaces, followed by the
   specified number of hashes, followed again by ``numSpaces`` more spaces.

   .. sourcecode:: js

      console.log(makeSpaceLine(3, 5));

   **Console Output**

   ::

      ___#####___

   .. note:: We have inserted underscores to represent spaces, so they are visible in the output. Don't do this in your code.

#. Write a function ``makeIsoscelesTriangle(height)`` that returns a triangle
   of the given height.

   .. sourcecode:: js

      console.log(makeIsoscelesTriangle(5));

   **Console Output**

   ::

          #
         ###
        #####
       #######
      #########

   .. tip:: Consider the top line of the triangle to be level 0, the next to be line 1, and so on. Then line ``i`` is a space-line with ``height - i - 1`` spaces and ``2 * i + 1`` hashes.

Diamonds
---------

#. Write a function ``makeDiamond(height)`` that returns a diamond where the
   triangle formed by the *top* portion has the given height.

   .. sourcecode:: js

      console.log(makeDiamond(5));

   **Console Output**

   ::

          #
         ###
        #####
       #######
      #########
      #########
       #######
        #####
         ###
          #

   .. tip::

      Consider what happens if you create a triangle and reverse it using
      :ref:`our reverse function <reverse_func>`.

Bonus Mission
--------------

Refactor your functions so that they take a single character as a parameter,
and draw the shapes with that character instead of always using ``'#'``. Make
the new parameter optional, with default value ``'#'``.
