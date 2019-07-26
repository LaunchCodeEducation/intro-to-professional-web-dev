.. _inheritance:

Inheritance
===========

.. index:: ! inheritance, ! object-oriented programming

**Object-oriented programming** is a type of software design where the codebase is organized around `objects` and `classes`.
Objects contain the functions and central logic of a program.

Object-oriented programming stands on top of four principles: abstraction, polymorphism, encapsulation, and inheritance.
We will dive into inheritance now and work with the other three principles in Unit Two of this class.

**Inheritance** refers to the ability of one class to acquire properties and methods from another.

Think of it this way, in the animal kingdom, a `species` is a unique entity that inherits traits from its `genus`. The `genus` also has unique properties, but inherits traits from its `family`.
For example, a tiger and a housecat are members of two different species, however, they share similar traits such as retractable claws.
The two cats inherited their similar traits from their shared family, `felidae`.

Using inheritance in programming, we can create a structure of classes that inherit properties and methods from other classes.

If we wanted to program classes for our tiger and housecat, we would create a felidae class for the family.
We would then create two classes for the panthera genus and the felis genus. We would create classes for the tiger and house cat species as well.
The species classes would inherit properties and methods from the genus classes and the genus classes would inherit properties and methods from the family class.

.. figure:: figures/inheritance.png
   :alt: Figure showing that panthera and felis inherit from felidae, tiger inherits from panthera, and housecat inherits from felis.

.. index:: ! parent class, ! child class

The classes inheriting properties and methods are **child classes**, and the classes passing down properties and methods are **parent classes**.

``extends``
-----------

When designating a class as the child class of another in JavaScript, we use the ``extends`` keyword.
We also must use the ``super()`` constructor to get the properties and methods needed from the parent class.

.. sourcecode:: js
   :linenos:

   class ChildClass extends ParentClass {
      constructor () {
         super();
         // properties
      }
   }

In the case of a tiger, tigers have stripes, but they also have loud roars.
Their ability to roar loudly is a trait they share with other members of the `panthera` genus.
Tigers also got their retractable claws from the `felidae` family.

.. admonition:: Example

   .. replit:: js
      :slug: InheritanceTryIt
      :linenos:

      class Felidae {
         constructor() {
            this.claws = "retractable";
         }
      }

      class Panthera extends Felidae {
         constructor() {
            super();
            this.roar = "loud"
         }
      }

      class Tiger extends Panthera {
         constructor() {
            super();
            this.hasStripes = "true";
         }
      }

      let tigger = new Tiger();

      console.log(tigger);

   When creating the classes for our tiger, we can use the ``extends`` keyword to set up ``Tiger`` as the child class of ``Panthera``.
   The ``Tiger`` class then inherits the property, ``roar``, from the ``Panthera`` class and has an additional property, ``hasStripes``.

.. note::

   The ``extends`` keyword is not supported in Internet Explorer.

Check Your Understanding
------------------------

.. admonition:: Question

   If you had to create classes for a *wolf*, the *canis* genus, and the
   *carnivora* order, which statement is TRUE about the order of inheritance?

   a. ``Wolf`` and ``Canis`` are parent classes to ``Carnivora``.
   b. ``Wolf`` is a child class of ``Canis`` and a parent class to ``Carnivora``.
   c. ``Wolf`` is child class of ``Canis``, and ``Canis`` is a child class of ``Carnivora``.
   d. ``Wolf`` is child class of ``Canis``, and ``Canis`` is a parent class of ``Carnivora``.
