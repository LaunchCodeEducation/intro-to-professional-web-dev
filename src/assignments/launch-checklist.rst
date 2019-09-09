Assignment #5: Launch Checklist Form
====================================

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

Fork and clone the repository with the starter code.

Adding Validation
-----------------

Use ``preventDefault()`` and an alert to notify the user if they have not filled out any of the fields.

Use ``preventDefault()`` and an alert to notify the user if they have not entered the correct type of info.
The name fields should be text.
The fuel levels need to be a number.
Cargo weight needs to be a number.

If the user submits a fuel level that is too low (less than 10,000 gallons), let the user know.

If the user submits a cargo weight that is too heavy (more than 10,000 pounds), let the user know.

Styling the Page
----------------

The launch status should turn red if the flight is not ready.

The launch status should turn green if the flight is ready.
