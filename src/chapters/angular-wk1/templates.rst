Templates
==========
Take a look at the homepage for `LaunchCode <https://www.launchcode.org/>`__.
The content includes text, images, a navigation bar, buttons, embedded videos,
static and scrolling sponsor logos, and links. All of this content is carefully
arranged.

Your Own Website
-----------------

Imagine building your own website with a smaller set of features. You could
include favorite movies or sports teams, cities where you have lived, schools
attended, hobbies, etc. Using your :ref:`HTML <html-index>` and
:ref:`CSS <css-index>` knowledge, you could construct an appealing layout using
carefully selected and arranged tags (``<div>, <button>, <img>``, etc.).

Now imagine you have to change one or more items on the page. Maybe you move
and your school or team loyalty shifts. Updating the city, school logo, etc.
means adjusting those items in the HTML, and if that information appears in
other areas of your website, then you need to update that code as well. Also,
you need to consider any formatting changes that result from adding or removing
content.

Whew! Updating your website rapidly gets tedious, especially if it contains
lots of information or consists of multiple pages. If only there was a way to
automatically update the content and layout for your site...

Templates are Frameworks
-------------------------

.. index:: ! template

A **template** provides a general structure for a web page. It identifies where
different elements get placed on the page, but it does NOT fill them with
content. Think of a template like a skeleton, a blueprint, or an outline for
what we want the page to look like.

.. admonition:: Example

   TODO: Compare...

   Show HTML code for simple layout - heading, main div, sub divs for ul and links.
   Show template for same layout. "Blanks" can be updated and filled by changing the arguments sent into the framework.

Each section in the template contains one or more "blanks" where specific items
need to be added. Separate JavaScript code sends data to the template to fill
in these blanks, and this data can change based on a user's actions.

If you used a template to build your website, then changing the list of movies,
schools, cities, or hobbies just involves altering something as simple as an
array or object. After you change the data, the template does the tedious work
of updating the HTML. For example, if your site lists your hobbies in three
separate places, then all three will update automatically after you add
"Shark Rodeo" to your ``hobbies`` array. You do not need to worry about
re-doing any of the tags.

   Question: Replace "Shark Rodeo" and ``hobbies`` with "Hidden Figures" and
   ``favoriteMovies``?
