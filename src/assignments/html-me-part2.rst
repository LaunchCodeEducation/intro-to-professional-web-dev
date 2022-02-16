.. _html-me-part2:

HTML Me Something, Part 2
=========================

In Part 2, you’ll get comfortable with using CSS selectors and rules to dictate
display, while keeping your styles separate from your content.

Getting Started
----------------

#. Open a file named ``styles.css`` in your ``html-me-something/``
   directory.

Getting to Work
----------------

Go ahead and start adding styles in your ``styles.css`` file!

Requirements
^^^^^^^^^^^^^

Your CSS must:

#. Use `margin <http://www.w3schools.com/css/css_margin.asp>`__ and
   `padding <http://www.w3schools.com/css/css_padding.asp>`__ to space your
   elements in a visually pleasing manner.
#. Use at least one of each of the following types of selectors:

   a. `element <http://www.w3schools.com/cssref/sel_element.asp>`__,
   b. `class <http://www.w3schools.com/cssref/sel_class.asp>`__,
   c. `id <http://www.w3schools.com/cssref/sel_id.asp>`__.

#. Follow these rules:

   a. Use the element selector to give the ``<body>`` element a margin value of 8px and a display type of block.
   b. Give a heading on your page the id of ``mainHeading`` and use the id selector in ``styles.css`` to give it a color value of red.
   c. Give a paragraph on your page the id of ``testP`` and a class name of ``funParagraph``. Use the class selector in ``styles.css`` to give it a color value of green.

Notes
^^^^^^

#. In order to see any visible change, make sure to link the stylesheet
   to your main document.
#. Feel free to check out our `styled example
   <http://education.launchcode.org/html-me-something/submissions/chrisbay/index.html>`__
   to see how we did things. Use “View Source” (by right-clicking anywhere on
   the page and selecting *View Source*).
#. Another thing you might find useful is your browser’s `developer tools
   <https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools>`__.
#. And be sure to use the *Resources* section below as you go.

Resources
----------

General CSS Examples and References:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `w3schools CSS Reference <http://www.w3schools.com/css/default.asp>`__ Great site for syntax examples
#. `CSS Zen Garden <http://www.csszengarden.com>`__ This site provides multiple examples of what you can do with CSS in a browser.
#. (Advanced) `Specifics on CSS Specificity
   <https://css-tricks.com/specifics-on-css-specificity/>`__
#. (Advanced) `Specificity (MDN)
   <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`__
#. (Advanced)  `CSS Design Awards <https://www.cssdesignawards.com/>`__  Showcase for CSS designers to share their work. 

.. _normalization:

CSS Normalization:
^^^^^^^^^^^^^^^^^^^

#. `Eric Meyer’s reset.css <http://meyerweb.com/eric/tools/css/reset/>`__
#. `normalize.css <http://necolas.github.io/normalize.css/>`__

Add and Commit Your Changes on Git
-----------------------------------

When you finish making your page look spiffy, take a moment to commit your
changes on Git:

::

   $ git add styles.css
   $ git commit -m "Added some killer CSS styling"

If you also made tweaks to your ``index.html`` file, then you need to commit
those changes as well (along with a descriptive commit message):

::

   $ git add index.html
   $ git commit -m "Changed title from 'My Favorite Puppies' to 'The Objectively Best Puppies'"

Incidentally, this is a good opportunity to address the question: *Why does Git
have two separate commands for ``add`` and ``commit`` if I always do them
together anyway?*

The answer comes back to the notion of collecting your changes in a “coherent
chunk of work” for each commit. The ``add`` command gives you the opportunity
to specify exactly *which* file(s) should be included in the upcoming commit.
In the example above, this allowed us to perform two separate commits---each
with its own message describing its own chunk of work.

Note that you certainly can ``add`` multiple files to the same commit. For
example, suppose you made changes to both ``index.html`` and ``styles.css``,
but those changes are all part of the same unit of work. In that case you would
add them both before committing:

::

   $ git add index.html
   $ git add styles.css
   $ git commit -m "Added puppy image with thick yellow border"

There is a convenient shortcut, ``git add .``, for those (frequent) occasions
when you want to include *every* changed file without having to type each one
individually. The following example is equivalent to the previous one (assuming
you only changed ``index.html`` and ``styles.css``):

::

   $ git add .
   $ git commit -m "Added puppy image with thick yellow border"

It is usually a good idea to check first (using ``git status``) before
running ``git add .``, so that you don’t mistakenly include unwanted
changes.

Go ahead and push your work to your remote repository using ``git push`` and head over to Github to see how you did.

Done!
------

If you have a green check mark, you are ready to submit! Go back to the
:ref:`Assignment Page <submitting-your-work>` and follow the submission
instructions there.
