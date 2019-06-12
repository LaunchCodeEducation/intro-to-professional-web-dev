What Are Classes?
==================

Recall that :ref:`objects <objects-intro>` are data structures that hold many
values, which consist of *properties* and *methods*.

**Classes** extend this idea by providing a template for building multiple
examples of a particular object.

An Astronaut Object
--------------------

Let's revisit the animal astronauts from previous exercises. If we create an
object to hold an astronaut's data, it might look something like:

.. sourcecode:: js
   :linenos:

   let fox = {
      name: 'Fox',
      age: 7,
      mass: 12,
      catchPhrase: function(repeats) {
         let phrase = 'LaunchCode';
         for (let i = 0; i < repeats; i++) {
            phrase += ' Rocks';
         }
         return phrase;
   }

The ``fox`` object now contains all the data for the astronaut named ``'Fox'``.

Of course, we have multiple astronauts on our team. To store data for each one,
we would need to copy the structure for ``fox`` multiple times and then change
the values to suit each crew member. This is inefficient and repetitive. As
expected, JavaScript provides us a better way to create multiple, similar
objects.

To create many objects of the same type, we start by defining a **class**,
which allows us to build the general structure for an object. We can then
reuse that structure to build multiple objects. These objects will have the
same set of *keys*, but the values assigned to each key will vary.

   [TODO: Add a figure showing class & objects]
