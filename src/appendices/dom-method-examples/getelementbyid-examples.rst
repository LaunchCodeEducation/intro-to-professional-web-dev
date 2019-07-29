.. _dom-getelementbyid-examples:

``getElementById`` Examples
===========================

The general syntax for this method is:

.. sourcecode:: js

   let element = document.getElementById("element-id");

Searches the HTML document for an element that has an *id* attribute that matches the string
parameter. Returns a reference to the matching element object if match found. If NO matching
element is found, ``null`` is returned.


.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
         </head>
         <body>
            <h1>getElementById Example</h1>
            <p id="description">
               This will be turned blue.
            </p>
            <script>
               let paragraph = document.getElementById("description");
               console.log("paragraph contents:", paragraph.innerHTML.trim());
               paragraph.style.color = "blue";
            </script>
         </body>
      </html>

   **Console Output**

   ::

      paragraph contents: This will be turned blue.


.. tip::

   Because ``getElementById`` returns ``null`` if an element with a matching id can NOT be found, you
   could see a message like ``TypeError: paragraph is null``. Be sure to double check the id you are using
   in JavaScript and in the HTML.
