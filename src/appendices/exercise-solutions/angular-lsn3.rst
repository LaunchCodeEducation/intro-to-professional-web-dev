.. _angular-lsn3-exercise-solutions:

Exercise Solutions: Angular, Lesson 3
=====================================

Add Attribute Directives and Template Variables
-----------------------------------------------

Update the HTML
^^^^^^^^^^^^^^^

.. _angular-lsn3-exercise-solutionsA1:

#. Pass in the ``message`` variable to the app html:
   
   ``app.component.html``:

   .. sourcecode:: html+ng2
      :lineno-start: 5

      <p>{{message}}</p>

.. _angular-lsn3-exercise-solutionsA3:

3. Use the ``height`` property to determine the displayed height:

   ``app.component.html``:

   .. sourcecode:: html+ng2
      :lineno-start: 31

      <p>{{height}} km</p>


:ref:`Back to the exercises <exercises-angular-lsn3A>`

Add Events to Modify Directives
-------------------------------

Control Buttons
^^^^^^^^^^^^^^^

.. _angular-lsn3-exercise-solutionsB1:

#. Add an event listener to the *Take Off* button.

   ``app.component.html``:

   .. sourcecode:: html+ng2
      :lineno-start: 38
   
      <button (click) = "handleTakeOff()">Take Off</button>

:ref:`Back to the exercises <exercises-angular-lsn3B>`


Movement Buttons
^^^^^^^^^^^^^^^^
.. _angular-lsn3-exercise-solutionsC1:

#. Label the ``img`` element so we can reference it:

   ``app.component.html``:

   .. sourcecode:: html+ng2
      :lineno-start: 20

      <img #rocketImage src="assets/images/LaunchCode_rocketline_white.png" height = "75" width = "75" [style.left]="0" [style.bottom]="0"/>

.. _angular-lsn3-exercise-solutionsC3:

3. Complete the ``moveRocket()`` method in the app's component class to handle rocket movement to the right:

   ``app.component.ts``:

   .. sourcecode:: TypeScript
      :lineno-start: 25

      moveRocket(rocketImage, direction) {
         if (direction === 'right') {
            let movement = parseInt(rocketImage.style.left) + 10 + 'px';
            rocketImage.style.left = movement;
            this.width = this.width + 10000;
         }
      }

:ref:`Back to the exercises <exercises-angular-lsn3C>`


New Requirements
----------------

.. _angular-lsn3-exercise-solutionsD1:

#. Add a check for the take off status of the shuttle:

   ``app.component.ts``:

   .. sourcecode:: TypeScript
      :lineno-start: 15

      takeOffEnabled: boolean = true;

.. _angular-lsn3-exercise-solutionsD3:

3. Use ``*ngIf`` and ``takeOffEnabled`` to determine which movement buttons are disabled.

   ``app.component.html``:

   .. sourcecode:: html+ng2
      :lineno-start: 26

      <div *ngIf="!takeOffEnabled">
         <button (click)="moveRocket(rocketImage, 'up')">Up</button>
         <button (click)="moveRocket(rocketImage, 'down')">Down</button>
         <button (click)="moveRocket(rocketImage, 'right')">Right</button>
         <button (click)="moveRocket(rocketImage, 'left')">Left</button>
      </div>

:ref:`Back to the exercises <exercises-angular-lsn3D>`
