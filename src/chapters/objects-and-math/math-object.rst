The ``Math`` Object
====================

In the previous sections, we learned how to construct, modify, and use objects.

.. admonition:: Example

   .. sourcecode:: js

      let turtle = {
         name = 'Bob',
         color = 'green',
         hungry = true,
         eat: function(){return false},
         move: function(){return true}
      };

      if (turtle.hungry){
         console.log(`${turtle.name} is hungry.`);
         console.log(turtle.name + " eats.");
         turtle.hungry = turtle.eat();
         console.log(`${turtle.name} is happy and ${turtle.color}.`);
      } else {
         console.log(`${turtle.name} is happy and ${turtle.color}.`);
         console.log(turtle.name + " moves.");
         turtle.hungry = turtle.move();
         console.log(`${turtle.name} is hungry.`);
      }

   **Output**
   ::

      Bob is hungry.
      Bob eats.
      Bob is happy and green.

Here, the ``turtle`` object has the properties ``name``, ``color`` and
``hungry``, each of which stores a value. The methods ``eat`` and ``move`` are
functions, which perform specific actions when called.

JavaScript provides several built-in objects, which can be called directly by
the user. One of these is the ``Math`` object, and it allows us to go beyond
the standard mathematical operations (``+, -, *, /``).

``Math`` Properties Are Constants
----------------------------------

If you ever wondered, *I wish I had quick access to the square root of 1/2*,
then JavaScript has your back.

Just like ``turtle`` stores values for a name and color, the ``Math`` object
has 8 defined properties. These represent mathematical *constants*, like the
value for pi (π) or the square root of 1/2.

Instead of defining a variable in our programs to hold "3.14" (or however many
digits of pi a programmer can remember), JavaScript stores the value for us.
To use this value, we do NOT need to create a new object. We just apply dot
notation on the ``Math`` object name.

.. admonition:: Example

   .. sourcecode:: js

      console.log(Math.PI);
      console.log(Math.PI*4);
      console.log(Math.PI + Math.PI);

   **Output**
   ::

      3.141592653589793
      12.566370614359172
      6.283185307179586

By calling ``Math.PI``, JavaScript fills in the value of pi automatically. To
use one of the other constants stored in ``Math``, we replace ``PI`` with the
property name (e.g. ``SQRT1_2`` stores the value for the square root of 1/2).

Recall that for ``turtle``, we can add, remove or change any of the properties
or methods assigned to that object. Renaming ``turtle`` is as simple as
``turtle.name = "Frank";``.

Unlike other objects, the constants defined for ``Math`` are *immutable*.

.. admonition:: Example

   .. sourcecode:: js

      console.log(Math.PI);

      Math.PI = 1234;

      console.log(Math.PI);

   **Output**
   ::

      3.141592653589793
      3.141592653589793

Other ``Math`` Properties
--------------------------

Besides the value of pi, JavaScript provides `7 other constants <https://www.w3schools.com/jsref/jsref_obj_math.asp>`__.
How useful you find each of these depends on the type of project you need to
complete.

More powerful uses of the ``Math`` object involve using *methods*, which we
will examine next.
