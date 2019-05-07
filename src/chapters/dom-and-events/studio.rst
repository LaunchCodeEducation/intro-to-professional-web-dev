Studio: The DOM and Events
==========================

Now that we can build a basic flight simulator, we want to add more controls for the staff at our space station.
The HTML, CSS, and JavaScript files are provided. For each event, the requirements and desired effect is listed.

1. When the "Take off" button is clicked, the following should happen:
   
   1. A window confirm should let the user know "Confirm that the shuttle is ready for takeoff." If the shuttle is ready for liftoff, then add steps 2-4.
   2. The flight status should change to "Shuttle in flight".
   3. The background color of the shuttle flight screen (``id = "shuttleBackground"``) should change from green to blue.
   4. The shuttle height should increase by 10,000 miles.

2. When the "Land" button is clicked, the following should happen:

   1. A window alert should let the user know "The shuttle is landing. Landing gear engaged."
   2. The flight status should change to "The shuttle has landed".
   3. The background color of the shuttle flight screen should change from blue to green.
   4. The shuttle height should go down to 0.


3. When the "Abort Mission" button is clicked, the following should happen:

   1. A window confirm should let the user know "Confirm that you want to abort the mission." If the user wants to abort the mission, then add steps 2-4.
   2. The flight status should change to "Mission aborted."
   3. The background color of the shuttle flight screen should change from blue to green.
   4. The shuttle height should go do to 0.

4. When the "Up", "Down", "Right", and "Left" buttons are clicked, the following should happen:

   1. The rocket image should move 10 px in the direction of the button that was clicked.
   2. If the "Up" or "Down" buttons were clicked, then the shuttle height should increase or decrease by 10,000 miles.

Bonus Mission
-------------

If you are done with the above and have some time left during class, there are a few problems that you can tackle for a bonus mission.

1. Keep the rocket from flying off of the background.
2. Return the rocket to its original position on the background when it has been landed or the mission was aborted.