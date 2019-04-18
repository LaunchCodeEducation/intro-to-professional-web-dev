CSS Structure
=============

In order to get the styles to work together with the content and make a beautiful web page, it is critical to properly link the CSS to the HTML.

There are three different places to add CSS:

1. External: CSS is kept in a separate file that is linked to the HTML document in the ``<head>``. When the programmer has large quantities of CSS.
2. Document or internal: All CSS styling is kept together in the HTML file, but within the ``<head>``. When the programmer has a small amount of CSS that applies to the whole document.
3. Inline: CSS styling is added to individual tags. Good place to add some specific styling that applies to that one instance of the tag.

Though programmers find themselves preferring different ways to add CSS, it is important to be able to add or modify CSS in all three locations.

There is also an order of precedence, much like the order of operations, to the way that CSS is added. This can also be used to the programmer's advantage if they want to be very specific with overwriting some CSS for one element.

Inline CSS is highest in precedence with internal CSS being next and then external CSS is lowest. 

When writing CSS, there are three different selectors that the programmer can use to make their style choices. The first one that most beginners start with is the element selector. Element refers to the HTML elements, so if the selector used is ``p``, then the styling will apply to all paragraph elements. The ID selector is a specific id given to one element for CSS styling, which might be used if one paragraph on the web page needs to be bright pink.
The final selector is the class selector. Class is a group of HTML elements that need the same styling.