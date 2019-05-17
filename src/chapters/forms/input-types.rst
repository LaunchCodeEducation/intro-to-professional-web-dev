Input Types
===========

As you know from using the web sites, it's possible to use more than simple text inputs. There
are additional input *types* that each have a specific purpose. Many of the elements are
``<input>`` tags with a different ``type`` value, however some have entirely different tag names.

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

On or Off Inputs
----------------

.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - checkbox
     - ``<input type="checkbox" name="signUp"/>``
     - A small box for marking form option as *checked*.
     - :raw-html:`<label>sign up<input type="checkbox" name="signUp"/></label>`
   * - radio
     - ``<input type="radio" name="crewReady" value="yes"/>``
     - A small circle that allows selecting *one* of multiple values. Used in groups of two or more.
     - :raw-html:`<label>yes<input type="radio" name="crewReady" value="yes"/></label><label>no<input type="radio" name="crewReady" value="no"/></label>`

**Check Box Usage**

Checkbox inputs are great for two scenarios:

1. A yes/no question
2. A question with zero, one, or multiple answers

.. admonition:: Example

    One checkbox. No ``value`` attribute is set, so the default value of ``on`` is submitted.

    .. sourcecode:: html

       <label>crew<input type="checkbox" name="crewReady"/></label>

    **Submitted** (if checked)

    ::

      crewReady=on

.. admonition:: Example

    Multiple checkbox inputs. All with *different* ``name`` attributes.

    .. sourcecode:: html

       <div>Activities</div>
       <label>cooking<input type="checkbox" name="cooking"/></label>
       <label>running<input type="checkbox" name="running"/></label>
       <label>movies<input type="checkbox" name="movies"/></label>

    **Submitted** (if cooking and movies are checked)

    ::

      cooking=on&movies=on


.. admonition:: Example

    Multiple checkbox inputs with the SAME ``name`` attribute.

    .. sourcecode:: html

       <div>Ingredients</div>
       <label>Onion<input type="checkbox" name="ingredient" value="onion"/></label>
       <label>Butter<input type="checkbox" name="ingredient" value="butter"/></label>
       <label>Rice<input type="checkbox" name="ingredient" value="rice"/></label>

    **Submitted** (if butter and rice are checked)

    ::

      ingredient=butter&ingredient=rice


Defined Option Inputs
---------------------
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


Check Your Understanding
------------------------
TODO...
