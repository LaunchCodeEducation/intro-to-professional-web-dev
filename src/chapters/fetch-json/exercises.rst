Exercises
=========

JSON
----

1. Which of the following three code snippets is correct JSON syntax? Why are the other two options incorrect?

.. sourcecode:: js

   {
       type: "dog",
       name: "Bernie",
       age: 3
   }

.. sourcecode:: js

   {
       "type": "dog",
       "name": "Bernie",
       "age": 3
   }

.. sourcecode:: js

   {
       "type": 'dog',
       "name": 'Bernie',
       "age": 3
   }

2. Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

.. sourcecode:: js

   {
       "animals": [
           {
               "type": "dog",
               "name": "Bernie",
               "age": 3
           },
           {
               "type": "cat",
               "name": "Draco",
               "age": 2
           }
       ]
   }

.. sourcecode:: js

   {
       [
          {
               "type": "dog",
               "name": "Bernie",
               "age": 3
           },
           {
               "type": "cat",
               "name": "Draco",
               "age": 2
           } 
       ]
   }

.. sourcecode:: js

   [
        {
            "type": "dog",
            "name": "Bernie",
            "age": 3
        },
        {
            "type": "cat",
            "name": "Draco",
            "age": 2
        } 
    ]


Fetch
-----

.. todo:: add exercises for fetch
Make a request to an API using fetch
Handle a response from an API
Update the web page using data from a response
Understand the asynchronous cycle of network requests
Familiar with terms AJAX and XHR (XmlHttpRequest)