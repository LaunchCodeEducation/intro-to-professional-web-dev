Remote Repositories
===================

Local, Remote, GitHub, Oh My!
-----------------------------

So far, the book has covered how to setup a Git repository on the local machine.
But, one of the benefits of using a VCS was storage of backups.
So, what happens to the code base if something happens to the machine?
That is where remote repositories come in.
Instead of keeping a Git repository only on a local machine, the code base is in a **remote repository** and the programmers working on it keep copies on their local machine. 

To get started with remote repositories, create an account on `GitHub <https://www.github.com/>`_.
From there, programmers can create a remote repository, view commit history, and report issues with the code.
 

Collaborating with Colleagues
-----------------------------

What if a programmer wants to start collaborating with their colleagues on a new project?
They might need to start with the work that one of their colleagues has already done.
In this particular case, the programmer has to import the work that is being stored in an online repository onto their local machine.

They can clone a remote repository by using the ``git clone <url>`` command.
Github and other online Git systems give users the option to clone the repository through HTTPS or SSH depending on how their Github profile is set up.
The ``<url>`` of the command is where the programmer adds the url to the repository that they are cloning. 

.. note::

   Throughout this book, HTTPS will be used for cloning repositories.

Contributing to a Remote Repository
-----------------------------------

Now that the programmer has a profile on Github and a local copy of a remote repository, they start coding!

Once they create a new feature, it is time to make a commit.
When working with a remote, the commit process has five steps:

1. ``git status``
2. ``git add``
3. ``git commit``
4. ``git push origin master``
5. ``git log``

The fourth step uses the new command ``git push`` where the commit is pushed to the remote from the local.
``origin`` indicates that the commit does indeed go to the remote and ``master`` is the name of the branch that the commit goes to. 

Check Your Understanding
------------------------------

.. admonition:: Question

   What is the new command for making a commit to a remote repository?
