More Event Types
================
Something about how there are numerous event types. Below are examples of a few more.
Link to full list?

The following sections are a summary of a few events,
see the reference links below for a more complete list. Note, you do NOT need to memorize each
event in the reference links, instead use them as a guide when you are ready to learn more about
the DOM.

1. `W3Schools Event reference  <https://www.w3schools.com/jsref/dom_obj_event.asp>`_
2. `MDN Event reference <https://developer.mozilla.org/en-US/docs/Web/Events>`_


Load Event
----------

.. index::
   single: event; load

The DOM includes the **load event** which is triggered when the window, elements, and resources have
been *loaded* by the browser. Why is it important to know when things have loaded? Remember you can't
interact with HTML elements in JavaScript unless they have been loaded into the DOM.

Previously we were moving the ``<script>`` element *below* any HTML elements that we needed
to reference in the DOM. Using the *load event* on the global variable ``window`` is an
alternative to ``<script>`` placement. When the *load event* has triggered on the *window* as
a whole, we can know that all the elements are ready to be used.

.. admonition:: Example

   

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
         <title>Window Load Event</title>
         <script>
            // add load event handler to window
            window.addEventListener("load", function() {
                // put DOM code here to ensure elements have been loaded
                console.log('window loaded');
                
                let ring = document.getElementById("ring-button");
                button.addEventListener("click", function (event) {
                    console.log("ring ring");
                });

                let knock = document.getElementById("knock-button");
                button.addEventListener("click", function (event) {
                    console.log("knock knock");
                });
            });
         </script>
      </head>
      <body>
         <div id="toolbar">
            <button id="ring-button">Ring Bell</button>
            <button id="knock-button">Knock on Door</button>
         </div>
      </body>
      </html>

   **Output** (if "Knock on Door" button is clicked)

   ::

      window loaded
      knock knock




Mouseover Event
---------------
example of mouseover

Do they know the elements that use these yet?
focus?
change?


Check Your Understanding
------------------------
TODO:...
use these and maybe more events
