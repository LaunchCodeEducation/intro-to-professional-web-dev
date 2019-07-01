Data Formats and JSON
=====================

.. index:: ! Data format

In order for our application to make a request to an API, the data will need to be formatted in a
way both our application and the API can understand.

The API may have been built with another programming language, and it may not use the same variables,
objects, and data structures as JavaScript. To solve the issue of APIs being built in different
programming languages Data Formats are used.

A **data format** is a set of rules that govern how data is written, organized, and labeled.
Data formats make working with data consistent and reliable.

JSON
----

.. index:: ! JSON

.. index::
   single: JSON; JavaScript Object Notation


There are quite a few different data formats, but we will only focus on one throughout this
class: **JavaScript Object Notation**, also known as **JSON**. JSON
is one of the leading data formats used, especially on the web.

JSON is based on JavaScript object syntax, but has some differences.

Let's consider an API that serves information about the books in a library. In this example we searched
for "An Astronaut's guide to life on Earth".

.. sourcecode:: js
   :linenos:

   {
       "title": "An Astronaut's guide to life on Earth",
       "author": "Chris Hadfield",
       "ISBN": 9780316253017,
       "year_published": 2013,
       "subject": ["Hadfield, Chris", "Astronauts", "Biography"],
       "available": true
   }

The API returned a match for our search. The search provides us with information that may be useful to the user in the
form of the title, author, ISBN, the year the book was published, the subjects of the book, and if the book is currently
available for checkout.

JSON Rules
----------

JSON is a collection of key value pairs. In the example above ``"title"`` is a key, and it's value is
``"An Astronaut's guide to life on Earth"``.

The key value pairs describe the data that is being transferred.

A JSON key MUST be a string, but the value may be a number, string, boolean, array, object, or null.

In the example above the JSON describes one object, a book! All of the keys are strings, and the values
are: string, string, number, number, array, and boolean respectively.

JSON can also be used to describe a collection of objects at the same time. Consider we search for
the word "Astronaut".

.. sourcecode:: js
   :linenos:

   {
       "hits": 3,
       "book": [
           {
               "title": "An Astronaut's guide to life on Earth",
                "author": "Chris Hadfield",
                "ISBN": 9780316253017,
                "year_published": 2013,
                "subject": ["Hadfield, Chris", "Astronauts", "Biography"],
                "available": true
           },
           {
               "title": "Astronaut",
               "author": "Lucy M. George",
               "ISBN": 9781609929411,
               "year_published": 2016,
               "subject": ["Astronauts", "Juvenille Fiction", "Space stations"],
               "available": false
           },
           {
               "title": "Astronaut Ellen Ochoa",
               "author": "Heather E. Schwartz",
               "ISBN": 9781512434491,
               "year_published": 2018,
               "subject": ["Ochoa Ellen", "Women astronauts", "Astronauts", "Biography", "Women scientists", "Hispanic American women"],
               "available": true
           }
       ]
   }

This time our search term "Astronaut" returned multiple books, and so a collection of book objects was returned in JSON format.

Each book object can be found in the array with the key ``"book"``. Each book contains the keys title, author, ISBN, year_published,
subject, and available.

When we make a request to an API, the API formats the data we requested into JSON, and then responds to our request with the
JSON representation of our request.


JSON & JavaScript Object Differences
------------------------------------

JSON is based on how JavaScript objects work. However, there are some key differences between the two.

JSON keys MUST be in double quotes. When defining properties for a JavaScript object double quotes should not be used when
declaring properties.

JSON

.. sourcecode:: js
   :linenos:

   {
       "title": "The Cat in the Hat"
       "author": "Dr. Seuss"
   }

JavaScript object

.. sourcecode:: js
   :linenos:

   let newBook = {
       title: "The Cat in the Hat",
       author: "Dr. Seuss"
   }

To represent a string in JSON you MUST use double quotes. In JavaScript you can use double quotes, or single quotes.

JSON

.. sourcecode:: js
   :linenos:

   {
       "title": "The Last Astronaut",
       "author": "David Wellington"
   }

JavaScript object

.. sourcecode:: js
   :linenos:

   let anotherBook = {
       title: 'The Last Astronaut',
       author: 'David Wellington'
   }

.. note::

   JSON is based on JavaScript objects, but there are key differences. JSON syntax is a little more strict than JavaScript
   object syntax.

Check Your Understanding
------------------------

.. admonition:: Question

   What does API stand for?

.. admonition:: Question

   Why might you connect to an API?

.. admonition:: Question

   What is JSON?

.. admonition:: Question

   What purpose does JSON serve?
