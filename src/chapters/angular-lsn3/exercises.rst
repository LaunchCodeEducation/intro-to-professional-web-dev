Exercises: Angular, Part 3
===========================

Remember that :ref:`DOM and Events studio <DOM-studio>`? Let's
revisit this and do it again Angular-style.

Starter Code
-------------

The starter code for the exercises is in the same
`repository <https://github.com/LaunchCodeEducation/angular-lc101-projects>`__
that you cloned for the all of the Angular lessons.

From the ``lesson3`` folder in VSCode, navigate into the
``exercises/src/app/`` folder. Open the
``app.component.html`` and ``app.component.ts`` files.

In the terminal, navigate into the lesson 3 ``exercises`` folder. Enter
``npm install`` to add the Angular modules, then run ``ng serve``. When you
open the webpage in your browser, it should look like this:

   .. figure:: ./figures/lesson3-exercises-initial-view.png
      :alt: Initial view of the exercises app.

   Initial view of the exercises app

The Requirements Review
-----------------------

The requirements are the same as before:

#. When the "Take off" button is clicked, the following should happen:

   1. A confirmation window should let the user know "Confirm that the shuttle is ready for takeoff." If the shuttle is ready for liftoff, then add steps b-d.
   2. The flight status should change to "Shuttle in flight."
   3. The background color of the shuttle flight screen should change from green to blue.
   4. The shuttle height should increase by 10,000 miles.

#. When the "Land" button is clicked, the following should happen:

   1. A window alert should let the user know "The shuttle is landing. Landing gear engaged."
   2. The flight status should change to "The shuttle has landed."
   3. The background color of the shuttle flight screen should change from blue to green.
   4. The shuttle height should go down to 0.


#. When the "Abort Mission" button is clicked, the following should happen:

   1. A confirmation window should prompt the user if they really want to abort the mission. If the user wants to abort the mission, then add steps b-d.
   2. The flight status should change to "Mission aborted."
   3. The background color of the shuttle flight screen should change from blue to red.
   4. The shuttle height should go do to 0.

#. When the "Up", "Down", "Right", and "Left" buttons are clicked, the following should happen:

   1. The rocket image should move 10 px in the direction of the button that was clicked.
   2. If the "Up" or "Down" buttons were clicked, then the shuttle height should increase or decrease by 10,000 miles.


Add Attribute Directives and Template Variables
-----------------------------------------------

Open ``app.component.ts`` and take a look. The ``color``, ``height``, and 
``message`` properties will all be used as template variables to dynamically 
update the view. 

.. sourcecode:: TypeScript
   :linenos:
      
   export class AppComponent {
      title = 'Exercises: Angular Lesson 3';

      color = 'green';
      height = 0;
      width = 0;
      message = 'Space shuttle ready for takeoff!';
   }

In ``app.component.html``, change line 19 to the following:

.. sourcecode:: html+ng2
      
      <div class="shuttle-background" [style.backgroundColor]=“color”>

Use the ``height`` property to determine the 
displayed height. Change line 31 as follows;

.. sourcecode:: html+ng2
      
      <p>{{height}}</p><p> miles</p>

Finally, change line 5 to make use of ``message``.

.. sourcecode:: html+ng2
      
      <p>{{message}}</p>

Refresh the page to ensure your template variables are assigned correctly.


Add Events to Modify Directives
-------------------------------

Control Buttons
^^^^^^^^^^^^^^^

Now, we'll add some event listeners to the three control buttons on the bottom of the page. 
These listeners will reassign the values of ``color``, ``height``, ``width``, and ``message``.

1. In ``app.component.html``, add an event listener to the *Take Off* button.

.. sourcecode:: html+ng2
      
      <button (click) = "handleTakeOff()">Take Off</button>

2. Back in ``app.component.ts``, we'll define this listener. The confirm method will look the same as before, but this time we can use a few less lines of code to update the view.

.. sourcecode:: TypeScript
   :linenos:

   handleTakeOff() {
      let result = window.confirm('Are you sure the shuttle is ready for takeoff?');
      if (result) {
         this.color = 'blue';
         this.height = 10000;
         this.width = 0;
         this.message = 'Shuttle in flight.';
      }
   }

3. Follow the same pattern to handle the *Land* and *Abort Mission* click events.

Movement Buttons
^^^^^^^^^^^^^^^^

Next, we'll tackle the ``Up``, ``Down``, ``Left``, and ``Right`` buttons that
move the rocket. The ``movement`` formula is the same as we've used before:

.. sourcecode:: TypeScript
   :linenos:

   let movement = parseInt(img.style.left) + 10 + 'px';


But now, instead of using the ``getElementById`` method, we'll
access the ``img`` element by passing it in to the click
event.

1. In ``app.component.html``, label the ``img`` element so we can reference it:

.. sourcecode:: html+ng2
      
      <img #rocketImage src="assets/images/LaunchCode_rocketline_white.png" height = "75" width = "75" [style.left]="0" [style.bottom]="0"/>

2. While you're here, add the click handler to the *Right* button:

.. sourcecode:: html+ng2
      
      <button (click)="moveRocket(rocketImage, 'right')">Right</button>

3. Now in ``app.component.ts`` we can write the ``handleRightClick()``:

.. sourcecode:: TypeScript
   :linenos:

   moveRocket(rocketImage, direction) {
    if (direction === 'right') {
      let movement = parseInt(rocketImage.style.left) + 10 + 'px';
      rocketImage.style.left = movement;
      this.width = this.width + 10000;
    } 
   }

4. Add conditional logic to this ``moveRocket()`` method to account for the other movement directions, modifying the
movement formula as needed. Be sure to also update the height or width property
where appropriate.

Update the Control Button Click Handlers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Along those same lines, we'll want to modify a couple of our control 
button handlers to update ``rocketImage``'s position when the status
changes. Pass in ``rocketImage`` to your *Land* and *Abort Mission* 
handlers and add the following:

.. sourcecode:: TypeScript

   rocketImage.style.bottom = '0px';

New Requirements
----------------

1. Right now, a user can move the rocket before it has officially taken off or abort the 
mission while the rocket is still on the ground. This doesn't make much sense. With attribute
directives, we can dynamically set those buttons to only be enabled in some states.

Let's add a check for the take off status of the shuttle.

.. sourcecode:: TypeScript
   :linenos:

    takeOffEnabled: true,
    

2. When the app is first loaded, we want the user to be able to click the *Take Off*
button, but not the *Land* or *Abort Mission* button. We'll add some 
``[disabled]`` attribute directives on the control buttons to reflect these values.

Update the control buttons:

.. sourcecode:: html+ng2
   :linenos:
      
   <div class="container-control-buttons">
      <button (click)="handleTakeOff()" [disabled]="!takeOffEnabled">Take Off</button>
      <button (click)="handleLand(rocketImage)" [disabled]="takeOffEnabled">Land</button>
      <button (click)="handleMissionAbort(rocketImage)" [disabled]="takeOffEnabled">Abort Mission</button>
   </div>

Now, based on the boolean ``takeOffEnabled``, only the *Take Off* control button 
is enabled when the rocket is on the ground.

Update the control button click handlers to toggle the enabled/disabled status 
of the controls using this value.

3. For another improvement, we shouldn't be able to move the rocket if it hasn't taken off. To toggle the status of
the direction buttons, we could add more boolean checks to our component. However, we know we only
want these buttons to be accessible when the *Take Off* button is not. We can therefore take advantage
of this property we already defined to determine if the user can click the direction buttons.

.. sourcecode:: html+ng2
   :linenos:
      
   <button (click)="moveRocket(rocketImage, 'up')" [disabled]="takeOffEnabled">Up</button>

In fact, since all four direction buttons share the same requirements for disablement, we can take
advantage of our old friend ``ngIf`` to display the whole set based on ``takeOffEnabled``.

.. sourcecode:: html+ng2
   :linenos:

   <div *ngIf="!takeOffEnabled">
      <button (click)="moveRocket(rocketImage, 'up')">Up</button>
      <button (click)="moveRocket(rocketImage, 'down')">Down</button>
      <button (click)="moveRocket(rocketImage, 'right')">Right</button>
      <button (click)="moveRocket(rocketImage, 'left')">Left</button>
   </div>

4. Lastly, let's change the shuttle's background color to a warning color if the rocket image gets too 
close to the edge. Add a function to your component that will check the width and height values
and changes the color value to orange if those values are too high or low. Call that function in each
of the direction button click handlers.


Bonus Mission
-------------

#. Just like the original studio, change the code to prevent the rocket image from flying off the colored background.
#. Dynamically adjust the enabled/disabled status of the direction buttons based on the position of the rocket.
