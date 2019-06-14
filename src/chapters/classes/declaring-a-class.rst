Declaring and Calling a Class
==============================

Creating a Class
-----------------

Just like the ``function`` keyword defines a new function, the keyword for
defining a new class is ``class``. By convention, class names start with
capital letters to distinguish them from JavaScript function and variable names
(e.g. ``MyClass`` vs. ``myFunction``).

Remember that classes are blueprints for building multiple objects of the same
type. The general format for declaring a class is:

.. sourcecode:: js
   :linenos:

   class ClassName {
      constructor(parameters) {
         //assign properties
      }
      //define methods
   }

.. index:: ! constructor

Note how defining a class differs from defining a function:

#. The keyword ``constructor``. This is a special method for creating objects
   of the same type, and it assigns the key/value pairs.
#. Parameters are passed into the ``constructor`` method rather than the
   ``class`` declaration.

As an example, let's set up an ``Astronaut`` class to help us store data about
our animal crew.

Assigning Properties
^^^^^^^^^^^^^^^^^^^^^

Each animal in our crew has a ``name``, ``age``, and ``mass``, and we assign
these properties in ``constructor`` as follows:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      constructor(name, age, mass) {
         this.name = name,
         this.age = age,
         this.mass = mass
      }
   }

The ``this`` keyword defines a key/value pair, where the text attached to
``this`` becomes the key, and the value follows the equal sign (``this.key =
value``).

``constructor`` uses the three ``this`` statements (``this.name = name``, etc.)
to achieve the same result as the object declaration
``let objectName = {name: someString, age: someNumber, mass: someMass}``. Each
time the ``Astronaut`` class is called, ``constructor`` builds an object with
the SAME set of keys, but it assigns different values to the keys based on the
arguments.

.. admonition:: Note

   Each class requires one and only one ``constructor``. Including more than one
   results in a syntax error. If ``constructor`` is left out of a class declaration,
   JavaScript adds an empty one automatically---``constructor () {}``.

Calling a New Class Object
---------------------------

To create an object from a class, we use the keyword ``new``. The syntax is:

::

   let objectName = new ClassName(arguments).

``new`` creates an **instance** (or example) of the class. Each object
generated shares the same set of keys as every other object made from the
class.

.. admonition:: Example

   Let's create objects for two of our crew members - Fox and Hippo.

   .. sourcecode:: js
      :linenos:

      class Astronaut {
         constructor(name,age,mass){
            this.name = name,
            this.age = age,
            this.mass = mass
         }
      }

      let fox = new Astronaut('Fox', 7, 12);
      let hippo = new Astronaut('Hippo', 25, 1500);

      console.log(typeof hippo, typeof fox);

      console.log(hippo, fox);

   **Console Output**

   ::

      object object

      Astronaut { name: 'Hippo', age: 25, mass: 1500 }
      Astronaut { name: 'Fox', age: 7, mass: 12 }

Line 12 verifies that both ``fox`` and ``hippo`` are objects. The output from
line 14 shows that ``fox`` and ``hippo`` are both the same type of object
(``Astronaut``). The two share the same *keys*, but they have different
values assigned to those keys.
