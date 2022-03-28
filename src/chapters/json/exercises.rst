.. _exercises-JSON:

JSON
----

1. Which of the following three code snippets is correct JSON syntax? Why are the other two options incorrect?

   a. 
      .. sourcecode:: js

         {
            type: "dog",
            name: "Bernie",
            age: 3
         }

   b. 

      .. sourcecode:: js

         {
            "type": "dog",
            "name": "Bernie",
            "age": 3
         }
   
   c.

      .. sourcecode:: js

         {
            "type": 'dog',
            "name": 'Bernie',
            "age": 3
         }

   :ref:`Check your solution <JSON-exercise-solutions1>`. 

2. Which of the following three code snippets is correct JSON? Why are the other two options incorrect?

   a.

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

   b.

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

   c.

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
