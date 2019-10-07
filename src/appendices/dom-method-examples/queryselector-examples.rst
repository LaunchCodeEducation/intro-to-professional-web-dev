``querySelector`` and ``querySelectorAll`` Examples
===================================================

.. _dom-querySelector-examples:

``querySelector``
-----------------

The general syntax for this method is:

.. sourcecode:: js

   let element = document.querySelector("CSS selector");

Uses a CSS selector pattern and CSS selector rules to find a matching element. Returns the FIRST matching element.
If NO match is found, ``null`` is returned.

CSS Selector Examples

* class selector: ``document.querySelector(".class-name");``
* tag selector: ``document.querySelector("div");``
* id selector: ``document.querySelector("#main");``

.. tip::

   You can use any valid CSS selector with ``querySelector``. The selectors can be simple like
   ``querySelector("div")`` or complex like ``querySelector("#main div .summary")``.

.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
            <style>
                  .main {
                     font-weight: bold;
                  }
            </style>
         </head>
         <body>
            <h1>querySelector Example</h1>
            <p id="description" class="main">
                  querySelector's power is exceeded only by it's mystery.
            </p>
            <div id="response">
                  It's not that mysterious, querySelector selects elements
                  using the same rules as CSS selectors.
            </div>
            <script>
                  // selects the <p> using class selector
                  let main = document.querySelector(".main");
                  console.log(main.innerHTML.trim());
                  main.style.color = "blue";

                  // Selects the <div> using tag selector
                  let response = document.querySelector("div");
                  console.log(response.innerHTML.trim());
                  response.style.color = "red";
            </script>
         </body>
      </html>

   **Console Output**

   ::

      querySelector's power is exceeded only by it's mystery.
      It's not that mysterious, querySelector selects elements
      using the same rules as CSS selectors.

.. _dom-querySelectorAll-examples:

``querySelectorAll``
--------------------

The general syntax for this method is:

.. sourcecode:: js

   let elements = document.querySelectorAll("CSS selector");

Uses a CSS selector pattern and CSS selector rules to find a matching elements. Returns
ALL elements that match the selector. If NO match is found, ``null`` is returned.

.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
            <style>
                  .red {
                     color: red;
                  }
                  .purple {
                     color: purple;
                  }
            </style>
         </head>
         <body>
            <h1>querySelectorAll Example</h1>

            <h2>Red Fruits</h2>
            <ul class="red">
               <li>Strawberry</li>
               <li>Raspberry</li>
               <li>Cherry</li>
            </ul>

            <h2>Purple Fruits</h2>
            <ul class="purple">
               <li>Blackberry</li>
               <li>Plums</li>
               <li>Grapes</li>
            </ul>

            <script>
                  // Selects ALL the <li> elements and adds text to each one
                  let listItems = document.querySelectorAll("li");
                  for (let i=0; i < listItems.length; i++) {
                     listItems[i].innerHTML += " is yummy"
                  }

                  // Selects the PURPLE <li> elements and make them bold
                  let purpleItems = document.querySelectorAll(".purple li");
                  for (let i=0; i < purpleItems.length; i++) {
                     purpleItems[i].innerHTML += "!!!"
               }

               // Console log the contents of the first items in each list
               // Remember that querySelector returns only the FIRST match
               let firstRed = document.querySelector(".red li");
               console.log("contents of first red li:", firstRed.innerHTML);
               let firstPurple = document.querySelector(".purple li");
               console.log("contents of first purple li:", firstPurple.innerHTML);
            </script>
         </body>
         </html>

   **Console Output**

   ::

      contents of first red li: Strawberry is yummy 
      contents of first purple li: Blackberry is yummy!!!
