JSON
====

JavaScript Object Notation (JSON) is one of the leading data formats used especially on the web.

JSON is based on JavaScript object syntax, but has some differeneces.

Let's consider an API that serves information about the books in a library. In this example we searched for "An Astronaut's guide to life on Earth".

.. sourcecode:: js

   {
       "title": "An Astronaut's guide to life on Earth",
       "author": "Chris Hadfield",
       "ISBN": 9780316253017,
       "year_published": 2013,
       "subject": ["Hadfield, Chris", "Astronauts", "Biography"],
       "available": true
   }

The API returned a match for our search. The search provides us with information that may be useful to the user in the form of the title, author, ISBN, the year the book was published, the subjects of the book, and if the book is currently available for checkout.

JSON Rules
----------

JSON is a collection of key value pairs. In the example above "title" is a key, and it's value is "An Astronaut's guide to life on Earth"

The key value pairs descirbe the data that is being transferred.

A JSON key must always be a string, but the value may be a number, string, boolean, array, object, or null.

In the example above the JSON describes one object, a book! All of the keys are strings, and the values are: string, string, number, number, array, and boolean respectively.

JSON can also be used to describe a collection of objects at the same time. Consider we search for the word "Astronaut".

.. sourcecode:: js

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

Each book object can be found in the array with the key "book". Each book contain the keys title, author, ISBN, year_published, subject, and available.

When we make a request to an API, the API formats the data we requested into JSON, and then responds to our request with the JSON representation of our request.

JSON is one of the leading data formats used in web development, and is the data format we will use throughout this course. In the next section we will show you how to use the ``fetch()`` method to make a request to an API that will return a JSON representation of the data we requested.

JSON & JavaScript Object Differences
------------------------------------

JSON is based on how JavaScript objects work. However, there are some key differences between the two.

JSON keys **must** be in double quotes. When defining properties for a JavaScript object double quotes should not be used when declaring properties.

.. sourcecode:: js
   :caption: JSON

   {
       "title": "The Cat in the Hat"
       "author": "Dr. Seuss"
   }

.. sourcecode:: js
   :caption: JavaScript object

   let newBook = {
       title: "The Cat in the Hat",
       author: "Dr. Seuss"
   }

To represent a string in JSON you must use double quotes. In JavaScript you can use double quotes, or single quotes.

.. sourcecode:: js
   :caption: JSON

   {
       "title": "The Last Astronaut",
       "author": "David Wellington"
   }

.. sourcecode:: js
   :caption: JavaScript object

   let anotherBook = {
       title: 'The Last Astronaut',
       author: 'David Wellington'
   }

.. note::

   JSON is based on JavaScript objects, but there are key differences. JSON syntax is a little more strict than JavaScript object syntax. Luckily JavaScript has built in tools to turn JSON into a JavaScript object with relative ease. These tools will be introduced later in the course.

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