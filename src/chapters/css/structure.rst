CSS Structure
=============

Writing CSS
-----------

.. index:: ! rule, ! selector

Programmers can change a lot of different styling using CSS **rules**.
A rule includes the selector and a declaration block.
A **selector** determines which elements will be affected by the rule.
Inside the declaration block, programmers set CSS properties to specific values.
CSS has a lot of different properties and it would be impossible to memorize them all.

::

   selector {
       declaration block
   }

CSS Selectors
^^^^^^^^^^^^^

CSS has three different selectors that the programmer can use to make their style choices.

The first one that most beginners start with is the **element selector**.
Element refers to the HTML elements, so if the selector used is ``p``, then the styling will apply to all paragraph elements.

The **id selector** is a specific id given to one element for CSS styling, for example when one paragraph on the web page needs to be bright pink.

The final selector is the **class selector**. A class is a group of HTML elements that need the same styling. The class name is determined by the programmer.
The class name should be unique and have meaning like variable names.

Declaration Blocks
^^^^^^^^^^^^^^^^^^

The declaration block is a series of initializations of style rules in CSS for a selector.
Programmers can write CSS two different ways depending on where the CSS is in relation to the HTML document.
We will go more in depth about the differences between CSS locations in the next section.

Here is an example of how to write the declaration block for internal and external CSS:

.. sourcecode:: css
   :linenos:

   selector {
       property: value;
       property: value;
       property: value;
   }

For inline CSS, the declaration block is inside one line of HTML like so:

.. sourcecode:: html

   <tag style="property:value;property:value;property:value;">content</tag>


Every property in CSS has a default value. For example, ``color``, which governs text color, defaults to "black".
For that reason, programmers only need to declare the CSS properties they want to change from the default.

.. note::

   HTML elements also have a default appearance. When creating web pages, we should be aware of which elements are inline elements and which elements are block elements. Inline elements will not start a new line (such as ``<b>``, ``<em>``, and ``<span>``) and block display elements do (such as ``<h1>``, ``<div>``, and ``<p>``).

CSS Examples
^^^^^^^^^^^^

Here are three different examples of how we can use selectors to make the text in a paragraph pink.

**Element Selector**

Using the element selector to change the color of all ``<p>`` elements,

.. sourcecode:: css
   :linenos:

   p {
      color: pink;
   }

Using the element selector will make all paragraph elements on the page have pink text.

**Class Selector**

We can give a few of the paragraphs on the page the class ``pink-paragraph`` on the HTML document, like so: ``<p class="pink-paragraph">content</p>``.
If we want to then style the ``pink-paragraph`` elements, we need to use the class selector in CSS.
Here is how our CSS might look:

.. sourcecode:: css
   :linenos:

   .pink-paragraph {
      color: pink;
   }

In CSS, the class selector is preceded by ``.``.

**Id Selector**

If one paragraph is going to have pink text, the id selector on the HTML document would look like: ``<p id="pinkParagraph">content</p>``.
In CSS, we would use the id selector to make the paragraph pink:

.. sourcecode:: css
   :linenos:

   #pinkParagraph {
      color: pink;
   }

In CSS, the id selector is preceded by ``#``.

Linking CSS to HTML
-------------------

To get started with CSS, programmers need to add CSS to HTML.

There are three different places to add CSS in an HTML file as indicated below:

1. External: The CSS is in a separate file linked to the HTML document in the ``<head>``. External linking of CSS is great for when programmers have large quantities of CSS that apply to the whole page.

   .. sourcecode:: html
      :linenos:

      <head>
         <title>My Web Page</title>
         <link rel="stylesheet" type="text/css" href="styles.css">
      </head>

   ``link`` is an HTML tag that tells the browser to connect what is inside the linked file to the web page content.
   ``rel``, ``type``, ``href`` are all HTML attributes that are required to properly link CSS and let the browser know that CSS is what is in the file and where the file is.
   ``rel`` should be set to "stylesheet", because it designates how the link relates to the page. ``type`` will be set to "text/css" for all stylesheets.
   ``href`` is where the programmer enters the path to the stylesheet that should be used for the page.

2. Document or internal: All CSS styling is inside the HTML file, but within the ``<head>``. Internal use of CSS is great for when the programmer has a small amount of CSS that applies to the whole document.

   ::

      <head>
         <title>My Web Page</title>
         <style>
            selector {
                declaration block
            }
         </style>
      </head>

3. Inline: Programmers add CSS styling to individual tags. This is a good place to add some specific styling.
   There is no selector in inline CSS; instead, the ``style`` attribute is used. This is because the styling only applies to that one instance of the HTML tag.

   .. sourcecode:: html

      <tag style="declaration block">content</tag>

Order of Precedence
^^^^^^^^^^^^^^^^^^^

Because there is an order of precedence to the location of CSS, it is important to be able to add or change CSS in all three locations.
Programmers use this to their advantage if they want to be very specific with overwriting some CSS for one element.
Inline CSS is highest in precedence with internal CSS being next and then external CSS is lowest.

Check Your Understanding
------------------------

.. admonition:: Question

   What is the order of precedence in CSS?

   #. Internal > External > Inline
   #. Inline > Internal > External
   #. Inline > External > Internal
   #. External > Internal > Inline
