Checkbox Input
==============

TODO:.. A few classy words about checkbox

Checkbox
--------

.. role:: raw-html(raw)
   :format: html

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

TODO:.. remove radio from this table


Examples
--------

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


Check Your Understanding
------------------------
TODO...
