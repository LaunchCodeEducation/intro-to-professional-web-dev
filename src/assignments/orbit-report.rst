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

.. sourcecode:: js

   constructor(name: string, type: string, launchDate: string, orbitType: string, operational: boolean)

Now we need to use the ``Satellite`` class to create an initial array of ``Satellite``s.

6. Define an array named ``sourceList`` in ``app.component.ts``.

   * ``sourceList: Satellite[];``
   * For this to compile, you must add ``import { Satellite } from './satellite';`` to the top of the file.

7. In the ``constructor`` in ``app.component.ts`` set ``sourceList`` to be an array of ``Satellite`` objects.

.. sourcecode:: js

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
9. At this point you should see the default Angular starter page. Check the build output and console for any errors.


2) Display Table of Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* create ``orbit-list`` component

  * ``ng g component orbit-list``

* Satellite list (using array first, fetch and json later)

  * In ``ngOnInit`` set ``sourceList`` to be an array that contains satellites created using ``new Satellite()``
  * Set the display list to be a copy of the source list. ``this.displayList = this.sourceList.slice()``

* In ``app.component.html`` pass in the list of satellites to ``<app-orbit-list>`` via ``[satellites]="displayList"``

  * This requires additions of ``@Input() satellites: Satellite;`` in ``OrbitListComponent``

* In orbit list component loop over ``satellites`` using an ``*ngFor``

  * Create a table with each row being a satellite.

* Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into app.component.css
* Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into index.html in a style tag


3) Fetch Satellite Data
^^^^^^^^^^^^^^^^^^^^^^^
* In ``ngOnInit`` in ``AppComponent`` add a ``fetch`` to this URL https://api.myjson.com/bins/103ku9
* Populate ``displayList`` with the results that come back from the fetch
* This replaces the hardcoded array of Satellites you had been using


Highlight Space Debris
^^^^^^^^^^^^^^^^^^^^^^
* Add a ``isSpaceJunk`` method to the ``Satellite`` class.
* Use that method to add a ``waring`` css class to the Type column

  * ``[class.warning]="satellite.isSpaceJunk()"``

Sorting
^^^^^^^
* Add a ``(click)="sort('name')"`` handler to the Name and Type ``<th>`` elements
* Add a ``sort`` function to ``OrbitListComponent``

  * This function will sort the ``satellites`` array in the component

.. sourcecode:: js
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


Searching
^^^^^^^^^
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


Counting Satellites
^^^^^^^^^^^^^^^^^^^
#. Create a ``orbit-counts`` component
#. Copy css from https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6 and put it into orbit-counts.component.css
#. TODO: tell them what to do


Bonus Mission
-------------
Sort feature should also find matches using the ``orbitType`` and ``type`` properties.


Submitting Your Work
--------------------
TODO: do these
