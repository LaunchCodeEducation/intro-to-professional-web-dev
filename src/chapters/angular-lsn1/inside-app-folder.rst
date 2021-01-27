The Angular Framework
======================

In VSCode, navigate to the ``src`` folder, open the ``index.html`` file, and
examine the code:

.. sourcecode:: html
   :linenos:

   <!doctype html>
   <html lang="en">
   <head>
      <meta charset="utf-8">
      <title>FirstProject</title>
      <base href="/">

      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" type="image/x-icon" href="favicon.ico">
   </head>
   <body>
      <app-root></app-root>
   </body>
   </html>

You have seen most of the HTML tags before, but line 12 shows something odd.
The strange tag ``<app-root>`` represents a key idea behind building templates.
Angular allows us to define our own tags, which are used as another type of
placeholder in an HTML file. In this case, ``<app-root></app-root>`` reserves
space on the web page for information supplied by other files. Line 12
essentially says, "Display all the content from the ``app`` folder here."

As we add more pieces to our template, we will define specific tags to help us
arrange the different items on the screen. This makes it easier for us to keep
track of our content. For example, if we want to build a web page that contains
a shopping list, a movies to watch list, and family photos, we can define the
tags ``<movies>``, ``<grocery-list>``, and ``<family-photos>``. With these
tags, we can reference specific content whenever we want and clearly place it
on a page. The tags also make it easy to play with new styles and formats for
our grocery list without changing much code or altering the appearance of the
movie list or photos.

Most of our work with Angular will take place within the ``app`` folder, so
let's take a closer look at some of the files there.

Inside the ``app`` folder
--------------------------

One way to change the color of the *Welcome to...* heading would be to open the
``app.component.css`` file and add some styling:

.. sourcecode:: CSS
   :linenos:

   h1 {
      color: brown;
   }

We can freely modify this file, but the CSS instructions only affect the HTML
files within ``app``. Also, the code in ``app.component.css`` overrides any CSS
found in the higher level ``styles.css`` file.

This is the pattern for Angular. CSS instructions further down in the file tree
have higher priority. If ``app`` contained a subfolder with its own ``.css``
file, then those instructions would be applied to the HTML files within that
subfolder.

Let's examine the code contained in three other ``app`` files.

``app.component.html`` File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Example

   Here is a sample of the default code inside ``app.component.html``:

   .. sourcecode:: html
      :linenos:

      <div style="text-align:center">
         <h1>
            Welcome to {{ title }}!
         </h1>
         <img width="300" alt="Angular Logo" src="image path...">
      </div>
      <h2>Here are some links to help you start: </h2>
      <ul>
         <!-- List items here... -->
      </ul>

``app.component.html`` contains the structure and most of the text seen on the
"Welcome to..." page. Note the placeholder ``{{title}}`` in line 3. This
gets filled with data passed in from another file, and it allows us to modify
the content on the page without revising the HTML.

``app.component.html`` serves as the main template for your web page. This file
will usually NOT hold a lot of HTML code. Instead, it will contain many
placeholders for content defined elsewhere in the project.

Later in this chapter, you will learn how to add new components to the ``app``
folder as well as how to arrange them in the HTML file.

``app.component.ts`` File
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Example

   ``app.component.ts``

   .. sourcecode:: TypeScript
      :linenos:

      import { Component } from '@angular/core';

      @Component({
         selector: 'app-root',
         templateUrl: './app.component.html',
         styleUrls: ['./app.component.css']
      })
      export class AppComponent {
         title = 'my-project-name';
      }

``app.component.ts`` performs several important functions with very few lines.

#. Line 4 defines the tag ``<app-root>``, which we saw in line 12 of
   ``index.html``. The tag can also be used in any files that import the
   ``AppComponent`` class.
#. Line 5 imports ``app.component.html``, which we examined above.
#. Line 6 imports ``app.component.css``, which applies styling to the HTML
   file. (If you set a different color for the *Welcome to...* sentence in the
   Try It tasks, this is why changing the css file worked).
#. Line 8 makes the ``AppComponent`` class available to other files.

Take a look at ``app.component.html`` again. We mentioned the ``{{title}}``
placeholder earlier and said that it gets filled with data from a different
file. Line 9 in ``app.component.ts`` supplies this data by assigning the string
``'my-project-name'`` to the ``title`` variable. Changing ``'my-project-name'``
to a different value alters the web page.

``app.module.ts`` File
^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Example

   ``app.module.ts``

   .. sourcecode:: TypeScript
      :linenos:

      import { BrowserModule } from '@angular/platform-browser';
      import { NgModule } from '@angular/core';

      import { AppComponent } from './app.component';

      @NgModule({
         declarations: [ AppComponent ],
         imports: [ BrowserModule ],
         providers: [],
         bootstrap: [AppComponent]
      })
      export class AppModule { }

Just like before, there is a lot going on within very few lines.

#. Lines 1, 2, and 8 import and assign the core modules that make Angular
   work. This is part of the automatic process, so do not play with these
   (yet).
#. Line 4 imports the class ``AppComponent`` from the local file
   ``app.component.ts``.
#. Line 4 also pulls in references to any other files linked to
   ``app.component.ts``.
#. Line 7 declares the imported local files as necessary for the project.
#. Line 12 exports the ``AppModule`` class and makes it available to other
   files.

``app.module.ts`` does the main work of pulling in the core libraries and local
files. As new parts are added to a project, the import statements, ``imports``
array, and ``declarations`` array update automatically. We do not have to worry
about the details for adding this critical code ourselves.

Change The Content
-------------------

Enough detail. Let's explore some more.

If you did not complete all of the :ref:`Try It <try-it-Angular-intro>`
tasks on the previous page, attempt them now. After that...

Try It!
^^^^^^^^

#. Run ``ng serve`` in the terminal to launch your web page again.
#. In ``app.component.ts``, declare and assign two variables in the
   ``AppComponent`` class---``name`` and ``itemList``.

   a. ``name`` holds your name.
   b. ``itemList`` is an array holding at least 4 items.

   .. sourcecode:: TypeScript
      :linenos:

      export class AppComponent {
         name: string = 'Barbara Liskov';
         itemList: string[] = ['item1', 'item2', 'item3', 'item4'];
      }

   .. admonition:: Note

      Instead of using the strong TypeScript variable declarations in step 2, we
      could substitute a pattern more like JavaScript:

      .. sourcecode:: JavaScript
         :linenos:

         export class AppComponent {
            name = 'Brendan Eich';
            itemList = ['item1', 'item2', 'item3', 'item4'];
         }

#. Replace line 4 in ``app.component.html`` with ``<h1>{{name}}'s First
   Angular Project</h1>``. Save your work and then check to make sure the
   web page shows the new heading.
#. Modify the ``<li></li>`` elements in ``app.component.html`` to display the
   elements from ``itemList`` in an unordered list. Be sure to use
   placeholders like ``{{itemList[0]}}`` between the tags.
#. Return to the ``AppComponent`` class in the ``.ts`` file. Define a
   ``rectangle`` object that has keys of ``length``, ``width`` and ``area``.
   Assign numbers to ``length`` and ``width``, and have ``area`` be a function
   that calculates and returns the area.

   .. sourcecode:: TypeScript
      :linenos:

      rectangle = {
         length: 5,
         width: 6,
         area: function() {
            return this.length * this.width;
         }
      }

#. Add a ``<p></p>`` element in ``app.component.html`` to display the sentence,
   "The rectangle has a length of ___ cm, a width of ___ cm, and an area of ___
   cm^2." Replace the blanks with placeholders so the web page displays the
   correct numbers whenever ``length`` or ``width`` are changed.

   .. sourcecode:: html

      <p>The rectangle has a length of {{rectangle.length}} cm, a width of {{rectangle.width}} cm,
         and an area of {{rectangle.area()}} cm^2.</p>

Filename Pattern
-----------------

Each of the files in the ``app`` folder contain the word ``component`` in their
name. This results from the fundamental idea behind Angular. Each *template*
for a web page is constructed from smaller pieces, and these pieces are the
*components*.

Our next step is to take a closer look at these building blocks within a
template.

Check Your Understanding
-------------------------

.. admonition:: Question

   Where would be the BEST place to modify our code if we want a different font
   for any ``<p>`` text within a template?

   #. ``app.component.ts``
   #. ``app.component.html``
   #. ``app.component.css``
   #. ``app.module.ts``

.. admonition:: Question

   Where would be the BEST place to modify our code if we want to add a heading
   and an unordered list to the template?

   #. ``app.component.ts``
   #. ``app.component.html``
   #. ``app.component.css``
   #. ``app.module.ts``

.. admonition:: Question

   Where do we define a new HTML tag?

   #. ``app.component.ts``
   #. ``app.component.html``
   #. ``app.component.css``
   #. ``app.module.ts``
