Angular Wrap-Up
================

Over the past three chapters, you have learned:

#. What *templates* are and why we want to use them,
#. How to use the Angular CLI to create a new project, generate new components,
   and run a project locally in your web browser.
#. How to define custom HTML tags and use them to arrange components within a
   template.
#. How to use the *structural directives* ``*ngFor`` and ``*ngIf`` to
   automatically generate HTML elements and display dynamic content.
#. How to catch events and set up data-binding to make your webpage respond to
   user actions.
#. How to use *attribute directives* to modify the appearance and behavior of
   specific HTML elements.

Tip of the Iceberg
-------------------

The Angular skills you learned are a small slice of what the framework can
accomplish. They provide a solid foundation if you choose to learn more on your
own.

Of course, practice makes better. The best way for you to get better at
Angular is to use Angular. Adapt the examples, exercises, and studio projects
however you want. Also, create your own project and build your own sample
webpages. Create an interactive family photo page, a grocery list, a web based
breakout box, or whatever you want.

You can find full documentation on the `Angular.io <https://angular.io/>`__
website. A good "next step" for your Angular learning would be to complete the
`Tour of Heros <https://angular.io/tutorial>`__ tutorial.

.. admonition:: Note

   The Angular documentation is excruciatingly complete, but do not be
   intimidated. There are plenty of separate tutorial sites that cover individual
   skills and techniques. When you find an interesting topic on the Angular site,
   feel free to Google that topic and explore how other coders explain how to use
   it.

Two Topics to Consider
^^^^^^^^^^^^^^^^^^^^^^^

In this chapter, we discussed *one-way* data binding. As the name suggests,
*two-way* binding exits as well. We chose not to explore this idea because
one-way tasks are more flexible and more frequently used. However, two-way
binding can come in handy if you want data from an ``input`` element to
automatically change a variable in the ``.ts`` file.

A much larger idea involves passing data between different components in the
same template. Passing data from a parent component to its children, from a
child to the parent, or between children is VERY useful. Unfortunately, that
topic is beyond the scope of these lessons.

Try Googling "Passing data between Angular components", and explore several
of the most recent results. Find one that best suits your learning style, and
then create a simple template that includes parent-child communication. Also,
the *Tour of Heros* tutorial uses component to component communication.

If your future coding job involves Angular, you will most likely need to learn
the skill.

Components Should Be Re-used
-----------------------------

Recall that at their best, functions accomplish only ONE task. This makes them
re-usable within the same program, or as a module accessible by many different
programs. Components should behave in a similar manner. Each one should do just
one simple thing and should be flexible enough to work within many different
templates.

The real power of a front end framework comes when you view components as
reusable elements. With time and practice, you will build a collection of
small, generic components. You can then combine these tools in different ways
to build small or large sections of any new project. The Lego analogy works
here---the same set of blocks can be combined in multiple ways to produce
different outcomes. Also, if you need consistent results on multiple webpages,
then you just put the components together the same way each time instead of
writing new code.

For demonstration purposes, some of our examples don't use this best practice
and instead include components that serve many purposes. After you finish the
following exercises and studio, consider how you could split the larger
components into smaller, re-usable pieces.
