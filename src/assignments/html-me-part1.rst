.. _html-me-part1:

HTML Me Something, Part 1
=========================

In Part 1, you will get comfortable with writing markup, and with separating
*content* from *design and layout*.

Getting Started
----------------

Stub out ``index.html`` with these basic elements:

.. sourcecode:: html
   :linenos:

   <!DOCTYPE html>

   <html>
      <head>
         <title></title>
      </head>

      <body></body>
   </html>

Fill each element with some appropriate content. You can start by removing the
snippet ``<p>YOUR NAME</p>`` that you used during setup.

Getting to Work
-----------------

Your mission is to build a page that:

#. Tells a story. This can be personal or impersonal, funny, serious or
   neither. You can do whatever you like, but it should be something in the
   range of 3-10 paragraphs or sections. `Here is an example
   <http://education.launchcode.org/html-me-something/submissions/chrisbay/index-nocss.html>`__,
   and here are some other ideas:

   a. Create a résumé page that tells the story of your professional
      journey to-date, and where you want to go as a coder.
   b. Describe a trip you took.
   c. Talk about one of your hobbies or passions.

#. Does each of the following:

   a. Uses each of the following structural HTML5 tags: ``<p>``,
      ``<header>``, ``<footer>``, ``<main>``, ``<article>``. If you need
      to review any of these tags, check out the `HTML tag reference
      <http://www.w3schools.com/tags/default.asp>`__ at w3schools.

   b. Uses at least one ``<img>`` tag (hopefully more). When placing
      images in your page, put them in a new subfolder called ``images``
      within your ``html-me-something`` directory.

   c. Uses at least one `HTML entity
      <http://www.w3schools.com/html/html_entities.asp>`__. Hint: putting a
      copyright notice in your footer will afford you the opportunity to use
      ``&copy;``, but you should also try to get creative here.

   d. Demonstrates creativity. Don’t stop with these items or tags. Have some
      ideas for your page, and make it great. And dig into the
      `w3schools HTML reference <http://www.w3schools.com/tags/default.asp>`__
      to learn more about other tags, their usage and attributes!

Notes and Tips
^^^^^^^^^^^^^^^

#. Use your browser developer tools to look at `the example
   page <http://education.launchcode.org/html-me-something/submissions/chrisbay/index-nocss.html>`__,
   or to troubleshoot things that don’t look right. You can mimic the
   document structure of this example, but do NOT just copy/paste!
#. Use the example to learn how your HTML elements might be structured,
   and build your page to fit your own content.
#. Don’t add any CSS yet. Really, we mean it! If you think your page
   looks boring now, that’s okay. We’ll get there soon enough.
#. As you make changes, you will obviously want to see the results. To
   do so, re-save the file in your text editor, then click Refresh in the
   browser window (or use cmd+R on a Mac, ctrl+R on Windows).
#. Rely on the reference sites linked on this page, or find others online. We
   haven’t taught you every detail about every tag that you may want or need.
#. You’re free to use tags that haven’t been explicitly introduced in class.
   We’ve given you enough background to get started, and are intentionally
   leaving some of the learning up to you.

Add and Commit Your Changes on Git
----------------------------------

Once you finish your page, use Git to ``add`` and ``commit`` your
``index.html`` changes.

*Why commit again?*

The reason is that you added a bunch of new HTML code to your ``index.html``
file. It is now in a very different state compared to the first time you
committed it. See this for yourself by checking the status:

::

   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

       modified:   index.html

   no changes added to commit (use "git add" and/or "git commit -a")

Git tells us:

   I see that you have modified ``index.html``. Use ``git add`` if
   you want these changes to be included in your next commit.

The Git workflow more or less comes down to this:

#. Create some initial stuff
#. ``init``
#. ``add`` and ``commit``
#. make some changes
#. ``add`` and ``commit``
#. make some more changes
#. ``add`` and ``commit``
#. etc...

The general rule is that *whenever you make any changes, you must add and
commit those changes to Git.*

So let’s do that. From within your root ``html-me-something/`` directory:

::

   $ git add index.html
   $ git commit -m "Finished work on HTML page"

You might be wondering: *How do I know when it’s time to pause working
and do another commit?*

This is somewhat subjective, and is ultimately up to you. The good habit is to
pause and commit any time you reach a natural stopping point or complete a
coherent chunk of work.

Done!
------

Well done! Time to `dive into some CSS <html-me-part2.html>`__.
