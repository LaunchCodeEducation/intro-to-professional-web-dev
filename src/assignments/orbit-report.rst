Assignment #6: Orbit Report
===========================
TODO: Summary of the assignment. Define satellite.

TODO: screen shot of finished report in the browser

Setup
-----
* create a new project on github named ``orbit-report``
* clone that repo to your computer
* create a new angular project in that cloned repo folder

  * ``$ ng new orbit-report``
  * (put answers to prompted questions: css, no routing)
* push your changes to your remote repo

Requirements
------------

Define and Create Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* create ``Satellite`` class

  * I'm not 100% sure on the properites yet

* Define arrays of Satellites in ``src/app/app.component.ts``

  * ``displayList: Satellite[];``
  * ``sourceList: Satellite[];``


Display Table of Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* create ``orbit-list`` component

  * ``ng g component orbit-list``

* Add this CSS to file ``orbit-list.component.css``

.. sourcecode:: html

  .sortable {
      cursor: pointer;
      color: #dd5;
  }

  .warning {
      background-color: #da8a8a;
  }

  table {
    color: #111;
    border-radius: .4em;
    overflow: hidden;
    margin: 1em 0;
    min-width: 300px;
    background: #dad8d8;
  }

  .header-row {
      background: #34495E;
      color: #fff
  }

  th, td {
      text-align: left;
      margin: .5em 1em;
      padding: 1em;
  }


* Satellite list (using array first, fetch and json later)

  * In ``ngOnInit`` set ``sourceList`` to be an array that contains satellites created using ``new Satellite()``
  * Set the display list to be a copy of the source list. ``this.displayList = this.sourceList.slice()``

* In ``app.component.html`` pass in the list of satellites to ``<app-orbit-list>`` via ``[satellites]="displayList"``

  * This requires additions of ``@Input() satellites: Satellite;`` in ``OrbitListComponent``

* In orbit list component loop over ``satellites`` using an ``*ngFor``

  * Create a table with each row being a satellite.


Highlight Space Junk
^^^^^^^^^^^^^^^^^^^^
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


Fetch Satellite Data
^^^^^^^^^^^^^^^^^^^^
* In ``ngOnInit`` in ``AppComponent`` add a ``fetch`` to this URL https://api.myjson.com/bins/103ku9
* Populate ``displayList`` with the results that come back from the fetch
* This replaces the hardcoded array of Satellites you had been using

Bonus Mission
-------------
TODO: do these


Submitting Your Work
--------------------
TODO: do these
