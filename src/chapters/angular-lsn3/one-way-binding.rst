One-Way Data Binding
=====================

Linking data from a ``component.ts`` file to the ``component.html`` file is an
example of *one-way* binding. Changes made to the ``component.ts`` file are
reflected in the view, but changes made in ``component.html`` have no influence
on ``component.ts``. Information flows in one direction only.

Displaying the Values of Variables
-----------------------------------

As we saw in Angular lessons 1 and 2, the syntax for binding a variable is to
encase its name in double braces ``{{ }}``. We used this in the exercises and
studios to display headings, titles from our movie list, astronauts on our
crew, etc.

.. admonition:: Example

   Inside the ``my-list.component.ts`` file:

   .. sourcecode:: TypeScript
      :linenos:

      export class MyListComponent implements OnInit {
         listHeading: string = 'My Great List';
         luckyNumber: number = 42;

         constructor() { }

         ngOnInit() { }
      }

   Inside the ``my-list.component.html`` file:

   .. sourcecode:: html

      <h3>{{listHeading}}</h3>
      <p>{{luckyNumber}}<p>

Changing the value of ``luckyNumber`` in the ``MyListComponent`` class will
change the text displayed by the ``p`` element. However, altering the HTML will
NOT affect the value of ``luckyNumber`` in the class.

Binding to HTML Attributes
---------------------------

We also used one-way data binding to modify attributes within an HTML tag. For
example, assume the ``image`` variable holds the URL for a photo we want to use
on our webpage.

.. admonition:: Example

   Inside the ``photos.component.ts`` file:

   .. sourcecode:: TypeScript
      :linenos:

      export class PhotosComponent implements OnInit {
         image: string = 'https://www.launchcode.org/assets/icons/trophy-95e8cbe9bfda44123422302951deb1c92a237d39052669b8fbfafec00cb4f608.png';

         constructor() { }

         ngOnInit() { }
      }

   Inside the ``photos.component.html`` file:

   .. sourcecode:: html

      <img src="{{image}}"/>

Within the ``<img>`` tag, we bind the ``image`` variable to the ``src``
attribute. Note that the braces and variable name must be inside quotes. When
the code runs, the string stored in ``image`` is used to provide the required
URL.

Update on the Binding Syntax
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Angular allows us to use an alternate syntax whenever we use data-binding to
modify an HTML attribute.

To avoid cluttering up our HTML tags with lots of double braces ``{{ }}``, we
simplify the notation as follows:

.. admonition:: Examples

   Double braces syntax:

   .. sourcecode:: html

      <img src="{{ variableName }}"/>
      <input name="{{ otherVariable }}" value="{{ thirdVariable }}"/>

   Alternate syntax:

   .. sourcecode:: html+ng2

      <img [src]="variableName"/>
      <input [name]="otherVariable" [value]="thirdVariable"/>

Instead of ``{{ }}``, place the HTML attribute in square brackets ``[ ]`` and
set that equal to the variable name in quotes.

   Note: Although the two methods accomplish exactly the same thing, the square
   brackets syntax is recommended as a best practice.

Check Your Understanding
-------------------------

.. admonition:: Question

   Which of the following is NOT a true statement about data binding?

   #. Data binding refers to the linking of component information to a view.
   #. In one-way binding, information flows in one direction only.
   #. In one-way binding, changing a component variable never updates the application view. 
   #. In one-way binding, user input does not effect component data. 


.. admonition:: Question

   What are the limitations of one-way binding? What could be accomplished 
   with two-way binding?