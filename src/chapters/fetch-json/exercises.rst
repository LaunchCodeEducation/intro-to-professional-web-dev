Exercises
=========

Valid JSON
----------

Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

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

Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

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