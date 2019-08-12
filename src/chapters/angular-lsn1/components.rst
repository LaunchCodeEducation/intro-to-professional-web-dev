Components
===========

.. index:: ! angular-component

In Angular a **component** controls a patch of screen called a view.

Angular builds a web page by combining multiple components together.
Splitting our page into individual components makes our application more
organized, and increases our ability to focus on one section of our web
application at a time.

Everything in Angular centers on the idea of building a webpage from separate,
smaller pieces. We must understand how to get these pieces to work together,
and that begins by exploring what makes up each individual component. In order
to build a reliable component, we must understand how each of its parts work
and interact.

Component Files
---------------

A component consists of 4 files:

#. an HTML file (.html)
#. a CSS file (.css)
#. a typescript file (.ts)
#. a test file (.spec.ts)

.. figure:: ./figures/ComponentPieces.png
   :alt: Visual of the files associated with a Component.

Looking at the file tree, we see that all four files contain the name of the
component. Also, the files are located in a folder named after the component.
In the example above the component was named ``header``.

If we add a new component named ``task-list``, the four files created inside
the ``task-list`` folder and would be called:

#. task-list.html
#. task-list.css
#. task-list.ts
#. task-list.spec.ts

Each file contains the information necessary for ONLY that component.
``task-list.html`` holds the HTML required for the task-list and no other
component. ``task-list.css`` only styles html within the ``task-list`` folder,
the typescript code in ``task-list.ts`` only applies to this component, and all
the tests for this component will be found in ``task-list.spec.ts``.

Adding a New Component
----------------------

Each component is a smaller part of an overall web application. The main
component serves as a base structure, and it comes standard with all Angular
applications. It's the container that holds all of the other components, and it
organizes them into the web application.

An important thing to understand is how new components are created and then
added to the main component.

When you generate a new component using a tool like Stackblitz or the Angular
CLI, it is automatically added to the main component. Let's explore how this
process works.

With the Angular CLI we generate a new component with the ``ng generate
component`` command from the terminal.

.. figure:: ./figures/GenerateComponent.png
   :alt: Visual of the terminal command to create a new Component.

From the output of the command we can see it creates four new files in the
appropriate folder, and updates our ``app.module.ts`` file. Which results in
the following file structure.

.. figure:: ./figures/GenerateComponentResult.png
   :alt: Visual of the results of generate Component.

Component Nesting
-----------------

Components can be put inside of other components. In essence, this is how the
main component works. It is the component that holds all other components.

However, sometimes you may want to nest a new component inside of another one
rather than in main.

Let's assume we want to add a new component within our ``task-list`` folder. In
this case we simply change into the ``task-list`` directory from our terminal
and then run the ``ng generate component`` command.

.. figure:: ./figures/GenerateNestedComponent.png
   :alt: Visual of the terminal command(s) to create a nested component.

Running this command nests our new folder inside of the ``task-list`` folder,
and it contains the four files we would expect.

.. figure:: ./figures/GenerateNestedComponentResult.png
   :alt: Visual of the result of the running the commands to create a nested component.

When we nest a component inside of another, we still have all the files for
the nested component at our disposal. Any CSS, HTML, or JavaScript we write
will only affect the nested component and not the parent. However, the parent
component DOES influence the nested one. For example, any CSS within
``task-list.component.css`` will apply to both ``task-list.component.html`` and
``inside-task-list.component.html``. If we want ``inside-task-list`` to have
different styling, we need to add code to the ``inside-task-list`` CSS file to
override the parent.