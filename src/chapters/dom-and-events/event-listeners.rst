More Events
===========

Using inline event handling is a good way to get started handling events. A second way
to handle events uses the DOM objects and methods. Remember the DOM is an object representation
of the entire web page. The DOM will allow us to use only JavaScript to configure
our event handlers. The event handling declaration and code will no longer in the HTML
element attirbue, but will intead be in a``<script>`` or external JavaScript file.


Add Event Handlers in JavaScript
--------------------------------

.. index:: ! listener

Before we add event handlers in JavaScript, we need to learn a new vocabulary term related to
events in programming. A **listener** is another name for an event handler. The term
listener refers to the code *listening* for the event to occur. If the code *hears* the event,
then the event is handled.

``addEventListener`` is used to add an event handler, aka *listener*. ``addEventListener``
is a method available on instances of Window, Document, and Element.

.. sourcecode:: js

   anElement.addEventListener("eventName", aFunction);

``anElement`` is reference to a DOM element object. ``"eventName"`` is the name of an event that
the variable ``anElement`` supports. ``aFunction`` is a reference to a function. To start we are
going to use a *named function*.

.. admonition:: Example

   Set the named function ``youRang`` as the *click* handler for the ``<button>``. Notice that
   the value passed in as the event name is ``"click"`` insead of ``"onclick``.

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
         <title>Use addEventListener</title>
      </head>
      <body>
         <p id="main-text" class="orange" style="font-weight: bold;">
            a bunch of really valuable text...
         </p>
         <button id="ring-bell">Ring Bell</button>
         <script>
            function youRang() {
               document.getElementById("main-text").innerHTML += "you rang...";
               console.log("you rang...");
            }
            // Obtain a reference to the button element
            let button = document.getElementById("ring-bell");
            // Set named function youRang as the click event handler
            button.addEventListener("click", youRang);
         </script>
      </body>
      </html>

   **Result** (if button is clicked)

   ::

      affect on page: adds "you rang..." to <p>
      output in console: you rang...

.. warning::

   Be sure to use the correct event name when declaring the event name. An error will NOT be thrown
   if an invalid event name is given.

.. note::

   .. index:: ! jQuery

   This chapter uses DOM methods to add event handlers. When searching online you may find examples
   using jQuery to add event handlers, which look like ``.on("click", ...)`` or ``.click(...)``.
   **jQuery** is a JavaScript library designed to simplify working with the DOM. jQuery's popularity
   has declined as the DOM itself has gained features and improved usablity.

The second parameter of ``addEventListener`` is a function. Remember there many ways to declare a
function in JavaScript. So far we have passed in named functions as the event handler.
``addEventListener`` will accept any valid function as the event handler. It's possible and
quite common to pass in an *anonymous function* as the event handler.

.. sourcecode:: js

   anElement.addEventListener("eventName", function() {
      // function body of anonymous function
      // this function will be executed when the event is triggered
   });


Event Details
-------------
A benefit of using ``addEventListener`` is that an *event* parameter is passed as parameter
to the event handler function. This event is an object instance of the Event class, which
defines methods and properties related to events.

.. sourcecode:: js

   anElement.addEventListener("eventName", function(event) {
      console.log("event type", event.type);
      console.log("event target", event.target);
   });

``event.type`` is a string name of the event. Example: ``"click"``.

``event.target`` is an element object that was the target of the event. Example: 
A reference to the ``<button>`` element that was clicked.

TODO: TRY IT asking student to try out the above code


Event Bubbling
--------------
Understand event bubbling and how to stop it
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Event_bubbling_and_capture


On Load
-------
Move event handling to load event
https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event
https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onload


More Event Types
----------------
Know these common DOM events: mouseover, focus, change


Check Your Understanding
------------------------
TODO:...
use anonymous function as the function parameter in addEventListener
