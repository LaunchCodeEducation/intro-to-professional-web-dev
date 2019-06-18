Inheritance
===========

.. index:: ! inheritance, ! object-oriented programming

**Object-oriented programming** is a type of software design where the codebase is organized around objects and classes.
Objects contain the functions and central logic of a program.

Object-oriented programming stands on top of four principles: abstraction, polymorphism, encapsulation, and inheritance.
We will dive into inheritance now and work with the other three principles later in Unit Two of this class.

**Inheritance** refers to the ability of one class to inherit properties and methods from another.

Think of it this way, in the animal kingdom, a species is a unique entity that inherits traits from its genus. The genus also has unique properties, but inherits traits from its family.
For example, a tiger and a housecat are members of two different species, however, they share similar traits such as retractable claws.
The similar traits they share, the two cats inherited from their shared family, `felidae`.

Using inheritance in programming, we can create a structure of classes that inherit properties and methods from other classes.

.. admonition:: Example

	If we wanted to program classes for our tiger and housecat, we would create a felidae class for the family.
	We would then create two classes for the panthera genus and the felis genus. We would create classes for the tiger and house cat species as well.
	The species classes would inherit properties and methods from the genus classes and the genus classes would inherit properties and methods from the family class.

	** Maybe add a figure **

.. index:: ! parent class, ! child class

The classes inheriting properties and methods are **child classes** and the classes passing down properties and methods are **parent classes**.

``extends``
-----------

When designating a class as inheriting from another class in JavaScript, we use the ``extends`` keyword.
By adding ``extends`` to the class declaration, we can designate that the class we are declaring is a child class of its parent. 

.. admonition:: Example

	.. sourcecode:: js

		class panthera {
			isBig: True;
		}

		class tiger extends panthera {
			hasStripes: True;
		}

	When creating the classes for our tiger, we can use the ``extends`` keyword to set up ``tiger`` as the child class of ``panthera``.
	The ``tiger`` class then inherits the property, ``isBig``, from the ``panthera`` class and has an additional property, ``hasStripes``.

.. note::

	The ``extends`` keyword is not supported in Internet Explorer.