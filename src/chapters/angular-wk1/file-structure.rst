Angular File Structure
=======================

Each Angular project contains a standard file structure, which is shown in the
figure below.

.. figure:: ./figures/AngularFileStructure.png
   :alt: Visual of the standard Angular file structure.

All of the project files (and there will be LOTS) are stored in the single,
top-level folder, ``projectName``, which contains a ``src`` folder and a set of
support files.

.. admonition:: Note

   When you start a new Angular project, do not worry about the support files.
   These will be generated automatically, and they take care of the routine
   technical details for making your project run smoothly.

``src`` contains the ``app`` folder and four important files: index.html,
main.ts, style.css, and polyfills.ts. We will explore these files in more
detail later [TODO: Rephrase].

The ``app`` folder contains the files and subfolders needed to control the
nitty-gritty details of displaying a webpage. For your projects, most of your
time and effort will be spent modifying the contents within ``app``.

StackBlitz
-----------

Your first Angular project will be another "Hello, World" example, and we will
use a different online tool to build this. The site is called
`StackBlitz <https://stackblitz.com>`__, and it is similar to Repl.it in that
it allows us to play without risk. The main difference is that StackBlitz is
specifically designed to create webpage templates.

.. admonition:: Note

   For the "HTML Me Something" studio, you created an account on
   `GitHub <https://github.com>`__ . Since you will modify your Angular project
   over the next few lessons, you need access to GitHub to store your progress.

   Follow the link and make sure you remember your login information, or enroll
   if you have not yet created an account.

StackBlitz Workspace Layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before we dive into the project, we need to become familiar with the StackBlitz
layout. The workspace consists of 3 main panels and several menu functions.

Features to note:

#. Use your GitHub account to store your projects. Click the GitHub button (1)
   to save your progress.
#. If you have a link and are viewing someone else's project, you can *fork*
   the content (2). This stores a copy of the project in your account, allowing
   you to edit the files without changing the originals. This lets you use
   other programmers' work (with permission) to enhance your own.

.. figure:: ./figures/StackBlitzWorkspace.png
   :alt: StackBlitz workspace layout.

3. File panel and menu (3). Allows you to search for an item, add extensions,
   update settings, and add, open, or delete files.
#. Editor panel (4). Your code goes here. Click on a filename to open it in a
   tab in the editor.
#. Preview panel (5). Provides a view of what the webpage looks like. This
   panel can be minimized to save space or opened into a new browser window
   (6).

As with any new coding skill or tool, the best way to learn is to actively
practice. Let's begin building your first Angular project.
