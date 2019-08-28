Attribute Directives
=====================

In the previous two chapters, you learned about two of the three
:ref:`Angular directives <angular-directives>`---components and structural. You
will now use data-binding to practice *attribute directives*. These change the
appearance of a specific HTML element within the DOM.

Open the Lesson 3 Folder
-------------------------

Open VSCode and return to the ``angular-lc101-projects`` folder. Find
``lesson3/examples/src/app`` in the sidebar and open the
``skill-set.component.ts`` and ``skill-set.component.html`` files.

.. figure:: ./figures/lesson3-menu.png
   :alt: Access Angular lesson 3 in VSCode.

Open the terminal panel and navigate to the lesson3 ``examples`` folder. Also
make sure that you are on the ``master`` branch.

.. sourcecode:: bash

   $ git branch
      * master
      solutions
   $ ls
      lesson1 lesson2 lesson3
   $ cd lesson3
   $ ls
      examples        exercises
   $ cd examples

Once you are in the folder, enter ``npm install`` in the terminal, then run
``ng serve`` to launch the project.

You should see the following:

.. figure:: ./figures/lesson3-attribute-directive-practice-start.png
   :alt: Attribute directives starting screen.

Update the Skill-Set Styling
-----------------------------

Examine the code in the ``skill-set.component.html`` and
``skill-set.component.ts`` files:

.. admonition:: Examples

   ``skill-set.component.html``

   .. sourcecode:: html+ng2
      :linenos:

      <div class="skills">
         <h3>{{listHeading}}</h3>
         <ul>
            <li *ngFor="let skill of skills">{{skill}}</li>
         </ul>
         <p>Here is some practice text...</p>
         <p>Here is some more practice text...</p>
      </div>

   ``skill-set.component.ts`` SkillSetComponent class:

   .. sourcecode:: TypeScript
      :linenos:

      export class SkillSetComponent implements OnInit {
         listHeading: string = 'Some Coding Skills I Know';
         skills: string[] = ['Loops', 'Conditionals', 'Functions', 'Classes', 'Modules', 'Git', 'HTML/CSS'];
         color: string = 'black';
         alignment: string = 'center';
         changeColor: boolean = true;

         constructor() { }

         ngOnInit() { }

      }

Right now, there is an awful lot of green in the list, which is set by the
``skills`` class in ``skill-set.component.css``. Let's fix this.

Inline Styling
^^^^^^^^^^^^^^^

To change the color and alignment of the first paragraph element, we could
override the CSS instructions with some inline code:

.. sourcecode:: html

   <p style="color: black" align="center">Here is some practice text...</p>

However, we can use what we learned about data-binding to replace these
hard-coded styles with variables:

.. sourcecode:: html+ng2

   <p [style.color]="color" [align]="alignment">Here is some practice text...</p>

Ideas to note:

#. Unlike the structural directives ``*ngFor`` and ``*ngIf``, we can add more
   than one attribute directive to an HTML tag.
#. The ``style`` attribute has different properties that can be assigned using
   dot notation. Examples include ``style.color`` and ``style.background``.
#. The variables ``color`` and ``alignment`` are assigned in
   ``skill-set.component.ts`` file.
#. NEAT! Reassigning the ``color`` variable in the ``.ts`` file causes EVERY
   tag with ``[style.color]="color"`` to change color.

.. admonition:: Try It

   Change the values for the ``color`` and ``alignment`` variables. Save your
   work and refresh the webpage to see the results.

Changing Styles with Booleans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can accomplish the same results by applying a class to the second ``p`` tag:

#. Add the following code to ``skill-set.component.css``:

   .. sourcecode:: html
      :linenos:

      .pcentered {
         color: black;
         text-align: center;
      }

#. Next, modify line 7 in the starter code:

   .. sourcecode:: html+ng2
      :linenos:

      <div class="skills">
         <h3>{{listHeading}}</h3>
         <ul>
            <li *ngFor="let skill of skills">{{skill}}</li>
         </ul>
         <p [style.color]="color" [align]="alignment">Here is some practice text...</p>
         <p [class.pcentered]="changeColor">Here is some more practice text...</p>
         <div>Here is another line of practice text...</div>
      </div>

   After saving these updates, the skills list changes appearance:

   .. figure:: ./figures/lesson3-styled-skill-text.png
      :alt: Attribute directives midpoint screen.

#. Instead of setting ``[class.pcentered]`` equal to a string, the
   ``changeColor`` variable is a boolean (line 6 in
   ``skill-set.component.ts``). If ``changeColor`` is ``true``, Angular adds
   the ``pStyle`` class of the tag. If ``changeColor`` is ``false``, the class
   remains absent from the tag.

.. admonition:: Try It

   #. Set ``changeColor`` to ``false`` and verify that "Here is some more
      text..." changes back to green.
   #. Create a ``li-centered`` class in the CSS file and modify line 4  in
      ``skill-set.component.html`` to make the style of the ``li`` elements
      depend on ``!changeColor``.

What About the Buttons?
------------------------

Nice display of eagerness! We will deal with the buttons on the next page.

Check Your Understanding
-------------------------

Lorem ipsum...
