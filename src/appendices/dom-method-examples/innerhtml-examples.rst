.. _dom-innerHTML-examples:

**innerHTML** Examples
======================

The general syntax for this method is:

.. sourcecode:: js

   element.innerHTML

The innerHTML property of elements *reads* and *update* the HTML and or text that is
inside the element.

.. note::

   The ``innerHTML`` value for empty elements is empty string ``""``.

.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
         </head>
         <body>
            <h1>innnerHTML Example</h1>

            <h2>Yellow Fruits</h2>
            <ul class="yellow">
               <li>Banana</li>
            </ul>

            <script>
               let ul = document.querySelector(".yellow");
               console.log(ul.innerHTML.trim());
            </script>
         </body>
      </html>

   **Console Output**

   ::

      <li>Banana</li>


.. tip::

   Use ``.trim`` to remove the whitespace around the value of ``.innerHTML``

As mentioned above ``innerHTML`` can be used to read and *update* the contents of an element.
``innerHTML`` is so powerful that you can pass in strings of HTML.

.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
         </head>
         <body>
            <h1>innnerHTML Example</h1>

            <h2>Yellow Fruits</h2>
            <ul class="yellow">
               <li>Banana</li>
            </ul>

            <script>
               let ul = document.querySelector(".yellow");
               // Add a <li> to the list
               ul.innerHTML += "<li>Lemon</li>";
               console.log(ul.innerHTML.trim());
            </script>
         </body>
      </html>

   **Console Output**

   ::

      <li>Banana</li>
      <li>Lemon</li>
