Dynamic Style Changes
======================

By adding :ref:`event listeners <angular-events>` to our Angular projects, we
can make any element on our webpage interactive. This allows us to change the
styling on the page in response to user actions.

Before we add functionality to the buttons, let's first update our text styling
a little bit.

Interactive Elements
---------------------

Let's make one of the paragraph elements respond to user clicks. Change line 7
in ``skill-set.component.html`` by adding a ``(click)`` event:

.. sourcecode:: html+ng2
   :linenos:

   <div class="skills">
      <h3>{{listHeading}}</h3>
      <ul>
         <li *ngFor="let skill of skills">{{skill}}</li>
      </ul>
      <p [style.color]="color" [align]="alignment">Here is some practice text...</p>
      <p [class.pStyle] = "changeColor" (click)="changeColor = !changeColor">Here is some more practice text...</p>
      <div>Here is another line of practice text...</div>
   </div>

Since ``changeColor`` is a boolean, ``(click)="changeColor = !changeColor"``
flips the value of the variable between ``true`` and ``false`` whenever the
text is clicked.

.. figure:: ./figures/lesson3-partially-interactive-text-styling.gif
   :alt: Interactive text styling.

.. admonition:: Try It

   Replace ``(click)`` with ``(mouseover)`` in line 7 and examine how the
   interactivity changes.


Button Styling
---------------

