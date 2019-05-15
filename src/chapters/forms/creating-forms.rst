Forms
=====

.. index:: ! form

Web pages are used to display and accept data, is not a provocative statement. In this chapter
we are going to learn more about how web pages handle data input using HTML forms.
An HTML **form** is used to accept input from the user and send that data to the server.


Create a Form
-------------
To declare a form in HTML use the ``<form>`` tag with open and closing tags. This form element
will service as container for various types of other elements that are designed to capture
input from the user.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <!-- empty form -->
         <form></form>
      </body>
   </html>

By default an empty ``<form></form>`` will not appear on a web page until inputs have been
added inside of it. Below we have added one basic
``<input>`` tag.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <input type="text"/>
         </form>
      </body>
   </html>


Input Element
-------------

.. index:: ! input

The ``input`` element is used to add interactive fields, which allow the user to enter data.
``input`` elements have two very important attributes: *name* and a *type*.

- ``name`` attribute is used to identify the input's value when the data is submitted
- ``type`` attribute defines which type of value of the input represents

.. sourcecode:: html

   <input type="text" name="username"/>

.. warning::

   Your form will NOT submit a value for an ``<input>`` unless it has a ``name`` attribute.

.. index:: ! label

Forms normally contain more than one input. ``<label>`` tags are used provide a textual label,
which informs the user of the purpose of the field. The simplest usage of
``<label>`` tags is to *wrap* them around ``<input>`` tags.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <label>Username <input type="text" name="username"/></label>
            <label>Team Name <input type="text" name="teamName"/></label>
         </form>
      </body>
   </html>

.. figure:: figures/label-example.png
   :alt: HTML that includes a form tag with two input elements. Each element is inside of a label element.

A second way to relate a ``<label>`` tag to an ``<input>`` is to use the ``id`` attribute of
``input`` and the ``for`` attribute of ``label``. When ``for`` is used, the ``<input>``
does NOT have to inside of the``<label>``.


.. sourcecode:: html

   <label for="username"/><input id="username" name="username" type="text"/>

What happens when a ``<label>`` is clicked? The answer depends on what the ``<label>`` is
associated to.

.. index:: ! focus

For *text* inputs, when the label is clicked, then the input gains *focus*. An element with
**focus** is currently selected by the browser and ready to receive input.

For *non-text* based inputs, when the label is clicked, a value is selected. This behavior
can be seen with ``radio`` and ``checkbox`` elements which we will learn more about soon.


Types of Inputs
---------------
As you know from using the web sites, it's possible to use more than simple text inputs. There
are additional input *types* that each have a specific purpose. Many of the elements are
``<input>`` tags with a different ``type`` value, however some have entirely different tag names.

Basic Text Inputs
^^^^^^^^^^^^^^^^^
Any values can be typed into these text fields, there are no restrictions enforced by the
browser.

.. role:: raw-html(raw)
   :format: html

.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - text
     - ``<input type="text" name="username">``
     - A single line text field.
     - :raw-html:`<input type="text" name="username"/>`
   * - textarea
     - ``<textarea name="missionDescription"/>``
     - A larger, multi-line text box.
     - :raw-html:`<textarea name="missionDescription"></textarea>`
   * - password
     - ``<input type="password" name="passCode"/>``
     - A text field that obscures the text typed by the user.
     - :raw-html:`<input type="password" name="passCode"/>`

.. note::

   Form inputs will NOT look exactly the same in all browsers.
   However, the inputs *should* function the same way. Use `<https://caniuse.com>`_,
   if there is ever a question of browser support for a certain feature.


Specialized Text Inputs
^^^^^^^^^^^^^^^^^^^^^^^
For these text inputs the browser will validate and provide feedback to the user based on
rules for the declared type.

.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - date
     - ``<input type="date" name="flightDate"/>``
     - Browser validates the value is a valid date
       format. Some browsers provide a *date picker*.
     - :raw-html:`<input type="date" name="flightDate"/>`
   * - email
     - ``<input type="email" name="emailAddress"/>``
     - Browser validates the value is a valid email address format.
     - :raw-html:`<input type="email" name="emailAddress"/>`
   * - number
     - ``<input type="number" name="fuelTemp"/>``
     - Browser validates the value is a valid number format.
     - :raw-html:`<input type="number" name="fuelTemp"/>`


Clicky Thing Inputs
^^^^^^^^^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - checkbox
     - ``<input type="checkbox" name="fuelChecked"/>``
     - A small box for marking form option as *checked*.
     - :raw-html:`<input type="checkbox" name="fuelChecked"/>`
   * - radio button
     - ``<input type="radio" name="commChannel" value="105"/>``
     - A small circle that allows selecting one of multiple values. Used in groups of two or more.
     - :raw-html:`<input type="radio" name="commChannel" value="105"/>`

Fancy Clicky Thing Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - range
     - ``<input type="range" name="volume"/>``
     - A slider that allows the user to input a numeric value within the given range.
     - :raw-html:`<input type="range" name="volume"/>`
   * - select
     - ``<select name="weather"><option>clear</option><option>cloudy</option></select>``
     - A *drop down* menu that allows selection of one option. Requires options to be in ``<option>`` tags.
     - :raw-html:`<select name="weather"><option>clear</option><option>cloudy</option></select>`


Examples
--------
selectbox
radio buttons
multi checkbox


Check Your Understanding
------------------------
TODO:...
