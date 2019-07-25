.. _dom-confirm-examples:

``confirm`` Examples
====================

The general syntax for this method is:

.. sourcecode:: js

   let answer = window.confirm("Message to user");

Displays a dialog box with a message and returns ``true`` if user clicks "ok" and ``false`` if user clicks "cancel".
The browser waits until the user clicks "ok" or "cancel".

.. admonition:: Example

   .. sourcecode:: js

      let response = window.confirm("Would you like to play a game?");
      // Code does NOT continue until user responds to confirm window
      if (response) {
         console.log("Let's play a board game");
      } else {
         console.log("Oh well, let's code instead");
      }

.. note::

   Remember that methods defined on ``window`` can be used without referencing the ``window`` variable.

.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
         </head>
         <body>
            <h1>Window Confirm Example</h1>
            <script>
                  let response = confirm("Are you excited?");
                  if (response) {
                     console.log("Yay! Me too!");
                  } else {
                     console.log("Oh no! I hope tomorrow is a better day!");
                  }
            </script>
         </body>
      </html>

   **Console Output** (If "cancel" clicked)

   ::

      Oh no! I hope tomorrow is a better day!
