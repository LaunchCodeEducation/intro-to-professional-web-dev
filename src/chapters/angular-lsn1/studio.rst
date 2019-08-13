Studio: Angular, Part 1
===============================
In this chapter, you learned about the Angular file structure, templates, and
components. Over the next three classes, you will build a Mission Planning Dashboard
using your Angular skills.


Mission Planning Dashboard
--------------------------
A useful and common front end application is a *dashboard*. It shows quick
information about a topic, so individuals using the web app can be well
informed and make good decisions.

You will create a Space Mission Planning Dashboard.


Setup
-----
1. Fork the Angular Lesson 1 Studio repository.
2. Clone your fork to your computer.
3. Verify that you are on branch ``studio-1``.

   * Note ``studio-1`` this is a mostly empty branch.

Create Angular Project
^^^^^^^^^^^^^^^^^^^^^^
4. Open a terminal at the root of the ``angular-lc101-mission-planner`` repository you just cloned.
5. Create a new Angular project by running ``ng new mission-dashboard``.

   #. When prompted about using routing, enter "N" for No.
   #. When prompted to select the stylesheet format, select CSS.

::

   your-computer:angular-lc101-mission-planner $ ng new mission-dashboard
   ? Would you like to add Angular routing? No
   ? Which stylesheet format would you like to use? CSS

6. Navigate into the new folder by running ``cd mission-dashboard``
7. Install dependencies by running ``npm install``
8. Verify that the application will run by running ``ng serve``
9. View the site in your browser at http://localhost:4200

   * You should see a header that says "Welcome to mission-dashboard!"

10. Stage and commit the files before starting on the features.

Requirements
------------
The mission dashboard you are creating will eventually look like this.

.. figure:: ./figures/example-mission-dashboard.png
   :alt: Screen shot showing the mission dashboard with mission name, rocket name, crew members, equipment, and experiments.

Header Component
^^^^^^^^^^^^^^^^
1. Create a ``app-header`` component using ``ng g header``.
2. In file ``/mission-dashboard/src/app/header/header.component.html`` add HTML:

.. sourcecode:: html+ng2
   :linenos:

   <h1>Mission Planning Dashboard</h1>
   <h3>Mission Name: {{ missionName }}</h3>
   <h3>Carrier Rocket: {{ rocketName }}</h3>

TOOD: add variables to component

#. A list that displays the names of the crew
#. A list that displays crew member roles
#. A list that displays required equipment
#. A list that displays the countries represented by the crew

Make the three lists align by adding this CSS to ``studios/angular-part1/src/app/app.component.css``.

Each section needs to be it's own component, and they all need to be placed
within the ``app`` folder.

In the next two studios we will learn how to expand this project by using more
Angular tools that will make the application more interactive. For the purposes
of today's studio our web application will not be interactive, and will simply
display static information.


Bonus Mission
-------------

#. Add CSS to change add different colors, fonts, borders, etc. to your
dashboard.
#.Be creative! Make your components look good.
