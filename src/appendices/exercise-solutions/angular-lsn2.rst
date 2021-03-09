.. _angular-lsn2-exercise-solutions:

Exercise Solutions: Angular, Lesson 2
=====================================

.. _angular-lsn2-exercise-solutionsA:

A. **Candidates Column**

   #. Use ``*ngFor`` in the ``<li>`` tag to loop over the candidates array and display each name in an ordered list.

      .. sourcecode:: html+ng2
         :linenos:

         <div class="candidates col-3">
            <h2>Candidates</h2>
            <ol>
               <li *ngFor="let candidate of candidates" (click)="selected = candidate">{{candidate.name}}</li>
            </ol>
         </div>

:ref:`Back to the exercises <exercises-angular-lsn2-candidates-column>`


B. **Candidate Data Column**

   .. _angular-lsn2-exercise-solutionsB1:

   #. Add labels in the html for a candidate's name, age, mass, and sidekick data.

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

   .. _angular-lsn2-exercise-solutionsB3:

   3. Use ``*ngIf`` to check if a candidate has been selected. If so, display the labels and the data.

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

C. **Sidekick Image Column**

   #. In the ``<img>`` tag, use ``*ngIf`` to check if a candidate has been selected.

      .. sourcecode:: html+ng2
         :linenos:

         <div class="centered col-3">
            <h2>Sidekick</h2>
            <div *ngIf = "selected">
               <img src="{{placeholder}}" alt="Oops! Missing photo!"/>
            </div>
         </div>

:ref:`Back to the exercises <exercises-angular-lsn2-sidekick-image-column>`