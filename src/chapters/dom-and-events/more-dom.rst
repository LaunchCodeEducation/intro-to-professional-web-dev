
More DOM Methods and Properties
===============================
The global variables that make up the DOM are instances of classes defined in JavaScript. There are DOM
classes for every part of a web age, those classes contain methods and properties related to specific
duties of those entities.

The following sections are a summary of some DOM classes, methods, and properties, A
more complete list can be found in the reference links below. Note, you do NOT need to memorize
everything in the reference links, instead use them as a guide when you are ready to learn more about
the DOM.

1. `W3Schools DOM reference <https://www.w3schools.com/js/js_htmldom_document.asp>`_
2. `MDN DOM reference <https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction#Important_Data_Types>`_


Window
------
The global vairable ``window`` is an instance of the Window class. The Window class represents the browser
window. In the case of multi-tabbed browsers the global ``window`` variable represents the specific tab in which
the JavaScript code is running.

.. list-table:: Window Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - alert
     - ``window.alert("String message")``
     - Displays a dialog box with a message and a "ok" button to close the box.
   * - confirm
     - ``window.confirm("String message")``
     - Displays a dialog box with a message and returns ``true`` if user clicks "ok" and ``false`` if user clicks "cancel".
   * - location
     - ``window.location``
     - Object that represents and alters the web address of the window or tab.
   * - close
     - ``window.close()``
     - Closes the current window or tab. Note only closes windows opened with ``window.open()``.
   * - open
     - ``window.open()``
     - Opens a new browser window or tab.
   * - console
     - ``window.console``
     - Represents the debugging console. Most common and baisc use is ``window.console.log()``.

.. note::

   When using JavaScript in the browser environment, methods and properties defined on the Window
   class are exposed as global functions and variables. An example of this is ``window.console.log()``
   is accessible by referencing ``console.log()`` directly.


Document
--------
The global ``document`` variable is an instance of the Document class. The Document class represents the
HTML web page that is read and displayed by the browser. The Document class provides properties and methods
to find, add, remove, and alter HTML elements inside on the web page.

.. list-table:: Document Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - title
     - ``document.title``
     - Read or set the title of the document.
   * - getElementById
     - ``document.getElementById("example-id")``
     - Returns a reference to the element that's ``id`` attribute matches the given string value.
   * - getElementsByTagName
     - ``document.getElementsByTagName("div")``
     - Returns a list of elements with the given tag name.
   * - getElementsByClassName
     - ``document.getElementsByClassName("main-content")``
     - Returns a list elements with the given css class name.
   * - querySelector
     - ``document.querySelector(".selector-pattern")``
     - Returns the first element that matches the given css selector.
   * - querySelectorAll
     - ``document.querySelectorAll(".selector-pattern")``
     - Returns a list of elements that match the given css selector.

.. note::

   ``querySelector`` and ``querySelectorAll`` use the css selector pattern to find matching elements. The pattern
   passed in must be a valid css selector. Elements will be found and returned the same way that elements
   are selected to have css rules applied.

Element
-------
HTML documents are made up of a tree of elements. The Element class represents an HTML element.
TODO: another sentence about elements and the methods?

.. list-table:: Element Properties and Methods
   :header-rows: 1

   * - Method or Property
     - Syntax
     - Description
   * - getAttribute
     - ``element.getAttribute("id")``
     - Returns the value of attribute.
   * - setAttribute
     - ``element.setAttribute("id", "string-value")``
     - Sets the attribute to the given value.
   * - style
     - ``element.style.color``
     - Object that allows reading and setting css properties.
   * - innerHTML
     - ``element.innerHTML``
     - Reads or sets the HTML inside an element.

Examples
--------
TODO: more examples of using these. Maybe put an examples section under each section?

Check Your Understanding
------------------------
TODO: more examples of using these
