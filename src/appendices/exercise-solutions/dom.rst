.. _dom-exercise-solutions:

Exercise Solutions: The DOM and Events
======================================

1. When the *Take off* button is clicked, the text ``The shuttle is on the ground`` changes to ``Houston, we have liftoff!``. The *Take off* button has an ``id="liftoffButton"`` attribute.

   .. sourcecode:: js

      button.addEventListener('click', event => {
         paragraph.innerHTML = 'Houston! We have liftoff!';
      });

3. When the user's cursor *leaves* the *Abort Mission* button, the button's background returns to its original state (*Hint:* Setting the background color to the empty string, ``""``, will force it to revert to the default browser styles.)

   .. sourcecode:: js

      missionAbort.addEventListener("mouseout", function( event ) {   
         event.target.style.backgroundColor = "";
      });

