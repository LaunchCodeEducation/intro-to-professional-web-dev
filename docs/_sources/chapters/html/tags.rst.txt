HTML Tags
=========

Time to dive into learning about all the different tags for creating content!
This page contains a helpful table of tags to know for beginning programmers to bookmark.
This is by no means an exhaustive list of all HTML tags, but it is a good place to start.

Tags to Know
------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Tag Name
     - Code
     - Definition
   * - Bold
     - ``<b>``
     - When surrounding text, makes that text bold.
   * - Emphasis
     - ``<em>``
     - When surrounding text, makes that text italic.
   * - Hyperlink
     - ``<a>``
     - Creates hyperlinks.
   * - Image
     - ``<img>``
     - Denotes images.
   * - Break
     - ``<br>``
     - A single line break.
   * - Paragraph
     - ``<p>``
     - Creates a paragraph in text.
   * - Section
     - ``<span>``
     - Makes a section in text.
   * - Division
     - ``<div>``
     - Defines an area of the page.
   * - Form
     - ``<form>``
     - Creates a form for user input.
   * - Unordered List
     - ``<ul>``
     - Creates an unordered list.
   * - Ordered List
     - ``<ol>``
     - Creates an ordered list.
   * - List element
     - ``<li>``
     - Denotes an element of the list. This tag is used for both ordered and unordered lists.
   * - Table
     - ``<table>``
     - Creates a table on the page.
   * - Heading Level One
     - ``<h1>``
     - Creates a heading in the text. 

.. note::
   
   There are multiple headings in HTML going from ``h1`` to ``h6``.
   The headings get progressively smaller.
   A good rule of thumb is to have only one ``h1`` in a web page and do not skip a level.
   Headings can be resized so there is no need to do so.

Tag Example
-----------

Here is an example of a basic web page utilizing some of the tags above with the HTML used to make the site.

.. sourcecode:: html

   <!DOCTYPE html>
   <html>
      <head>
         <title>Plant-Loving Astronauts</title>
      </head>
      <body>
         <h1>Space Plants Are Cool</h1>
         <p>NASA discovers that plants can live in <b>outer space</b>. More innovations from this discovery to follow.</p>
         <!-- add images from NASA of these space plants -->
      </body>
    </html>

.. figure:: figures/plant-loving-astronauts.png
   :alt: A web page with the heading, Space Plants Are Cool, and the paragraph about NASA's discovery of space plants.

Attributes
----------

.. index:: ! attribute

Programmers can add extra information beyond element type to HTML tags.
Programmers add **attributes** to HTML tags for further specification about the element's appearance.
Examples of attributes include the alignment of the element or alternate text to an image.

Programmers add attributes before the closing bracket in the opening tag, like so:

.. sourcecode:: html
   
   <element attribute = "value">content</element>

Attributes Example
------------------

Here is an example of a basic web page utilizing some of the tags above and appropriate attributes with the HTML used to make the site.

.. sourcecode:: html

   <!DOCTYPE html>
   <html>
      <head>
         <title>Plant-Loving Astronauts</title>
      </head>
      <body>
         <h1>Space Plants Are Cool</h1>
         <p>NASA discovers that plants can live in <b>outer space</b>. More innovations from this discovery to follow.</p>
         <img src = "space-flower.jpg" alt = "Flower floating in space.">
      </body>
    </html>

.. figure:: figures/plant-loving-astronauts-2.png
   :alt: A web page with the heading, Space Plants Are Cool, and the paragraph about NASA's discovery of space plants with an accompanying picture of a flower floating in space.

The ``<img>`` tag has two attributes that you will see a lot. ``src`` gives the location of the image that is being used and ``alt`` gives alternate text for screen reader users. For that reason, ``alt`` should be a concise description of what is going on in the image.

Check Your Understanding
------------------------

.. admonition:: Question
 
   Which tag is used to make text italicized?

   #. ``b``
   #. ``i``
   #. ``em``
   #. ``br``
