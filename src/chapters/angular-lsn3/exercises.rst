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

   1. A window confirm should let the user know "Confirm that the shuttle is ready for takeoff." If the shuttle is ready for liftoff, then add steps 2-4.
   2. The flight status should change to "Shuttle in flight."
   3. The background color of the shuttle flight screen should change from green to blue.
   4. The shuttle height should increase by 10,000 miles.

#. When the "Land" button is clicked, the following should happen:

   1. A window alert should let the user know "The shuttle is landing. Landing gear engaged."
   2. The flight status should change to "The shuttle has landed."
   3. The background color of the shuttle flight screen should change from blue to green.
   4. The shuttle height should go down to 0.


#. When the "Abort Mission" button is clicked, the following should happen:

   1. A window confirm should let the user know "Confirm that you want to abort the mission." If the user wants to abort the mission, then add steps 2-4.
   2. The flight status should change to "Mission aborted."
   3. The background color of the shuttle flight screen should change from blue to green.
   4. The shuttle height should go do to 0.

#. When the "Up", "Down", "Right", and "Left" buttons are clicked, the following should happen:

   1. The rocket image should move 10 px in the direction of the button that was clicked.
   2. If the "Up" or "Down" buttons were clicked, then the shuttle height should increase or decrease by 10,000 miles.


Add Attribute Directives and Template Variables
-----------------------------------------------
TODO: add directives for ``class``, ``value``, etc.?

For requirements 1-3, you'll see that the properties that need to be changed 
have been arranged into several status objects, ``initStatus``, ``shuttleTakeOff``,
``shuttleLand``, and ``shuttleMissionAbort``. Depending on the state of the rocket,
one of these status objects will assign the values seen in the app view.

The ``color``, ``height``, and ``message`` properties will all be used as
template variables to dynamically update the view. In ``app.component.html``,
change line 19 to the following:

.. sourcecode:: html+ng2
      
      <div class="shuttleBackground" [style.backgroundColor]=“status.color”>

Use the ``status.height`` property to determine the 
displayed height. Change line 31 as follows;

.. sourcecode:: html+ng2
      
      <p>{{status.height}}</p><p> miles</p>

Finally, change line 5 to make use of ``status.message``.

.. sourcecode:: html+ng2
      
      <p>{{status.message}}</p>

Now, back in ``app.component.ts``, you'll see that line 35
assigns the current status to the ``initStatus`` object. 
So the app now uses the properties found in ``initStatus``
to render the page.


Add Events to Modify Directives
-------------------------------

Now, we'll add some event listeners to the three control
buttons on the bottom of the page. These listeners will
reassign the status object to one of ``shuttleTakeOff``,
``shuttleLand``, or ``shuttleMissionAbort``.

In ``app.component.html``, add an event listener to the *Take Off*
button.

.. sourcecode:: html+ng2
      
      <button (click) = "handleTakeOff()">Take Off</button>

Back in ``app.component.ts``, we'll define this listener.
The confirm method will look the same as before, but this
time we can use a few less lines of code to update the view.

.. sourcecode:: TypeScript
   :linenos:

   handleTakeOff() {
      let result = window.confirm('Are you sure the shuttle is ready for takeoff?');
      if (result) {
         this.status = this.shuttleTakeOff;
      }
   }

Follow the same pattern to handle the *Land* and *Abort Mission*
click events.

Next, we'll tackle the ``Up``, ``Down``, ``Left``, and ``Right`` buttons that
move the rocket. The ``movement`` formula is the same as we've used before:

.. sourcecode:: TypeScript
   :linenos:

   let movement = parseInt(img.style.left) + 10 + 'px';


But now, instead of using the ``getElementById`` method, we'll
access the ``img`` element by passing it in to the click
event.

In ``app.component.html``, label the ``img`` element so we can reference it:

.. sourcecode:: html+ng2
      
      <img #rocketImage src="assets/images/LaunchCode_rocketline_white.png" height = "75" width = "75" [style.left]="0" [style.bottom]="0"/>

While you're here, add the click handler to the *Right* button:

.. sourcecode:: html+ng2
      
      <button (click)="handleRightClick(rocketImage)">Right</button>

Now in ``app.component.ts`` we can write the ``handleRightClick()``:

.. sourcecode:: TypeScript
   :linenos:

   handleRightClick(rocketImage) {
      let movement = parseInt(rocketImage.style.left) + 10 + 'px';
      rocketImage.style.left = movement;
   }

Follow the same pattern for the other directional buttons, modifying the
movement formula as needed. For the *Up* and *Down* buttons, we'll want
to also update the current status object's height property.

For example, the *Down* click handler could look like this:

.. sourcecode:: TypeScript
   :linenos:

   handleDownClick(rocketImage) {
    let movement = parseInt(rocketImage.style.bottom) - 10 + 'px';
    rocketImage.style.bottom = movement;
    this.status.height = this.status.height - 10000;
   }

Along those same lines, we'll want to modify a couple of our control 
button handlers to update ``rocketImage``'s position when the status
changes. Pass in ``rocketImage`` to your *Land* and *Abort Mission* 
handlers and add the following:

.. sourcecode:: TypeScript
   :linenos:

   rocketImage.style.bottom = '0px';


Maybe change text color if fuel level drops too low?

Maybe enable/disable buttons based on whether ``cargoHold`` is full?

Enable ``Launch`` button when all checks pass?


Fly the Rocket?
----------------
