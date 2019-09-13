Assignment #6: Orbit Report
===========================
There are thousands of satellites oribiting the earth. You are tasked with creating a searchable, sortable table of satellites.
For the purposes of this assigment, **satellite** will be defined as any objects that were purposefully placed into orbit.

TODO: screen shot of finished report in the browser with numbers by each feature

1. **Satellites**: Table with each row being a satellite.
2. **Counts:** Count of all satellites and count for each type of satellite.
3. **Search form:** Text entered limits results based on matches. Pressing enter or clicking button triggers search.
4. **Sortable columns:** The name and type column headers can be clicked, which will sort the table using that property.


Setup
-----

1. Create a new project on github named ``orbit-report``.
2. Clone that repo to your computer.
3. Create a new Angular project in the cloned repo folder using this command.

   * ``$ ng new --skip-git orbit-report``
   * It's important to include the ``--skip-git`` because we don't want Angular to create a git repo for us.
   * Prompt answers: No Routing, Use CSS

4. Commit and push your changes to github.


Requirements
------------

1) Define and Create Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In JavaScript, TypeScript, and Angular projects you can create classes to represent entities in the project.
For this project you need to create a class named ``Satellite`` to represent, you guessed it, a satellite. The ``Satellite``
class needs to define the properties needed to accurately represent a satellite.

1. In terminal go to the ``orbit-report`` folder
2. Create a the class with command ``$ ng g class Satellite``
3. Notice that the new file ``orbit-report/src/app/satellite.ts`` was created.
4. Add these properties to the ``Satellite`` class in ``satellite.ts``:

.. sourcecode:: js

   name: string;
   orbitType: string;
   type: string;
   operational: boolean;
   launchDate: string;

5. Add a constructor that has this method signature:

.. sourcecode:: typescript

   constructor(name: string, type: string, launchDate: string, orbitType: string, operational: boolean)

Now we need to use the ``Satellite`` class to create an initial array of ``Satellite`` objects.

6. Define an array named ``sourceList`` in ``app.component.ts``.

   * ``sourceList: Satellite[];``
   * For this to compile, you must add ``import { Satellite } from './satellite';`` to the top of the file.

7. In the ``constructor`` in ``app.component.ts`` set ``sourceList`` to be an array of ``Satellite`` objects.

.. sourcecode:: typescript

   constructor() {
      this.sourceList = [
         new Satellite("SiriusXM", "Communication", "2009-03-21", "LOW", true),
         new Satellite("Cat Scanner", "Imaging", "2012-01-05", "LOW", true),
         new Satellite("Weber Grill", "Space Debris", "2001-11-01", "HIGH", false),
         new Satellite("GPS 938", "Positioning", "2001-11-01", "HIGH", true),
         new Satellite("ISS", "Space Station", "1998-11-20", "LOW", true),
      ];
   }

8. In termainl run ``ng serve``
9. View the app in your browser. At this point you should see the default Angular starter page. If you don't, check the build output and browser console for any errors.


2) Create Orbit List Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now that you have an array of ``Satellite`` objects, you can display them. To do that, you are going to need to create a
new component named ``oribit-list``.

1. Create ``orbit-list`` component using ``$ ng g component orbit-list``
2. Completely wipe out the contents of ``app.component.html``
3. Use ``<app-orbit-list></app-orbit-list>`` in ``app.component.html``
4. View the app in your browser. You should see: orbit-list works!


3) Pass in Satellites to Orbit List Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``orbit-list`` component's job is to show a list of statellites. Rember you declared an array of ``Satellite`` objects in
``app.component.ts`` named ``sourceList``. In order to pass that array into the ``orbit-list``, you need to learn a new Angular
feature named `input properties <https://angular.io/guide/component-interaction#pass-data-from-parent-to-child-with-input-binding>`_.
For the purpose of this feature, the term input refers to data being sent *into* the compoment. Angular input properties are NOT related to HTML ``input``
elements.

Currently ``app.component.html`` uses the ``orbit-list`` component like so:

.. sourcecode:: html+ng2

   <app-orbit-list></app-orbit-list>

To pass in the ``sourceList`` array to the ``orbit-list`` component you need to learn new syntax.
Notice the code ``[satellites]="sourceList"``. The ``[satellites]`` declares that you are setting a
property on the ``orbit-list`` component named ``satellites``. ``="sourceList`` declares that the value
of the ``satellites`` property will be the value of the ``sourceList`` array.

.. sourcecode:: html+ng2

   <app-orbit-list [satellites]="sourceList"></app-orbit-list>

1. Add ``[satellites]="sourceList"`` to ``<app-orbit-list></app-orbit-list>`` in ``app.component.html``.

   * ``<app-orbit-list [satellites]="sourceList"></app-orbit-list>``

2. View the app in your browser.

   * You should NOT see the message "orbit-list worked!". Why?
   
3. Open developer tools in your browser and look at the JavaScript console.

You should see the below error message telling you that the ``orbit-list`` compoment does NOT have a ``satellites`` property.
Note only the relavent message text has been included below.

::

  Error: Template parse errors:
  Can't bind to 'satellites' since it isn't a known property of 'app-orbit-list'.
  1. If 'app-orbit-list' is an Angular component and it has 'satellites' input, then verify that it is part of this module.

To solve this issue, you need to declare in ``orbit-list.component.ts`` that the ``orbit-list`` compoment has an input property named ``satellites``.

4. Add the code below to line 10 of ``orbit-list.component.ts``
   
   * ``@Input() satellites: Satellite[];``

The ``@Input()`` is special Angular syntax that declares that ``satellites`` is a property that will be passed into the component via ``<app-orbit-list [satellites]="sourceList"></app-orbit-list>``.

5. Update the ``require`` statements to import ``Input`` and ``Satellite``

   * ``import { Component, OnInit, Input } from '@angular/core';``
   * ``import { Satellite } from '../satellite';``

6. View the app in your browser. You should see: orbit-list works!

   * You still don't have satellites showing yet. That is the next step.

Your ``orbit-list.component.ts`` should now look like the below.

.. sourcecode:: typescript
   :linenos:

   import { Component, OnInit, Input } from '@angular/core';
   import { Satellite } from '../satellite';

   @Component({
      selector: 'app-orbit-list',
      templateUrl: './orbit-list.component.html',
      styleUrls: ['./orbit-list.component.css']
   })
   export class OrbitListComponent implements OnInit {

      @Input() satellites: Satellite[];

      constructor() { }

      ngOnInit() {
      }

   }


4) Display Table of Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* In orbit list component loop over ``satellites`` using an ``*ngFor``

  * Create a table with each row being a satellite.

* Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into app.component.css
* Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into index.html in a style tag


5) Fetch Satellite Data
^^^^^^^^^^^^^^^^^^^^^^^
* In ``ngOnInit`` in ``AppComponent`` add a ``fetch`` to this URL https://api.myjson.com/bins/103ku9
* Populate ``displayList`` with the results that come back from the fetch
* This replaces the hardcoded array of Satellites you had been using


6) Highlight Space Debris
^^^^^^^^^^^^^^^^^^^^^^^^^
* Add a ``isSpaceJunk`` method to the ``Satellite`` class.
* Use that method to add a ``waring`` css class to the Type column

  * ``[class.warning]="satellite.isSpaceJunk()"``

7) Sorting
^^^^^^^^^^
* Add a ``(click)="sort('name')"`` handler to the Name and Type ``<th>`` elements
* Add a ``sort`` function to ``OrbitListComponent``

  * This function will sort the ``satellites`` array in the component

.. sourcecode:: typescript
   :linenos:

   sort(column: string): void {
    // sort modifies the array, sorting the items based on the given sorting function
    // See: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#Description
    this.satellites.sort(function(a: Satellite, b: Satellite): number {
      if(a[column] < b[column]) {
        return -1;
      } else if (a[column] > b[column]) {
        return 1;
      }
      return 0;
     });
   }


8) Searching
^^^^^^^^^^^^
* Add an input and button to ``app.component.html``

.. sourcecode:: html+ng2

  Search: <input #searchTerm type="text" name="searchTerm"/>

  <button id="searchButton">search</button>

* Add a ``(click)`` handler to the button that calls the ``search(searchTerm.value);``
* Add a ``(keyup.enter)`` to the input that calls the ``search(searchTerm.value);``
* Define a ``search`` function in ``AppComponent``

  * Returns void
  * Takes one parameter ``searchTerm: string``
  * Find matches in ``satellites``
  * Update ``this.displayList`` to be the an array that only conatins matches
  * TODO: define matches. Give them the algorithm. Maybe even give them the code


9) Counting Satellites
^^^^^^^^^^^^^^^^^^^^^^
#. Create a ``orbit-counts`` component
#. Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into orbit-counts.component.css
#. TODO: tell them what to do


Bonus Mission
-------------
Search feature should also find matches using the ``orbitType`` and ``type`` properties.


Submitting Your Work
--------------------
TODO: do these
