Remote Repositories
===================

Local, Remote, GitHub, Oh My!
-----------------------------

So far, the book has covered how to setup a Git repository on the local machine.
However, one of the benefits of using a VCS is to store backups.
If something bad happens to a coder's machine, they might lose all of the code
for their projects! This is where remote repositories come in.
Instead of keeping a Git repository only on a local machine, the code base is
also saved in a **remote repository**. Any team members working on the project
keep copies of the code on their local machine. 

To get started with remote repositories, create an account on `GitHub <https://www.github.com/>`__.
From there, programmers can create a remote repository, view commit history, and report issues with the code.

Collaborating with Colleagues
-----------------------------

What if a programmer wants to start collaborating with their colleagues on a new project?
They might need to start with the work that one of their colleagues has already done.
In this particular case, the programmer has to import the work from an online repository
onto their local machine.

They can clone a remote repository by using the ``git clone <url>`` command.
Github and other online Git systems give users the option to clone the repository through HTTPS or SSH depending on how their Github profile is set up.
The ``<url>`` of the command is where the programmer adds the url to the repository that they are cloning. 

.. admonition:: Note

   Throughout this book, SSH will be used for cloning repositories. We'll show
   you how to set this up soon.

Renaming the Default Branch
---------------------------

When we run ``git init`` to start a new repository, part of the process creates
a single, default branch. We can see its name by running the command
``git branch``.

.. sourcecode:: bash
   :linenos:

   $ git branch
   * main

For the examples in this book, we refer to the default branch as ``main``.
However, depending on the Git settings on your computer, you might see a
different one. This won't affect the performance of your project in any way.
That said, GitHub defaults to ``main`` for all new repositories. To keep our
work clear, we should match our local and remote branch names.

.. admonition:: Try It!

   If your installed version of Git names the default branch something other
   than ``main``, change it with the command:

   .. sourcecode:: bash

      $ git branch -m old-branch-name main

   In this case, ``old-branch-name`` becomes ``main``.

Contributing to a Remote Repository
-----------------------------------

Once a programmer has a profile on Github and a local copy of a remote
repository, they start coding!

After they create a new feature, it is time to make a commit. When working with
a remote repo, the commit process includes five steps:

#. ``git status``
#. ``git add``
#. ``git commit``
#. ``git push origin main``
#. ``git log``

The fourth step uses the new command ``git push``, where the commit is pushed
to the remote from the local. ``origin`` indicates that the commit does indeed
go to the remote, and ``main`` is the name of the branch that receives the
commit. 

Check Your Understanding
------------------------------

.. admonition:: Question

   What is the new command for making a commit to a remote repository?
