Exercises: Classes
===================

Welcome to the space station!
It is your first day onboard and as the newest and most junior member of the crew, you have been asked to organize the library of manuals and fun novels for the crew to read.

Headquarters have asked that you store the following information about each book.

1. The title
2. The author
3. The copyright date
4. The ISBN
5. The number of pages
6. The number of times the book has been checked out.
7. Whether the book has been discarded.

Headquarters also needs you to track certain actions that you must perform when books get out of date.

For a manual, the book must be thrown out if it is over 5 years old.
For a novel, the book should be thrown out if it has been checked out over 100 times.

1. Construct three classes that will hold the information needed from headquarters as properties and the two methods that update the book's property if the book needs to be discarded.
	One class should be a ``book`` class and two child classes of the ``book`` class called ``manual`` and ``novel``.

	`Hint:` This means you need to read through the requirements for the problem and decide what should belong to ``book`` and what should belong to the ``novel`` and ``manual`` classes.

2. Declare an object of the ``novel`` class for the following tome from the library:

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

3. Declare an object of the ``manual`` class for the following tome from the library:

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

4. One of the above books needs to be discarded. Update the property of that book to reflect that the crew is throwing it into empty space to become space debris.
