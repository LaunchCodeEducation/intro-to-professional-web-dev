Objects and Why They Matter
===========================

.. index:: ! object, ! key/value pair

So far we have learned a lot about arrays, which are data structures that can hold many values.
**Objects** are also data structures that can hold many values. 

Unlike arrays, each value in objects has a name or key for reference purposes.
The pairing between a key and its value is called a **key/value pair**.

Initializing Objects
--------------------

.. index:: ! object literal

An object initialization is called an **object literal**.
We will need three things to create an object: the name of the object, the keys, and their corresponding values.

Once we have these three things, we can write an object literal like so:

.. sourcecode:: js

   var objectName = {key1: value1, key2:value2, key3:value3, ....};

If the object is quite large, you can also put the key/value pairs on a separate line!

.. sourcecode:: js

   var objectName = {
       key1: value1,
       key2: value2,
       key3: value3,
       .
       .
       .
   };

.. warning::

   When putting the key/value pairs on a separate line, it is important to pay attention to spaces and tabs!

When defining an object, keep in mind that the keys can only be valid JavaScript strings.
The values can be any of the data types that we have previously discussed.

.. admonition:: Example

   Let's say that we want to create a small program for a zoo.
   We could create an object for storing the different data points about the animals in a zoo.
   We start with our first tortoise. His name is Pete! He is an 85 year old, 919 lb Galapagos Tortoise, who prefers a diet of veggies.
   Our object literal for all of this important data about Pete would be: 

   .. sourcecode:: js

      var tortoiseOne = {
          species:"Galapagos Tortoise",
          name:"Pete",
          weight: 919,
          age: 85,
          diet:"veggies"
      };


Methods and Properties
----------------------

.. index:: ! property, ! method

A **property** of an object is a key/value pair of an object.
The property's name is the key and the property's value is the value assigned to that key.

A **method** performs an action on the object, because it is a property that stores a function.

.. admonition:: Example

   In the case of Pete, our zoo's friendly Galapagos Tortoise, the object ``tortoiseOne`` has several properties for his species, name, weight, age, and diet.
   If we wanted to add a method to our object, we might add a function that returns a helpful statement for the general public.

   .. sourcecode:: js

      var tortoiseOne = {
          species:"Galapagos Tortoise",
          name:"Pete",
          weight: 919,
          age: 85,
          diet:"veggies",
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

In the example above, we saw a new keyword that we haven't seen before.
``this`` is a keyword that programmers use when they need to call upon a property in the object in a method for that same object.

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
   b. ``var``
   c. ``this``