CSS Rules
=========

Below are some examples of common CSS properties and what they do.
It is by no means an exhaustive list of CSS properties, but it is a good place to start.

Good CSS Properties to Know
---------------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - CSS Property
     - Definition
     - Default Value
   * - ``font-size``
     - Changes the size of the font.
     - medium or 20px
   * - ``color``
     - Changes the text color.
     - black
   * - ``font-family``
     - Changes the font types.
     - Depends on the browser
   * - ``background-color``
     - Sets the color of the background of an element.
     - transparent
   * - ``text-align``
     - Aligns the text within an element.
     - left

CSS Example
-----------

Adding CSS to the HTML page about Space Plants is the logical next step in building a website about this cool discovery.
The astronauts building the site used the ``body``, ``h1``, and ``p`` selectors to change some of the styling of those elements.

.. sourcecode:: html
   :linenos:

   <!DOCTYPE html>
   <html>
      <head>
         <title>Plant-Loving Astronauts</title>
         <style>
            body {
              background-color: cornflowerblue;
            }
            h1 {
              color: green;
            }
            p {
              font-size: 18px;
            }
         </style>   
      </head>
      <body>
         <h1>Space Plants Are Cool</h1>
         <p>NASA discovers that plants can live in <b>outer space</b>. More innovations from this discovery to follow.</p>
         <img src = "space-flower.jpg" alt = "Flower floating in space.">
         <!-- This image was taken by NASA and is in the Public Domain -->
      </body>
    </html>

.. figure:: figures/plant-loving-astronauts-css.png
   :alt: Made the background color blue, the heading green, and the paragraph text 18 pt. font of the website in the previous chapter about space plants.

Check Your Understanding
------------------------

.. admonition:: Question

   Find a CSS property and give its name, definition, and default value. Please do NOT use one of the ones above.
