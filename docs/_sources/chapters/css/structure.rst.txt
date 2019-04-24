CSS Structure
=============

Writing CSS
-----------

.. index:: ! rule

Programmers can change a lot of different styling using CSS **rules**.
A rule includes the selector and a declaration block.
Inside the declaration block, programmers set CSS properties to specific values.
CSS has a lot of different properties and it would be impossible to memorize them all.

CSS has two main components: the selector and the declaration block.
Inside the declaration block, programmers set the style rules.

.. sourcecode:: css

   selector {
       declaration block
   }

CSS has three different selectors that the programmer can use to make their style choices.
The first one that most beginners start with is the element selector.
Element refers to the HTML elements, so if the selector used is ``p``, then the styling will apply to all paragraph elements.
The ID selector is a specific id given to one element for CSS styling, for example when one paragraph on the web page needs to be bright pink.
The final selector is the class selector. A class is a group of HTML elements that need the same styling.

The declaration block is a series of initializations of style rules.

Linking CSS to HTML
-------------------

To get started with CSS, programmers need to link CSS to HTML.

There are three different places to add CSS in an HTML file:

1. External: The CSS is in a separate file linked to the HTML document in the ``<head>``. External linking of CSS is great for when programmers have large quantities of CSS that apply to the whole page.

   .. sourcecode:: html
   
      <head>
         <title>My Web Page</title>
         <link rel="stylesheet" type="text/css" href="styles.css">
      </head>

   ``link`` is an HTML tag that tells the browser to connect what is inside the linked file to the web page content.
   ``rel``, ``type``, ``href`` are all HTML attributes that are required to properly link CSS and let the browser know that CSS is what is in the file and where the file is.
   ``rel`` should be set to "stylesheet" and ``type`` will be set to "text/css" for all stylesheets.
   ``href`` is where the programmer enters the path to the stylesheet that should be used for the page.

2. Document or internal: All CSS styling is inside the HTML file, but within the ``<head>``. Internal use of CSS is great for when the programmer has a small amount of CSS that applies to the whole document.

   .. sourcecode:: html

      <head>
         <title>My Web Page</title>
         <styles>
            selector {
                declaration block
            }
         </styles>
      </head>

3. Inline: Programmers add CSS styling to individual tags. Good place to add some specific styling that applies to that one instance of the tag.

   .. sourcecode:: html
    
      <tag style="declaration block">content</tag>

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