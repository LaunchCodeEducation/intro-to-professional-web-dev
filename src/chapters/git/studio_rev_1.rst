.. _comm-log-part1:

Studio: Communication Log (Revision)
====================================

.. admonition:: Note

   If you have not installed :ref:`Visual Studio Code <vsc-install>` on your
   computer yet, now would be the time to do so!

Code Together
-------------

Coding together allows you to work as a team so you can build bigger projects
faster.

In this studio, we will practice the common Git commands used when
multiple people work on the same code base.

You and a partner will begin by coding in tag-team shifts. By the end of the
task you should have a good idea about how to have two people work on the same
code at the same time. You will learn how to:

#. Quickly add code in pull + push cycles *(Important! This is the fundamental
   process!)*
#. Add a collaborator to a GitHub Project
#. Share *repositories* on GitHub
#. Create a *branch* in Git
#. Create a *pull request* in GitHub
#. Resolve merge conflicts (which are not as scary as they sound)

This lesson reinforces:

#. Creating repositories
#. Cloning repositories
#. Working with Git concepts: Staging, Commits, and Status.

Overview
---------

The instructor will discuss why GitHub is worth learning. You already know how
to use a local Git repository with one branch, giving you the ability to move
your code forward and backward in time. Working with branches on GitHub extends
this ability by allowing multiple people to build different features at the
same time, then combine their work. Pull requests act as checkpoints when code
flows from branch to branch.

Students *must* pair off for this exercise. If you have trouble finding a
partner, ask your TA for help.

Gitting Ready
-------------

Before you and your partner can begin your collaboration, you both need
practice with creating a new repository on GitHub. Your teamwork will soon
begin, but some preparation is required first.

Step 1: Create a New Local Repository
-------------------------------------

.. admonition:: Note

   Be careful if you try to use ``copy/paste`` with the ``git`` commands! The
   ``$`` symbols in the screenshots represent to the prompts in the terminal.
   They are NOT part of the commands.

#. In the terminal, navigate to your development folder. Enter the following 3
   commands to create a new project.

   ::

      $ mkdir communication-log
      $ cd communication-log
      $ git init

#. Launch Visual Studio Code. Use the *File* menu to open the
   ``communication-log`` folder.
#. Create a new file called ``index.html`` and open it in the workspace.
#. Paste in this code into ``index.html``:

   .. sourcecode:: html
      :linenos:

      <html>
         <body>
            <p>Radio check. Pilot, please confirm.</p>
         </body>
      </html>

#. Save your work, then stage and commit it.

   a. First, check the ``status``.

      ::

         $ git status
         On branch main

         Initial commit

         Untracked files:
         (use "Git add <file>..." to include in what will be committed)

            index.html

         nothing added to commit but untracked files present (use "git add" to track)

   b. The output shows is that ``index.html`` is not staged. Let's ``add``
      everything in this directory, then check the ``status`` again.

      ::

         $ git add .
         $ git status
         On branch main

         Initial commit

         Changes to be committed:
         (use "git rm --cached <file>..." to unstage)

            new file:   index.html

   c. The output tells us that the file is staged. Now let's ``commit``. After
      that, we can see a record of our progress by using ``git log``.

      ::

         $ git commit -m 'Started communication log.'
         [main (root-commit) e1c1719] Started communication log.
         1 file changed, 5 insertions(+)
         create mode 100644 index.html

         $ git log
         commit 679de772612099c77891d2a3fab12af8db08b651
         Author: Chris <chrisbay@gmail.com>
         Date:   Wed Apr 5 10:55:56 2021 -0500

            Started communication log.

Great! You've got your project going locally. The next step is to push the
project up to GitHub.

Step 2: Push Your Repository To GitHub
--------------------------------------

#. Go to your GitHub profile in a web browser. Click on the "+" button to add a
   new repository (called a *repo* for short).

   .. figure:: figures/studio/new-repo-button.png
      :alt: The New Repository link in the dropdown menu at top right on GitHub.

      The *New Repository* link is in the dropdown menu at top right on GitHub.

#. On the next page, fill in the Name and Description fields.
#. Uncheck *Initialize this repository with a README* and click
   *Create Repository*.

   .. figure:: figures/studio/create-repo.png
      :alt: Creating a new repository in GitHub by filling out the form.
      :width: 80%

      Create a new repository in GitHub

   .. admonition:: Note

      If you initialize with a README, in the next step Git will refuse to merge
      this repo with the local repo. There are ways around that, but it's faster
      and easier to just create an empty repo here.

#. After clicking, you should see something similar to:

   .. figure:: figures/studio/new-repo-push.png
      :alt: The page you see after creating an empty repository, with several options.
      :width: 80%

      Connecting to a repository in GitHub

#. Now go back to your terminal and copy/paste the commands shown in the GitHub
   instructions. These should be very similar to:

   ::

      $ git remote add origin https://github.com/your-username/communication-log.git
      $ git branch -M main
      $ git push -u origin main

   .. admonition:: Note

      The first time you push up to GitHub, you will be prompted to enter your
      account username and personal access token. Do this.
      
      You will then see a large amount of output that you can safely ignore. The
      final few lines will confirm a successful push. They will look something
      like this:

      ::

         To github.com:your-username/communication-log.git
            c7f97814..54993de3  main -> main

   .. admonition:: Warning

      Unless you've set up an SSH key with GitHub, make sure you've selected the
      HTTPS option in the Quick Setup. If you're not sure whether you have an SSH
      key, you probably don't.

#. Now you should be able to confirm that GitHub has the same version as your
   local project. Click around and see what is there. You can read all your
   code through GitHub's web interface. The files and code you see in your
   browser should match what you have in Visual Studio Code!

   .. figure:: figures/studio/repo-first-commit.png
      :alt: A repository with one commit in GitHub
      :width: 80%

      A repository with one commit in GitHub

Git Ready for Some Teamwork!
----------------------------

You've successfully created a new repository in GitHub and pushed content to
it. Now it's time to grab a partner and start collaborating on the same repo.

On to :ref:`Studio Part 2 <comm-log-part2>`!

Clone Repo
----------

.. todo:: Move cloning the repo here!

Instructions for cloning repo and adding a collaborator to the GH project...

Note that each partner needs to choose a role. The *Pilot* will need to clone
the repo from the *Base*, even though the former has their own!

Maybe have **Pilot** delete local repo? (Don't worry, you've got the original
saved on GH!)
