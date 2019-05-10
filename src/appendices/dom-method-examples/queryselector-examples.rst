.. _dom-querySelector-examples:

**querySelector** Examples
===========================

The general syntax for this method is:

.. sourcecode:: js

   let element = document.querySelector("CSS selector");

Searches the HTML document using a CSS selector pattern and CSS selector rules. Return the *first* matching element.
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
