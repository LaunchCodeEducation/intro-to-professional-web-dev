
More DOM Methods and Properties
===============================
The following sections are a summary of some DOM classes, methods, and properties. A
more complete list can be found in the reference links below. You do NOT need to memorize everything on these reference pages.
We are providing them to you as a guide for your future studies of the DOM.

1. `W3Schools DOM reference <https://www.w3schools.com/js/js_htmldom_document.asp>`_
2. `MDN DOM reference <https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction#Important_Data_Types>`_

Window
------
The global variable ``window`` is an instance of the ``Window`` class. The ``Window`` class represents the browser
window. In the case of multi-tabbed browsers, the global ``window`` variable represents the specific tab in which
the JavaScript code is running.

.. list-table:: Window Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - alert
     - ``window.alert("String message")``
     - Displays a dialog box with a message and an "ok" button to close the box.
   * - :ref:`confirm <dom-confirm-examples>`
     - ``window.confirm("String message")``
     - Displays a dialog box with a message and returns ``true`` if user clicks "ok" and ``false`` if user clicks "cancel".
   * - location
     - ``window.location``
     - Object that represents and alters the web address of the window or tab.
   * - console
     - ``window.console``
     - Represents the debugging console. Most common and basic use is ``window.console.log()``.

.. note::

   When using JavaScript in the browser environment, methods and properties defined on the ``Window``
   class are exposed as global functions and variables. An example of this is ``window.console.log()``
   is accessible by referencing ``console.log()`` directly.

Document
--------
The global ``document`` variable is an instance of the ``Document`` class. The ``Document`` class represents the
HTML web page that is read and displayed by the browser. The ``Document`` class provides properties and methods
to find, add, remove, and alter HTML elements inside on the web page.

.. list-table:: Document Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - title
     - ``document.title``
     - Read or set the title of the document.
   * - :ref:`getElementById <dom-getElementById-examples>`
     - ``document.getElementById("example-id")``
     - Returns a reference to the element that's ``id`` attribute matches the given string value.
   * - :ref:`querySelector <dom-querySelector-examples>`
     - ``document.querySelector("css selector")``
     - Returns the first element that matches the given CSS selector.
   * - :ref:`querySelectorAll <dom-querySelectorAll-examples>`
     - ``document.querySelectorAll("css selector")``
     - Returns a list of elements that match the given CSS selector.

.. note::

   ``querySelector`` and ``querySelectorAll`` use the CSS selector pattern to find matching elements. The pattern
   passed in must be a valid CSS selector. Elements will be found and returned the same way that elements
   are selected to have CSS rules applied.


Element
-------
HTML documents are made up of a tree of elements. The ``Element`` class represents an HTML element.

.. list-table:: Element Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - getAttribute
     - ``element.getAttribute("id")``
     - Returns the value of the attribute.
   * - setAttribute
     - ``element.setAttribute("id", "string-value")``
     - Sets the attribute to the given value.
   * - :ref:`style <dom-style-object-examples>`
     - ``element.style.color``
     - Object that allows reading and setting *INLINE* CSS properties.
   * - :ref:`innerHTML <dom-innerHTML-examples>`
     - ``element.innerHTML``
     - Reads or sets the HTML inside an element.


Check Your Understanding
------------------------

.. admonition:: Question

   What value will ``response`` have if the user clicks *Cancel*?

   .. sourcecode:: js

    let response = window.confirm("String message")

.. admonition:: Question

   Which of these are TRUE about selecting DOM elements?

   a. You can select elements by *CSS class* name
   b. You can select elements by *id attribute* value
   c. You can select elements by *tag* name
   d. All of the above

.. admonition:: Question

   What is the difference between the document and window variables?
