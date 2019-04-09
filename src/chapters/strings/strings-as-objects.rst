Strings as Objects
==================

Beyond bracket notation, there are many other tools we can use to work with strings. Talking about these tools requires some new terminology.

Object Terminology
------------------

.. index:: object, property, method

An **object** is collection of related data and operations. We have already encountered one object, the built-in object ``console``, which we use to output messages.

.. admonition:: Example

   .. sourcecode:: js

      console.log(typeof console);

   **Output**

   ::
   
      object

JavaScript reports that the type of ``console`` is indeed ``object``. An operation that can be carried out on an object is known as a **method**. 

You can think of methods as functions that "belong to" an object. In other words, they only make sense when used in conjunction with an object. We can call ``console.log()``, but we may not use ``log()`` on its own.

A piece of data that associated with an object is known as a **property**. While we have not had a reason to use them, the ``console`` object has ``name`` and ``length`` properties. 

You can think of properties as variables that "belong to" an object. They are accessed using **dot notation**, which dictates that we use the object name, followed by a ``.``, followed by the property name.

.. admonition:: Example

   .. sourcecode:: js
   
      console.log("Value of the name property:", console.name);
      console.log("Value of the length property:", console.length);

   **Output**

   ::

      Value of the name property: console
      Value of the length property: 0

Precisely what these properties of the built-in object ``console`` represent is not so important as the fact that they are there. Properties store data related to an object.

As with methods, it does not make sense to refer to a property without also referring to the associated object. Referencing ``name`` by itself in code *does not* give you the value of ``console.name``.

Properties and methods can be used in conjunction with a specific object, as we did with ``console``, or with a variable containing an object.

We will learn quite a bit more about objects in this course, including how to use objects to create your own custom data types. This powerful JavaScript features allows us to bundle up data and functionality in useful, modular ways.

Strings Are Objects
-------------------

In JavaScript, strings are objects. 

The fact that strings are objects means that they have associated data and operations, or properties and methods as we will call them from now on. 

.. index::
   single: ! string; length

Every string that we work with will have the same properties and methods. The most useful string property is named ``length``, and it tells us how many characters are in a string.

.. admonition:: Example

   .. sourcecode:: js
   
      let firstName = "Grace";
      let lastName = "Hopper";

      console.log(firstName, "has", firstName.length, "characters");
      console.log(lastName, "has", lastName.length, "characters");

   **Output**

   ::

      Grace has 5 characters
      Hopper has 6 characters

Every string has a ``length`` property, which is an integer.

The ``length`` property is the only string property that we will use, but there are many useful string methods. We will explore these in depth in the section :ref:`string-methods`, but let's look at one now to give you an idea of what's ahead.

The ``toLowerCase()`` string method returns the value of its string in all lowercase letters. Since it is a method, we must precede it with a specific string in order to use it.

.. admonition:: Example

   .. sourcecode:: js
   
      let nonprofit = "LaunchCode";

      console.log(nonprofit.toLowerCase());
      console.log(nonprofit);

   **Output**

   ::

      launchcode
      LaunchCode

Notice that ``toLowerCase()`` does not alter the string itself, but instead *returns* the result of converting the string to all lowercase characters. In fact, it is not possible to alter the characters within a string, as we will now see.
