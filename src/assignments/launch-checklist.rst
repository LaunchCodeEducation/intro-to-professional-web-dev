Assignment #5: Launch Checklist Form
====================================

Requirements
------------

Create a Launch Checklist Form for astronauts to fill out in preparation for launch.
The form should do the following:

1. Validate the form in JS based on responses
2. Validate with JS before the form is submitted and use ``preventDefault`` if form submissions are not valid.
3. Inform the user with validation messages before they submit
4. Use CSS to indicate good/bad responses

Setting Up Your Project Repository
----------------------------------

In the directory where you have been keeping your code for the class, create a new directory for this graded assignment.

Create 3 files in your assignment directory:

1. ``index.html``
2. ``script.js``
3. ``styles.css``

Set up a repository on your Github profile for your assignment and connect to your local directory.

Creating the Form
-----------------

Your form should have the following fields:

1. Pilot's name
2. Copilot's name
3. Fuel levels
4. Cargo weight

Adding Validation
-----------------

The name fields should be text.
The fuel levels need to be a number.
Cargo weight needs to be a number.

If the user submits a form without one or more of the fields filled out, then have a pop up appear that tells the user all fields are required.

If the user submits a fuel level that is too low, let the user know.

If the user submits a cargo weight that is too heavy, let the user know.

Styling the Page
----------------

The launch status should turn red if the flight is not ready.

The launch status should turn green if the flight is ready.
