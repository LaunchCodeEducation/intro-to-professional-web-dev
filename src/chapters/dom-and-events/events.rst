Events
======

.. index:: ! event

Have you ever thought about how programs respond to interactions from users and other
programs? Programming languages use events to represent these interactions. **Events**
are code representations of interactions that need to be responded to.

   In programming, events are triggered and then handled.

Events in programming are sent and responded to. That can also be said as
*Events in progarmming are triggered and handled*. **Triggering** an event is
the act of causing an event to be sent. **Hanlding** an event is receiving the
event and performing an action in response.


JavaScript and Events
---------------------

.. index:: ! event-driven

JavaScript is an event-driven progarmming language. **Event-driven** is a programming
pattern where the flow of the program is determined by a series of events. JavaScript
uses events to handle user interaction and make web pages dynamic. JavaScript also uses
events to know when the state of the web page components change.


DOM Events
----------
Running JavaScript in the browser requires a specific set of events that relate to loading,
styling, and displaying HTML elements. Objects in the DOM have event handling built right
into them.

Some elements, such as ``<a>`` have default functionality that handles certain events. An
example of default event handling is when a user clicks on a ``<a>``, the browser will
navigate to the address in the ``href`` attribute.

.. note::

   The DOM defines *numerous* events. Each element type does
   NOT support every event type. The events that each element supports relates to how the element
   is used.


Handling Events
---------------
Feature rich web applications rely on more than the default event handling provided by the
DOM. We can add custom interactivity with the users by attaching event handlers to HTML
elements and then writing the event handler code.

To write a handler, you need to tell the browswer what to do when a certain event happens.
DOM elements use the *on event* naming convention when declaring event handlers. For example
when defining what happens when a ``<button>`` is clicked, the ``onclick`` attribute is used.
This naming convention can be read as: *On click of the button, open an alert box.*

.. admonition:: Example

   Add a *click* handler to a ``<button>``. Define what happens when the ``<button>`` is clicked.

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
            <title>Button click handler</title>
      </head>
      <body>
            <button onclick="console('you rang...');">Ring Bell</button>
      </body>
      </html>

   **Output** (if button is clicked)

   ::

      you rang...

.. tip::

   Notice the use of single quotes ``'`` around ``'you rang...'``. When declaring the value
   of an attribute to be a string, you must use single quotes ``'`` inside the double
   quotes ``"``.

.. note::

   ``<button>`` elements represent a clickable entity. ``<button>`` elements have
   default *click* handling behavior related to ``<form>`` elements, that we will
   get into in a later chapter. For now we will be defining the *click* handler behavior.


TODO: TRY IT asking them to use alert instead of console


Check Your Understanding
------------------------

TODO:...

