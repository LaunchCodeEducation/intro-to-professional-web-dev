Data Binding
=============

In the previous two Angular lessons, you *stored* data in a ``component.ts``
file, and then *displayed* that data in a ``component.html`` file.

.. admonition:: Example

   Assign a ``listHeading`` variable and a ``movies`` array in the
   ``movie-list.component.ts`` file:

   .. sourcecode:: typescript
      :linenos:

      export class MovieListComponent implements OnInit {
         listHeading: string = "Oscar Winners to Watch";
         movies: string[] = ['Titanic', 'Gladiator', 'Mutiny on the Bounty', 'The Silence of the Lambs'];

         constructor() { }

         ngOnInit() { }

      }

   Display the list heading and the titles from the ``movies`` array using the
   ``movie-list.component.html`` file:

   .. sourcecode:: html+ng2
      :linenos:

      <div class='movies'>
         <h3>{{listHeading}}</h3>
         <ol>
            <li *ngFor = 'let movie of movies'>{{movie}}</li>
         </ol>
      </div>

.. index:: ! data binding, ! view

Each Angular component contains an HTML file that organizes the content users
see in their web browsers. We call these files the **view**.

**Data binding** refers to the technique of linking information contained in
a file to the view. In the example above, data contained in the
``movie-list.component.ts`` file is *bound* to placeholders in the
``movie-list.component.html`` file.

By binding ``listHeading`` and ``movies``, we are telling Angular to watch them
for changes. Whenever the variables in ``movie-list.component.ts``
change in value, Angular responds by automatically updating the HTML file.

Data binding is a powerful technique, since it allows developers to focus on
the fun part of the code rather than dealing with all the nitty-gritty
"ugh-I-need-to-add-statements-here-here-and-here-to-refresh-the-page".

Fortunately, you already experienced setting up data binding in Angular, so the
groundwork is done. In this chapter, we will continue practicing the skill, add
in the vocabulary, and explore some refinements.
