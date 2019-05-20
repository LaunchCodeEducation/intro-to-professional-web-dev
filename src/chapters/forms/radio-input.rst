Radio Input
===========

Radio inputs allow a user to pick one option out of a grouping of options.  Radio inputs with the
same name are considered in a group. Only one radio input in a group can be chosen at a time.
The ``value`` attribute of the chosen radio input
will be submitted. Radio inputs are best used with ``<label>`` tags.


Syntax/Description
------------------

.. role:: raw-html(raw)
   :format: html

.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - radio
     - ``<input type="radio" name="crewReady" value="yes"/>``
     - A small circle that allows selecting *one* of multiple values. Used in groups of two or more.
     - :raw-html:`<label>yes<input type="radio" name="crewReady" value="yes"/></label><label>no<input type="radio" name="crewReady" value="no"/></label>`


Examples
--------
.. admonition:: Example

    .. sourcecode:: html

       Flight Rating:
       <label>Rough<input type="radio" name="flightRating" value="rough"/></label>
       <label>Few Bumps<input type="radio" name="flightRating" value="fewBumps"/></label>
       <label>Smooth<input type="radio" name="flightRating" value="smooth"/></label>

    .. figure:: figures/radio-inputs-example.png
       :alt: Form for flight rating, with a radio inputs for rough, few bumps, and smooth.

    **Submitted Values**

    ::

      flightRating=smooth 

    `Run it <https://repl.it/@launchcode/radio-inputs-example>`_


Check Your Understanding
------------------------
.. admonition:: Question

   Should a group of radio inputs have the same value for the ``name`` attribute?
