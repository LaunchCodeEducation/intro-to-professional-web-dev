Exercises: Classes
===================

Welcome to the space station!
It is your first day onboard and as the newest and most junior member of the
crew, you have been asked to organize the library of manuals and fun novels for
the crew to read. Click on this
`repl.it link <https://repl.it/@launchcode/ClassExercises01>`__ and fork the
starter code.

Headquarters have asked that you store the following information about each
book.

1. The title
2. The author
3. The copyright date
4. The ISBN
5. The number of pages
6. The number of times the book has been checked out.
7. Whether the book has been discarded.

Headquarters also needs you to track certain actions that you must perform when
books get out of date. First, for a manual, the book must be thrown out if it
is over 5 years old. Second, for a novel, the book should be thrown out if it
has been checked out over 100 times.

1. Construct three classes that hold the information needed by headquarters as
properties. One class should be a ``Book`` class and two
child classes of the ``Book`` class called ``Manual`` and ``Novel``. 
Each class will contain two methods. One will be a constructor. The other one will either be in charge of disposal of the book or updating the property related to the number of times a book has been checked out.
`Hint:` This means you need to read through the requirements for the problem and decide what should belong to ``Book`` and what should belong to the ``Novel`` and
``Manual`` classes. 

:ref:`Check your solution <classes-exercise-solutions1>`

2. Declare an object of the ``Novel`` class for the following tome from the
library:

.. list-table:: Novel
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - Title
     - Pride and Prejudice
   * - Author
     - Jane Austen
   * - Copyright date
     - 1813
   * - ISBN
     - 1111111111111
   * - Number of pages
     - 432
   * - Number of times the book has been checked out
     - 32
   * - Whether the book has been discarded
     - No

3. Declare an object of the ``Manual`` class for the following tome from the
library:

.. list-table:: Manual
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - Title
     - Top Secret Shuttle Building Manual
   * - Author
     - Redacted
   * - Copyright date
     - 2013
   * - ISBN
     - 0000000000000
   * - Number of pages
     - 1147
   * - Number of times the book has been checked out
     - 1
   * - Whether the book has been discarded
     - No

:ref:`Check your solution <classes-exercise-solutions3>`

4. One of the above books needs to be discarded. Call the appropriate method
for that book to update the property. That way the crew can throw it into empty
space to become debris.

5. The other book has been checked out 5 times since you first created the
object. Call the appropriate method to update the number of times the book has
been checked out.

:ref:`Check your solution <classes-exercise-solutions5>`