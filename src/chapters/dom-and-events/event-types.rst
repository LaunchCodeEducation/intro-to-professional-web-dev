Event Types
===========

DOM and JavaScript can handle numerous event types. We will discuss a few different types of events here.
As you continue your studies of the DOM and events, you may find these two reference links helpful.

1. `W3Schools Event reference  <https://www.w3schools.com/jsref/dom_obj_event.asp>`_
2. `MDN Event reference <https://developer.mozilla.org/en-US/docs/Web/Events>`_


Load Event
----------

.. index::
   single: event; load

The DOM includes the **load event**, which is triggered when the window, elements, and resources have
been *loaded* by the browser. Why is it important to know when things have loaded? Remember you can't
interact with HTML elements in JavaScript unless they have been loaded into the DOM.

Previously, we were moving the ``<script>`` element *below* any HTML elements that we needed
to reference in the DOM. Using the *load event* on the global variable ``window`` is an
alternative to ``<script>`` placement. When the *load event* has triggered on the *window* as
a whole, we can know that all the elements are ready to be used.

.. admonition:: Example

   A ``<script>`` tag is in ``<header>`` and all DOM code is inside *load* event handler.

   .. sourcecode:: html
      :linenos:

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
                ring.addEventListener("click", function (event) {
                    console.log("ring ring");
                });

                let knock = document.getElementById("knock-button");
                knock.addEventListener("click", function (event) {
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

.. index::
   single: event; mouseover

There are many mouse related DOM events. We have already used the *click* event. Another example
of a mouse event is the **mouseover** event, which is triggered when the mouse pointer enters
an element.

.. admonition:: Example

   We can use *mouseover* event to add a ``">"`` to the ``innerHTML`` of the element that the mouse pointer
   has been moved over.

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
      <head>
         <title>Mouseover Event</title>
         <script>
               window.addEventListener("load", function() {
                  let list = document.getElementById("lane-list");
                  list.addEventListener("mouseover", function (event) {
                     let element = event.target;
                     element.innerHTML += ">";
                     console.log("target", element);
                  });
               });
         </script>
      </head>
      <body>
         Mouseover Race
         <ul id="lane-list">
               <li>Lane 1</li>
               <li>Lane 2</li>
               <li>Lane 3</li>
         </ul>
      </body>
      </html>

   **Example HTML Output** (if the mouse is moved over elements in the list)

   ::

      Mouseover Race

         Lane 1>>>>>>>
         Lane 2>>>>>>>>>>>>
         Lane 3>>>>>>>>


Check Your Understanding
------------------------

.. admonition:: Question

   What error happens when you try to access an element that has not been loaded into the DOM?


.. admonition:: Question

   What is *true* when the *load* event is triggered on ``window``?

   a. The console is clear.
   b. All elements and resources have been loaded by the browser.
   c. Your files have finished uploading.
