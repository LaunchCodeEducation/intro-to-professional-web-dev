Assignment #5: Launch Checklist Form
====================================

Using our knowledge of forms, the DOM, and HTTP, our favorite space shuttle program has asked us to create a quick launch checklist.
We have four fields that need to be filled out with vital information: the pilot's name, the co-pilot's name, the fuel levels, and the weight of the cargo.

Our pilot, Chris, and their co-pilot, Blake, have been hard at work securing the cargo and filling the shuttle tank. All we need to do is use validation to insure that we have all of the info for the space shuttle program and make sure no one prematurely launches the shuttle.

Requirements
------------

Create a Launch Checklist Form for astronauts to fill out in preparation for launch.
The form should do the following:

1. Validate the user responses with ``preventDefault()`` to insure the following:

   1. The user has entered something for every field.
   2. The user has entered text for names and numbers for fuel and cargo levels.

2. With validation, update a listing of what is currently ready for shuttle launch and not.
3. Use CSS to indicate what is good and bad about the shuttle and whether it is ready for launch. 

Setting Up Your Project Repository
----------------------------------

Fork the repository with the `starter code <https://github.com/LaunchCodeEducation/Launch-Checklist-Form/>`_ to your personal Github profile and clone the repository to the directory where you are keeping your assignments for the class.

.. note::

   When updating styles to indicate whether the shuttle is ready for launch, do not modify ``styles.css``!

Adding Validation
-----------------

Adding Alerts
^^^^^^^^^^^^^

First, let's add the validation to notify the user if they have forgotten to enter a value for any one of the fields.

This process is going to look similar to the :ref:`validation section <javascript-validation>` in the chapter on forms. 
Make sure to use ``preventDefault()`` and an alert to notify the user that all fields are required.

You also want to make sure that the user has entered valid info for each of the fields.
Valid information for the fields means that the user has entered a value that is easily converted to the correct data type for our fellow engineers.
The pilot and co-pilot names should be strings and the fuel level and cargo weight should be numbers.

.. note:: 

   If you want to check if something is ``NaN``, you cannot use ``==`` or ``===``.
   JavaScript does have a built-in method called ``isNaN(value)`` where it returns ``true`` if ``value`` is ``NaN`` and ``false`` if ``value`` is not ``NaN``.

Updating Shuttle Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list of shuttle requirements, ``"faultyItems``, should be updated if something is not ready for launch. 
Using template literals, update ``pilotStatus`` and ``copilotStatus`` to include the pilot's name and the co-pilot's name.

If the user submits a fuel level that is too low (less than 10,000 gallons), change the list to visible with an updated fuel status stating that there is not enough fuel for the journey.
The text of ``launchStatus`` should also change to let the user know that the shuttle is not ready for launch and become red.

If the user submits a cargo weight that is too heavy (more than 10,000 pounds), change the list to visible with an updated cargo status stating that there is too much weight for the shuttle to take off.
The text of ``launchStatus`` should also change to let the user know that the shuttle is not ready for launch and become red.

If the shuttle is ready to launch, change ``launchStatus`` to the shuttle is ready for launch and make the status green. The list should also become visible.

The End Result
--------------

After you implement everything, the following form submission would result in the proper updates to the ``launchStatus`` and ``faultyItems`` list.

.. figure:: figures/form-fields-ready.png
   :alt: Image showing the user is submitting a form with Chris as the pilot, Blake as the co-pilot, 890 gallons as the fuel level, and 178 pounds as the cargo weight.

With only 890 gallons of fuel, the status of the launch becomes red and states that the shuttle is not ready. 
The list has also updated to indicate that that is not enough fuel for the shuttle to launch.

.. figure:: figures/form-submission-result.png
   :alt: Image showing the updates to the faulty items list and the launch status.