CSS Structure
=============

Describe the 3 locations that style rules may be placed and when one location may be preferred over the others: external, document, inline

External: CSS is kept in a separate file that is linked to the HTML document in the ``<head>``. When the programmer has large quantities of CSS.
Document or internal: All CSS styling is kept together in the HTML file, but within the ``<head>``. When the programmer has a small amount of CSS that applies to the whole document.
Inline: CSS styling is added to individual tags. Good place to add some specific styling that applies to that one instance of the tag.


Use CSS rules at each of the 3 possible locations


Describe precedence between CSS rules based on location

Inline > Internal > External 

Describe the following simple selector types, and situations in which each is preferred: element, ID, class

Element refers to the HTML elements.
ID is a specific id given to one element for CSS styling.
Class is a group of HTML elements that need the same styling.