.. _git-stash:

Git Stash
=========

.. index::
   single: Git; stash

When working with branches in Git, you will sometimes make some changes
to your code only to realize you are not working in the branch
you thought you were. Thankfully, this is easy to remedy as long as you
haven't committed the changes. 

This tutorial introduces the ``stash``
command of ``git``, which allows you to easily move the changes from one branch to another

The Situation
-------------

We address the following situation: 

- You have multiple branches in your local repository. For this tutorial, we'll work with ``master`` and ``feature`` branches. 
- You are working in a given branch, and have saved some changes. 
- Your changes have NOT been staged or committed.
- You want to move your changes to another branch.

If this situation describes you, you're in luck! Let's fix it.

Using Git Stash
---------------

Suppose you have a branch called ``feature`` that you want to work in.
You've made some changes, and saved them, only to realize that you're in
(Gasp!) the ``master`` branch.

::

   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

       modified:   main.js

   no changes added to commit (use "git add" and/or "git commit -a")

At this point, you could try to ``git checkout feature``, but you would
encounter this error:

::

   $ git checkout feature
   error: Your local changes to the following files would be overwritten by checkout:
       main.js
   Please commit your changes or stash them before you switch branches.
   Aborting

This error results from the situation in which your ``feature`` branch
has commits that your ``master`` branch doesn't, so Git can't move the
un-staged changes you made in ``master`` cleanly over to ``feature``.

Take a deep breath. This is an easy one to remedy.

Use ``git stash`` to put these changes off to the side for a moment.

::

   $ git stash
   Saved working directory and index state WIP on master: 1da4892 Introduce render_template
   HEAD is now at 1da4892 Introduce render_template

Your message will differ, based on the most recent commit that you made
in the given branch.

Note that your ``master`` branch is now “clean”.

::

   $ git status
   On branch master
   nothing to commit, working tree clean

Now, safely switch to the ``feature`` branch.

::

   $ git checkout feature
   Switched to branch 'feature'

And then pick up the changes that you stashed, and put them in the
``feature`` branch using ``git stash pop``.

::

   $ git stash pop
   Auto-merging main.js
   On branch feature
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

       modified:   main.js

   no changes added to commit (use "git add" and/or "git commit -a")
   Dropped refs/stash@{0} (cb556d3734ed8675b6b81f5d4e37d003bd1bc6b9)

That's it! Carry on coding.

References
----------

-  `Git Stash Tutorial <https://www.atlassian.com/git/tutorials/git-stash>`__
