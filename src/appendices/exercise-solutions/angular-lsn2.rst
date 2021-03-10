.. _angular-lsn2-exercise-solutions:

Exercise Solutions: Angular, Lesson 2
=====================================

.. _angular-lsn2-exercise-solutionsA:

Candidates Column
-----------------

#. Use ``*ngFor`` in the ``<li>`` tag to loop over the candidates array and display each name in an ordered list.


   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html+ng2
      :linenos:

      <div class="candidates col-3">
         <h2>Candidates</h2>
         <ol>
            <li *ngFor="let candidate of candidates" (click)="selected = candidate">{{candidate.name}}</li>
         </ol>
      </div>

:ref:`Back to the exercises <exercises-angular-lsn2-candidates-column>`


Candidate Data Column
---------------------

.. _angular-lsn2-exercise-solutionsB1:

#. Add labels in the html for a candidate's name, age, mass, and sidekick data.

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html
      :linenos:

      <div class="data col-3">
         <h2>Candidate Data</h2>
         <p>
            Name: <br>
            Age: <br>
            Mass: <br>
            Sidekick: 
         </p>
      </div>

   :ref:`Back to the exercises <exercises-angular-lsn2-candidate-data-column>`

.. _angular-lsn2-exercise-solutionsB3:

3. Use ``*ngIf`` to check if a candidate has been selected. If so, display the labels and the data.

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html+ng2
      :linenos:

      <div class="data col-3">
         <h2>Candidate Data</h2>
         <p *ngIf="selected">
            Name: {{selected.name}} <br>
            Age: {{selected.data.age}} <br>
            Mass: {{selected.data.mass}} <br>
            Sidekick: {{selected.data.sidekick}}
         </p>
      </div>

   :ref:`Back to the exercises <exercises-angular-lsn2-candidate-data-column>`

.. _angular-lsn2-exercise-solutionsC:

Sidekick Image Column
---------------------

#. In the ``<img>`` tag, use ``*ngIf`` to check if a candidate has been selected.

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html+ng2
      :linenos:

      <div class="centered col-3">
         <h2>Sidekick</h2>
         <div *ngIf = "selected">
            <img src="{{placeholder}}" alt="Oops! Missing photo!"/>
         </div>
      </div>

:ref:`Back to the exercises <exercises-angular-lsn2-sidekick-image-column>`


Selected Crew Column
--------------------

.. _angular-lsn2-exercise-solutionsD1:

#. Start an ``addToCrew`` function that takes an object as a parameter.

   ``src/app/candidates/candidates.component.ts``:

   .. sourcecode:: ts
      :linenos:

      addToCrew(person: object) {
         //TODO: complete the function!
      }

   :ref:`Back to the exercises <exercises-angular-lsn2-selected-crew-column>`

.. _angular-lsn2-exercise-solutionsD3:

3. Add a "Send on Mission" button next to the "Clear Data & Image" button.

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html 
      :linenos:

      <div class="centered">
         <button> Clear Data and Image </button>
         <button> Send on Mission </button>
      </div>

   :ref:`Back to the exercises <exercises-angular-lsn2-selected-crew-column>`

.. _angular-lsn2-exercise-solutionsD5:

5. Under the "Selected Crew" section, use ``*ngFor`` to display each crew member's name.

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html+ng2
      :linenos:

      <h2>Selected Crew</h2>
      <ul>
         <li *ngFor = "let member of crew">{{member.name}}</li>
      </ul>

   :ref:`Back to the exercises <exercises-angular-lsn2-selected-crew-column>`

.. _angular-lsn2-exercise-solutionsD7:

7. Use ``*ngIf`` to conditionally show the "Clear Crew List" button when the crew array contains data. 

   ``src/app/candidates/candidates.component.html``:

   .. sourcecode:: html+ng2

      <button *ngIf = "crew.length !== 0">Clear Crew List</button>

   :ref:`Back to the exercises <exercises-angular-lsn2-selected-crew-column>`
