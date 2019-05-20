Input Types
===========

As you know from interacting with web forms, it's possible to use more than simple text
inputs. There are additional input *types*, each with different uses. Many of
the elements are ``<input>`` tags with a different ``type`` value, however some have
entirely different tag names.


Text Inputs
-----------
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

Example
-------
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

    `Run it <https://repl.it/@launchcode/basic-inputs-example>`_


Check Your Understanding
------------------------

.. admonition:: Question

   Which input type should be used if the user is going to enter a large amount of text?
