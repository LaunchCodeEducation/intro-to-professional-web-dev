.. _dom-exercises:

Exercises: The DOM and Events
=============================

Time to make a flight simulator for your fellow astronauts! The provided HTML
and JavaScript files can be used for all of the exercises. For each exercise,
the requirements and desired effect of the events is listed. 

`Repl.it with starter code <https://repl.it/@launchcode/Exercises-DOM-and-Events>`__

#. When the *Take off* button is clicked, the text ``The shuttle is on the ground`` changes to ``Houston, we have liftoff!``. The *Take off* button has an ``id="liftoffButton"`` attribute.

   :ref:`Check your solution <dom-exercise-solutions1>`

#. When the user's cursor goes over the *Abort Mission* button, the button's background turns red. The *Abort Mission* button has ``id="abortMission"``.
#. When the user's cursor *leaves* the *Abort Mission* button, the button's background returns to its original state (*Hint:* Setting the background color to the empty string, ``""``, will force it to revert to the default browser styles.)

   :ref:`Check your solution <dom-exercise-solutions3>`

#. When the user clicks the *Abort Mission* button, make a confirmation window that says ``Are you sure you want to abort the mission?``. If the user confirms that they want to abort, the text changes to ``Mission aborted! Space shuttle returning home``.
