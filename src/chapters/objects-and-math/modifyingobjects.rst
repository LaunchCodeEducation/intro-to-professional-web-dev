Working with Objects
====================

Accessing Properties
--------------------

When using objects, programmers oftentimes want to retrieve or change the value of one of the properties.
To access the value of a property, you will need the object's name and the key of the property.

Programmers have two ways to access the value of property:

1. Bracket syntax
2. Dot notation.

Bracket Syntax
^^^^^^^^^^^^^^

To access a property with bracket syntax, the code looks like: ``object["key"]``.

Dot Notation
^^^^^^^^^^^^

To access a property with dot notation, the code looks like: ``object.key``. Notice that the key is no longer surrounded by quotes. However, keys are still strings.

.. note::

   Recall, the only restraint in naming a key is that it has to be a valid JavaScript string.
   Since a key could potentially have a space in it, bracket syntax would be the only way to access the value in that property because of the quotes.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let tortoiseOne = {
          species: "Galapagos Tortoise",
          name: "Pete",
          weight: 919,
          age: 85,
          diet: ["pumpkins", "lettuce", "cabbage"]
      };

      console.log(tortoiseOne["name"]);
      console.log(tortoiseOne.name);

   **Console Output**

   ::

      Pete
      Pete

Modifying Properties
--------------------

A programmer can modify the value of a property by using either notation style.

.. warning::

   Recall that mutability means that a data structure can be modified without making a copy of that structure.
   Objects are mutable data structures.
   When you change the value of a property, the original object is modified and a copy is NOT made.

.. admonition:: Example

   In our zoo software, we may want to update Pete's weight as he has gained 10 lbs.
   We will use both bracket syntax and dot notation for our software, but that is not a requirement!
   Feel free to use whichever one suits your needs and is easiest for you and your colleagues to read.

   .. sourcecode:: js
      :linenos:

      let tortoiseOne = {
          species: "Galapagos Tortoise",
          name: "Pete",
          weight: 919,
          age: 85,
          diet: ["pumpkins", "lettuce", "cabbage"]
      };

      console.log(tortoiseOne.weight);

      newWeight = tortoiseOne.weight + 10;

      tortoiseOne["weight"] = newWeight;

      console.log(tortoiseOne["weight"]);

   **Console Output**

   ::

      919
      929

.. _add-new-object-properties:

Add New Key/Value Pairs
^^^^^^^^^^^^^^^^^^^^^^^^

After declaring and initializing an object, we can add new properties at any
time by using bracket syntax:

.. sourcecode:: js

   objectName["new-key"] = propertyValue;

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let tortoiseTwo = {
          species: "Galapagos Tortoise",
          name: "Pete",
          weight: 919
      };

      console.log(tortoiseTwo);

      tortoiseTwo["age"] = 120;
      tortoiseTwo["speed"] = 'Faster than the hare.'

      console.log(tortoiseTwo);
      console.log(tortoiseTwo.age);

   **Console Output**

   ::

      { species: 'Galapagos Tortoise', name: 'Pete', weight: 919 }
      { species: 'Galapagos Tortoise',
         name: 'Pete',
         weight: 919,
         age: 120,
         speed: 'Faster than the hare.' }
      120

Check Your Understanding
------------------------

All of the questions below refer to an object called ``giraffe``.

.. sourcecode:: js
   :linenos:

   let giraffe = {
     species: "Reticulated Giraffe",
     name: "Cynthia",
     weight: 1500,
     age: 15,
     diet: "leaves"
   };

.. admonition:: Question

   We want to add a method after the ``diet`` property for easily increasing Cynthia's age on her birthday.
   Which of the following is missing from our method? You can select MORE than one.

   ``birthday: function () {age = age + 1;}``

   a. ``return``
   b. ``this``
   c. ``diet``
   d. a comma

.. admonition:: Question

   Could we use bracket syntax, dot notation, or both to access the properties of ``giraffe``?
