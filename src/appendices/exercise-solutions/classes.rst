.. _classes-exercise-solutions:

Exercise Solutions: Classes
===========================

1. Construct three classes that hold the information needed by headquarters as
properties. One class should be a ``Book`` class and two
child classes of the ``Book`` class called ``Manual`` and ``Novel``. 
Each class will contain two methods. One will be a constructor. The other one will either be in charge of disposal of the book or updating the property related to the number of times a book has been checked out.
`Hint:` This means you need to read through the requirements for the problem and decide what should belong to ``Book`` and what should belong to the ``Novel`` and
``Manual`` classes. 

.. sourcecode:: js

   class Book {
      constructor(title, author, copyright, isbn, pages, timesCheckedOut, discarded){
         this.title = title;
         this.author = author;
         this.copyright = copyright;
         this.isbn = isbn;
         this.pages = pages;
         this.timesCheckedOut = timesCheckedOut;
         this.discarded = discarded;
      }

      checkout(uses=1) {
         this.timesCheckedOut += uses;
      }
   }

   class Manual extends Book {
      constructor(title, author, copyright, isbn, pages, timesCheckedOut, discarded){
         super(title, author, copyright, isbn, pages, timesCheckedOut, discarded);    
      }

      dispose(currentYear){
         if (currentYear-this.copyright > 5) {
            this.discarded = 'Yes';
         }
      }
   }
  
   class Novel extends Book {
      constructor(title, author, copyright, isbn, pages, timesCheckedOut, discarded){
         super(title, author, copyright, isbn, pages, timesCheckedOut, discarded);
      }
  
      dispose(){
         if (this.timesCheckedOut > 100) {
            this.discarded = 'Yes';
         }
      }
   }

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

.. sourcecode:: js

   let makingTheShip = new Manual('Top Secret Shuttle Building Manual', 'Redacted', 2013, '0000000000000', 1147, 1, 'No');

5. The other book has been checked out 5 times since you first created the
object. Call the appropriate method to update the number of times the book has
been checked out.

.. sourcecode:: js

   goodRead.checkout(5);
   goodRead.dispose();
