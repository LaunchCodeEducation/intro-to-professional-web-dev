Objects and Why They Matter
===========================

.. index:: ! object, ! key/value pair, ! key

So far we have learned a lot about arrays, which are data structures that can hold many values.
**Objects** are also data structures that can hold many values. 

Unlike arrays, each value in an object has a name or **key** for reference purposes.
The pairing between a key and its value is called a **key/value pair**. 

.. TODO:: Figure here with clarifying text!

Initializing Objects
--------------------

.. index:: ! object literal

When defining an object, we call the intialization an **object literal**.
We will need three things to create an object: the name of the object, the keys, and their corresponding values.

.. note::

   Object literals use curly braces, ``{}``, to enclose the key/value pairs.

Once we have these three things, we can write an object literal like so:

.. sourcecode:: js
   :linenos:

   let objectName = {key1:value1, key2:value2, key3:value3, ... };

If we have a lot of key/value pairs in our object, we can also put each one on a separate line!

.. sourcecode:: js
   :linenos:

   let objectName = {
       key1: value1,
       key2: value2,
       key3: value3,
       .
       .
       .
   };

.. warning::

   When putting the key/value pairs on a separate line, it is important to pay attention to spaces and tabs!
   Incorrect spacing or tab usage can result in a bug.

When defining an object, keep in mind that the keys can only be valid JavaScript strings.
The values can be any of the data types that we have previously discussed.

.. admonition:: Example

   Let's say that we want to create a small program for a zoo.
   We could create an object for storing the different data points about the animals in a zoo.
   We start with our first tortoise. His name is Pete! He is an 85 year old, 919 lb Galapagos Tortoise, who prefers a diet of veggies.
   Our object literal for all of this important data about Pete would be: 

   .. sourcecode:: js
      :linenos:

      let tortoiseOne = {
          species: "Galapagos Tortoise",
          name: "Pete",
          weight: 919,
          age: 85,
          diet: ["pumpkins", "lettuce", "cabbage"]
      };


Methods and Properties
----------------------

.. index:: ! property

.. index:: method

A **property** of an object is a key/value pair of an object.
The property's name is the key and the property's value is the data assigned to that key.

A **method** performs an action on the object, because it is a property that stores a function.

.. admonition:: Example

   In the case of Pete, our zoo's friendly Galapagos Tortoise, the object ``tortoiseOne`` has several properties for his species, name, weight, age, and diet.
   If we wanted to add a method to our object, we might add a function that returns a helpful statement for the general public.

   .. sourcecode:: js
      :linenos:

      let tortoiseOne = {
          species: "Galapagos Tortoise",
          name: "Pete",
          weight: 919,
          age: 85,
          diet: ["pumpkins", "lettuce", "cabbage"],
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

In the example above on line 8, we see a keyword which is new to us.
Programmers use the ``this`` keyword when they are calling an object's property from within the object itself.
We could use the object's name instead of ``this``, but ``this`` is shorter and easier to read.
We saw it in the method, ``sign``, because we wanted to use the ``name`` and ``species`` properties inside of the ``tortoiseOne`` object.


Check Your Understanding
------------------------

.. admonition:: Question

   Which of the following is NOT a true statement about objects?

   a. Objects can store many values
   b. Objects have properties
   c. Objects have methods
   d. Keys are stored as numbers

.. admonition:: Question

   Which keyword can be used to refer to an object within an object?

   a. ``Object``
   b. ``let``
   c. ``this``