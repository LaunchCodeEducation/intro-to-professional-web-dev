HTML Structure
==============

.. index:: ! head , ! title , ! html , ! doctype , ! body

Programmers should follow certain rules about how to structure an HTML file.
The rules about how to structure an HTML file and the tags used to lay out this structure are vital to the browser being able to render the page.

Structure Rules
---------------

When it comes to laying out the overarching structure of an HTML file, a programmer should follow 5 rules:

1. Every HTML file needs a ``DOCTYPE`` tag, specifying the HTML version used.
   When using the current version of HTML, the ``DOCTYPE`` tag is simple to remember as it is: ``<!DOCTYPE html>``.
   This is one of few tags that does not require a closing tag.
2. The ``<html>`` tag denotes the beginning and end of the HTML the programmer has written.
3. The ``<head>`` tag contains data about the web page.
4. The ``<body>`` tag contains everything that appears on the page of the document.
5. The ``<title>`` tag goes in the ``<head>`` of the document and browsers require it. It gives the title of the web page that appears in the tab.

Here is an example of the structure of an HTML page based off of these rules:

.. sourcecode:: html
   :linenos:

   <!DOCTYPE html>
   <html>
      <head>
         <title>My Web Page</title>
         content
      </head>
      <body>
         content
      </body>
   </html>


Document Head
-------------

So other than the title, what goes in the head of an HTML file?
The head includes links to other files and other data about the document.
Browsers do not display the content in the head.

.. note::

   The head can also include some styling to make the page beautiful.
   How to do that is covered in the next chapter on CSS.

Document Body
-------------

After the programmer has written the head of the document, it is time to move on to the body of the document.
The body of the document contains the content that appears on the web page.
Within the ``body`` tags, programmers add images, text, and even code samples with different HTML tags.
Content outside of the body will not appear on the page.

To make HTML more readable to other programmers, programmers write comments in HTML. When adding a comment, the programmer uses ``<!--`` to indicate the start and ``-->`` to end the comment, like so:

.. sourcecode:: html
   :linenos:

   <body>
      <!-- This is an important comment -->
   </body>

.. note::

   Spacing and tabs helps many programmers read through theirs and their colleagues' code.
   Be aware that doing so in HTML can affect how the browser renders the page in rare instances.

Check Your Understanding
------------------------

.. admonition:: Question

   Which HTML tag does not require a closing tag?

   #. ``title``
   #. ``body``
   #. ``head``
   #. ``DOCTYPE``
