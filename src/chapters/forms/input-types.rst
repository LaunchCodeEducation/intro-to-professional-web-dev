Input Types
===========

As you know from interacting with web forms, it's possible to use more than simple text
inputs. There are additional input *types*, each with different uses. Many of
the elements are ``<input>`` tags with a different ``type`` value, however some have
entirely different tag names.


Basic Text Inputs
-----------------
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
     - ``<input type="text" name="username"/>``
     - A single line text field.
     - :raw-html:`<input type="text" name="username"/>`
   * - textarea
     - ``<textarea name="missionDescription"></textarea>``
     - A larger, multi-line text box. Must have open and closing tags.
     - :raw-html:`<textarea name="missionDescription"></textarea>`
   * - password
     - ``<input type="password" name="passCode"/>``
     - A text field that obscures the text typed by the user.
     - :raw-html:`<input type="password" name="passCode"/>`

.. note::

   Form inputs will NOT look exactly the same in all browsers.
   However, the inputs *should* function the same way. Use `<https://caniuse.com>`_,
   if there is ever a question of browser support for a certain feature.

Basic Examples
--------------
.. admonition:: Example

    .. sourcecode:: html

       <label>Code Name<input type="text" name="codeName"/></label>
       <label>Code Word<input type="password" name="codeWord"/></label>
       <!-- textarea must have open and closing tags -->
       <label>Mission Description<textarea name="description" rows="5"></textarea></label>
       <button>Send Report</button>

    .. figure:: figures/basic-inputs-example.png
       :alt: Form with Code Name, Code Word, and Description field. All fields have values.

    **Submitted Values**

    ::

      codeName=Captain+Danvers&codeWord=avengers!&description=Test+flight.+Plane+maintenance.+Superhero+stuff.

    Notice that the textarea value does NOT include new lines, even thought it was typed that way.


Specialized Text Inputs
-----------------------
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

.. todo:: can the validation be activated in the demo?


Specialized Examples
--------------------
TODO... finish repl.it example https://repl.it/@launchcode/specialized-inputs-example

TODO... use that repl.it to create example admonition


Check Your Understanding
------------------------
TODO...
