.. _dom-style-object-examples:

**style property** Examples
===========================

The general syntax for the ``style`` property:

.. sourcecode:: js

   element.style.aStyleProperty

The ``style`` property is an object that allows you to *read* and *update* the
INLINE style properties of the element. The ``style`` property does NOT *read*
or *update* styles defined in a ``<style>``or an external CSS file linked with
a ``<link>``.


.. admonition:: Example

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
         <head>
            <title>DOM Examples</title>
         </head>
         <body>
            <h1>style property Example</h1>
            <div id="strawberry" style="color: red;">Strawberry</div>
            <div id="blackberry" style="color: purple; font-size: 5px">Blackberry</div>

            <script>
                  let strawberry = document.querySelector("#strawberry");
                  console.log(strawberry.style.color);
                  let blackberry = document.querySelector("#blackberry");
                  console.log(blackberry.style.fontSize);
                  // Update the font size of strawberry
                  strawberry.style.fontSize = "45px";
                  console.log(strawberry.style.fontSize);
            </script>
         </body>
      </html>

   **Console Output**

   ::

      red
      5px
      45px
