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
:ref:`CSS <css-index>` knowledge, you could construct an appealing layout with
carefully selected and arranged tags (``<div>, <button>, <img>``, etc.).

Now imagine you have to change one or more items on the page. Maybe you move
and your school or team loyalty shifts. Updating the city, school logo, etc.
means adjusting those items in the HTML, and if that information appears in
other areas of your website, then you need to modify that code as well. Also,
you need to consider any formatting changes that result from adding or removing
content.

Whew! Refreshing your website rapidly gets tedious, especially if it contains
lots of information or consists of multiple pages. If only there was a way to
automatically update the content and quickly rearrange the layout for your
site...

Templates are Frameworks
-------------------------

.. index:: ! template

A **template** provides the general structure for a web page. It identifies
where different elements get placed on the page, but it does NOT fill them with
content. Think of a template as an outline for what we want the page to look
like. No details yet, just defined spaces where information needs to be added.

Let's see how using a template makes our lives easier.

No Template
^^^^^^^^^^^^

The code below builds a simple 3-column webpage. It defines the location for
each heading, unordered list, and button. The CSS file (not shown) specifies
the font, text size, colors, etc.

.. replit:: html
   :slug: NoTemplateExample
   :linenos:

   <body>
      <h1>Hello, Screen!</h1>
      <div class="row list">
         <div class='movie'>
            <h4>Movies</h4>
            <ul>
               <li>Hidden Figures</li>
               <li>The Princess Bride</li>
               <li>Ferris Bueller's Day Off</li>
            </ul>
            <button class='movie'>More</button>
         </div>
         <div class='school'>
            <h4>Education</h4>
            <ul>
               <li>LaunchCode</li>
               <li>Monsters University</li>
               <li>My HS</li>
            </ul>
            <button class='school'>More</button>
         </div>
         <div class='hobby'>
            <h4>Hobbies</h4>
            <ul>
               <li>Knitting</li>
               <li>Cycling</li>
               <li>Shark Rodeo</li>
            </ul>
            <button class='hobby'>More</button>
         </div>
      </div>
      <hr>
      <div class="links">
         <h2>Links</h2>
         <a href="https://www.launchcode.org/" target="_blank">LaunchCode</a> <br>
         <a href="https://www.webelements.com/" target="_blank">WebElements</a>
      </div>
   </body>

We could drastically improve the appearance and content of the page by playing
around with the tags, classes, styles and text. However, any change we want to
make needs to be coded directly into the HTML and CSS files.

This quickly becomes inefficient, especially if changing the items involves
multiple blocks of code.

A Better Way
^^^^^^^^^^^^^

Each section in a template contains one or more *blanks* where specific items
need to be added. Separate JavaScript code sends data to the template to fill
in these blanks, and this data can change based on a user's actions.

.. sourcecode:: html
   :linenos:

   <body>
      <h1>{{mainHeading}}</h1>
      <div class="row list">
         <div class='movie'>
            <h4>Movies</h4>
            <ul>{{movieTitles}}</ul>
            <button class='movie'>More</button>
         </div>
         <div class='school'>
            <h4>Education</h4>
            <ul>{{schoolNames}}</ul>
            <button class='school'>More</button>
         </div>
         <div class='hobby'>
            <h4>Hobbies</h4>
            <ul>{{hobbies}}</ul>
            <button class='hobby'>More</button>
         </div>
      </div>
      <hr>
      <div class="links">{{headingAndLinkList}}</div>
   </body>

This HTML looks similar to the previous example, but saves about 16 lines. It
provides the same ``<div></div>`` structure but replaces some of the specific
text between the tags with *placeholders*.

Each item listed inside ``{{}}`` refers to data that will be passed into the
template and automatically formatted. For example, the template converts
``{{movieTitles}}`` into a sequence of ``<li></li>`` tags.

By defining our template in an even more general manner, we could replace the
``h4``, ``ul`` and ``button`` structure with a single placeholder.

.. sourcecode:: html
   :linenos:

   <body>
      <h1>{{mainHeading}}</h1>
      <div class="row list">
         <div class='movie'>{{movieContent}}</div>
         <div class='school'>{{schoolContent}}</div>
         <div class='hobby'>{{hobbyContent}}</div>
      </div>
      <hr>
      <div class="links">{{linkContent}}</div>
   </body>

By using a template to build the website, changing the list of movies, schools,
or hobbies involves altering something as simple as an array or object. After
changing that data, the template does the tedious work of modifying the HTML.
The list of movies would update automatically if we add "Up" to our
``favoriteMovies`` array, which then gets passed into ``{{movieContent}}``. We
do not need to worry about re-coding any of the tags.

Templates Support Dynamic Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we add a search box to our website, a user could enter *NASA images*,
*giraffe gif*, *move trailers*, or something else. We cannot know ahead of time
what a user will request, but we want our website to be able to display any
relevant results.

Besides making it easier to organize and display content, templates also allow
us to create a *dynamic* page. This means that its appearance changes to fit
new information. For example, we can define a grid for displaying photos in
rows of 4 across the page. Whether the images are of giraffes, tractors, or
balloons does not matter. The template sets the layout, and the code feeds in
the data. If more photos are found, extra rows are produced on the page, but
each row shows 4 images.

Templates must be used anytime we create a webpage that responds to a changing
set of data, especially if that data is unknown to us.

Templates Provide Structure, Not Content
-----------------------------------------

Templates allow us to decide where we want to display data on our webpage, even
if we do not know beforehand what that data will be. Information pulled from
forms, APIs, or user input will be formatted to fit within our design.

.. figure:: ./figures/AngularTemplateDiagram.png
   :scale: 90%
   :alt: Visual of a template structure.

In the figure, the black outlines represent different structures defined by the
template. Each structure governs a specific portion of the screen. As data gets
fed into the template, the appearance of the page changes.

If no data is sent to a particular structure, that part of the screen remains
empty because the space is still reserved. Other components of the page will
work around that space.

Check Your Understanding
-------------------------

.. admonition:: Question

   Why should we use a template to design a webpage rather than just coding
   the entire site with HTML and CSS?

.. admonition:: Question

   PREDICT: Do you think that changing the CSS for the *template* affects all
   of the smaller parts within that template?

   #. Yes
   #. No

.. admonition:: Question

   PREDICT: Do you think that changing the CSS for one *component* in a
   template affects all of the other parts within that template?

   #. Yes
   #. No
