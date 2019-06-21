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

Note the keyword ``constructor``. This is a special method for creating objects
of the same type, and it assigns the key/value pairs. Parameters are passed
into ``constructor`` rather than the ``class`` declaration.

Assigning Properties
^^^^^^^^^^^^^^^^^^^^

Let's set up an ``Astronaut`` class to help us store data about our animal
crew. Each animal has a ``name``, ``age``, and ``mass``, and we assign these
properties in ``constructor`` as follows:

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

   Each class requires *one* ``constructor``. Including more than one
   ``constructor`` results in a syntax error. If ``constructor`` is left out of
   a class declaration, JavaScript adds an empty ``constructor () {}``
   automatically.

Creating a New Class Object
----------------------------

To create an object from a class, we use the keyword ``new``. The syntax is:

::

   let objectName = new ClassName(arguments);

``new`` creates an **instance** of the class, which means that the object
generated shares the same set of keys as every other object made from the
class.

.. admonition:: Example

   Let's create objects for two of our crew members: Fox and Hippo.

   .. sourcecode:: js
      :linenos:

      class Astronaut {
         constructor(name, age, mass){
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

In lines 9 and 10, we call the ``Astronaut`` class twice and pass in different
sets of arguments, creating the ``fox`` and ``hippo`` objects.

The output of line 14 shows that ``fox`` and ``hippo`` are both the same
*type* of object (``Astronaut``). The two share the same *keys*, but they have
different values assigned to those keys.

   Objects created with the same class are NOT the same. They share an overall
   structure (keys), but the values differ.

After creating an ``Astronaut`` object, we can access, modify, or add new
key/value pairs as described in the
:ref:`Objects and Math chapter <objects-chapter>`.

.. admonition:: Try It

   Play around with modifying and adding properties inside and outside of the
   ``class`` declaration.

   .. replit:: js
      :slug: classExamples01
      :linenos:

      class Astronaut {
         constructor(name, age, mass){
            this.name = name,
            this.age = age,
            this.mass = mass
         }
      }

      let fox = new Astronaut('Fox', 7, 12);

      console.log(fox);
      console.log(fox.age, fox.color);

      fox.age = 9;
      fox.color = 'red';

      console.log(fox);
      console.log(fox.age, fox.color);

   **Console Output**

   ::

      Astronaut { name: 'Fox', age: 7, mass: 12 }
      7 undefined
      Astronaut { name: 'Fox', age: 9, mass: 12, color: 'red' }
      9 'red'

Attempting to print ``fox.color`` in line 12 returns ``undefined``, since that
property is not included in the ``Astronaut`` class. Line 15 adds the ``color``
property to the ``fox`` object, but this change will not affect any other
objects created with ``Astronaut``.

Setting Default Values
^^^^^^^^^^^^^^^^^^^^^^^

What happens if we create a new ``Astronaut`` without passing in all of the
required arguments?

.. admonition:: Try It!

   .. replit:: js
      :slug: classExamples02
      :linenos:

      class Astronaut {
         constructor(name, age, mass){
            this.name = name,
            this.age = age,
            this.mass = mass
         }
      }

      let tortoise = new Astronaut('Speedy', 120);

      console.log(tortoise.name, tortoise.age, tortoise.mass);

To avoid issues with missing arguments, we can set a *default* value for a
parameter as follows:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      constructor(name, age, mass = 54){
         this.name = name,
         this.age = age,
         this.mass = mass
      }
   }

Now if we call ``Astronaut`` but do not specify a mass value, the constructor
automatically assigns a value of ``54``. If an argument is included for
``mass``, then the default value is ignored.

TRY IT! Return to the repl.it in the example above and set default values for
one or more of the parameters.

Check Your Understanding
-------------------------

The questions below refer to a class called ``Car``.

.. sourcecode:: js
   :linenos:

   class Car {
      constructor(make, model, year, color, mpg){
         this.make = make,
         this.model = model,
         this.year = year,
         this.color = color,
         this.mpg = mpg
      }
   }

.. admonition:: Question

   If we call the class with ``let myCar = new Car('Chevy', 'Astro', 1985,
   'gray', 20)``, what is output by ``console.log(typeof myCar.year)``?

   a. object
   b. string
   c. function
   d. number
   e. property

.. admonition:: Question

   If we call the class with ``let myCar = new Car('Tesla', 'Model S', 2019)``,
   what is output by ``console.log(myCar)``?

   a. Car {make: 'Tesla', model: 'Model S', year: 2019, color: undefined, mpg: undefined }
   b. Car {make: 'Tesla', model: 'Model S', year: 2019, color: '', mpg: '' }
   c. Car {make: 'Tesla', model: 'Model S', year: 2019 }
