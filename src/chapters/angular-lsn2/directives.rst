Angular Directives
===================

.. index:: ! directive

Angular manages website content through the use of *directives*, and there
are three types:

#. **Components**: These control how a set of data gets displayed within a
   template.
#. **Structural directives**: These change the layout of the DOM by adding or
   removing elements (``div``, ``ul``, ``a``, ``li``, etc.).
#. **Attribute directives**: These change the appearance of a specific element
   within the DOM.

We learned how to generate and modify components in the
:ref:`last chapter <angular-1>`. In this lesson, we will focus on how to use
structural directives to enhance our work.

Open the Lesson 2 Folder
-------------------------

If you have not yet forked the Angular lessons repo, follow the directions for
given in :ref:`lesson 1 <angular-1>`.

Open the ``angular-lc101-projects`` folder in VSCode and find ``lesson2`` in
the sidebar.

.. figure:: ./figures/lesson2-menu.png
   :alt: Access Angular lesson 2 in VSCode.

Open the terminal panel and navigate to the lesson2 folder. You should find
subfolders for the examples, exercises, and studio used in this chapter. Also,
solutions to some of the tasks are located in the ``example-solutions`` branch.

.. sourcecode:: bash

   $ ls
      lesson1 lesson2 lesson3
   $ cd lesson2
   $ ls
      examples        exercises       studio
   $ git branch
      example-solutions
      * master
