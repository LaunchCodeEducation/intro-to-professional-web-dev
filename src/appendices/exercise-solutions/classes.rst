.. _classes-exercise-solutions:

Exercise Solutions: Classes
===========================

.. _classes-exercise-solutions1:

1. Construct three classes that hold the information needed by headquarters as
properties. One class should be a ``Book`` class and two
child classes of the ``Book`` class called ``Manual`` and ``Novel``. 
Each class will contain two methods. One will be a constructor. The other one will either be in charge of disposal of the book or updating the property related to the number of times a book has been checked out.
`Hint:` This means you need to read through the requirements for the problem and decide what should belong to ``Book`` and what should belong to the ``Novel`` and
``Manual`` classes. 

   .. sourcecode:: js
      :linenos:

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

.. _classes-exercise-solutions3:

3. Declare an object of the ``Manual`` class for the given tome from the
library.

   .. sourcecode:: js

      let makingTheShip = new Manual('Top Secret Shuttle Building Manual', 'Redacted', 2013, '0000000000000', 1147, 1, 'No');

.. _classes-exercise-solutions5:
   
5. The other book has been checked out 5 times since you first created the
object. Call the appropriate method to update the number of times the book has
been checked out.

   .. sourcecode:: js

      goodRead.checkout(5);
      goodRead.dispose();
