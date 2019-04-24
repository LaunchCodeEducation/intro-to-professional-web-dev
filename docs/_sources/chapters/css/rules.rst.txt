CSS Rules
=========

How to Write a Style Rules
--------------------------

CSS style rules cover an infinite amount of amount of possibilities.
Programmers initialize individual CSS properties within the declaration block.
Every property in CSS has a default value. For example, ``font-color`` defaults to "black".
Programmers only have to change what needs to be.
Below are some examples of common CSS properties and what they do.
It is by no means an exhaustive list of CSS properties, but it is a good place to start.

Here is an example of how to write the declaration block for internal and external CSS:

.. sourcecode:: css

   selector {
       property: value;
       property: value;
       property: value;
   }

For inline CSS, the declaration block is inside one line of HTML like so:

.. sourcecode:: html

   <tag style="property:value;property:value;property:value;">content</tag>


.. admonition:: Note

   HTML elements also default to how it displays on the page.
   Inline elements will not start a new line and block display elements do.

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

Check Your Understanding
------------------------

.. admonition:: Question

   Find a CSS property and give its name, definition, and default value. Please do NOT use one of the ones above.