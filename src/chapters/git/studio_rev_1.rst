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

You and a partner will code in tag-team shifts. By the end of the studio, you
should have a good idea about how two people can work on the same code at the
same time. You will learn how to:

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

Before you and your partner can begin your collaboration, some preparation is
required first. You both need to practice creating a new repository on GitHub.

Step 1: Create a New Local Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Warning

   Be careful if you try to ``copy/paste`` the ``git`` commands! The ``$``
   symbol in the sample code represents the terminal prompt. The symbol is NOT
   part of the commands.

#. In the terminal, navigate to your development folder. Enter the following 3
   commands to create a new project.

   ::

      $ mkdir communication-log
      $ cd communication-log
      $ git init

#. Launch Visual Studio Code. Use the *File* menu to open the
   ``communication-log`` folder.
#. Create a new file called ``index.html`` and open it in the workspace.
#. Paste this code into ``index.html``:

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
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

         $ git commit -m "Started communication log."
         [main (root-commit) e1c1719] Started communication log.
         1 file changed, 5 insertions(+)
         create mode 100644 index.html

         $ git log
         commit 679de772612099c77891d2a3fab12af8db08b651
         Author: Chris <chrisbay@gmail.com>
         Date:   Wed Apr 5 10:55:56 2021 -0500

            Started communication log.

#. Use the command ``git branch`` to check the name for the default branch. If
   necessary, change the name to ``main``.

   ::

      $ git branch
      * default_name

      $ git branch -m default_name main.

   GitHub uses ``main`` for its default branch. To make things easier, you
   should always try to match your local and remote branch names.

Great! You've got your project going locally. The next step is to push it up to
GitHub.

Step 2: Push Your Repository To GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Go to your GitHub profile in a web browser. Click on the "+" button to add a
   new repository (called a *repo* for short).

   .. figure:: figures/studio/new-repo-button.png
      :alt: The New Repository link in the dropdown menu at top right on GitHub.

      The *New Repository* link is in the dropdown menu at top right on GitHub.

#. On the next page, fill in the *Name* and *Description* fields. Also, uncheck
   the *Initialize this repository with a README* option, then click 
   *Create Repository*.

   .. figure:: figures/studio/create-repo.png
      :alt: Creating a new repository in GitHub by filling out the form.
      :width: 80%

      Create a new repository in GitHub.

   .. admonition:: Note

      If you initialize with a README, Git will refuse to merge the remote repo
      with your local one. There are ways around this, but it's faster and
      easier to just create an empty repo on GitHub.

#. After clicking, you should see something similar to:

   .. figure:: figures/studio/new-repo-push.png
      :alt: The page you see after creating an empty repository, with several options.
      :width: 80%

      Connecting to a repository in GitHub.

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

#. Confirm that GitHub has the same version as your local project. Click around
   and see what is there. You can view all your code through GitHub's web
   interface. The files and code you see in your browser should match what you
   have in Visual Studio Code!

   .. figure:: figures/studio/repo-first-commit.png
      :alt: A repository with one commit in GitHub
      :width: 80%

      A repository with one commit in GitHub.

Git the Teamwork Started!
-------------------------

You've successfully created a new repository in GitHub and pushed content to
it. Now it's time to grab a partner and start collaborating on the same repo.

You are going to simulate a radio conversation between a shuttle pilot and
mission control. You and your partner will alternate tasks, so decide who will
be the **Pilot** and who will be the **Control**.

Even when it is not your turn to complete a task, read and observe what your
partner is doing. The steps here mimic a real-world collaborative Git workflow.

Step 3: Add A Collaborator
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Control**, the first step is yours. In order for **Pilot** to make changes to
your GitHub repository, you must invite them to collaborate.

#. **Control**: In your web browser, go to your ``communication-log`` repo.
   Click the *Settings* button then select the *Manage Access* option.

   .. figure:: figures/studio/manage-access.png
      :alt: Click "Settings" and "Manage Access" to let other users modify the repo.
      :width: 70%

      Manage access to your repo.

#. **Control**: Click on the green *Invite a collaborator* button. Enter your
   partner's GitHub username and click *Add to repository*.

   .. figure:: figures/studio/add-repo-partners.png
      :alt: Enter a GitHub username, then click the Add button.
      :width: 40%

      Choose who else can modify your GitHub repo.

#. **Pilot**: You should receive an email invitation to join this repository.
   View and accept the invitation.

.. admonition:: Note

   **Pilot**: If you don't see the email, check your Spam folder. If you still
   don't have the email, login to your GitHub account. Visit the URL for 
   Control's copy of the repo. You should see an invite notification at the
   top of the page.

Step 4: Clone Project from GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pilot**, this next step is a little inconvenient, but we know you can handle
it! You will be changing *Control's* ``communication-log`` repo, not yours.
Unfortunately, both projects have the same name. To avoid confusion, find your
*local* ``communication-log`` folder on your machine. RENAME IT!

Once that change is made, continue on with the steps.

#. **Pilot**: Go to Control's GitHub profile and find their
   ``communication-log`` repo. Click on the green *Code* button. Select the
   HTTPS option and copy the URL to your clipboard.

   .. figure:: figures/studio/code-button.png
      :alt: The Code button is on the right-hand side of a project's main page.
      
      Cloning a repository in GitHub

#. **Pilot**: In your terminal, navigate back to your development folder and
   clone Control's repo. The command should look something like this:

   ::

      $ git clone https://github.com/username/communication-log.git

   Replace the URL with the address you copied from GitHub.

#. **Pilot**: You should now have a copy of **Control's** project on your
   machine.

Git Talking
-----------

Whew! That was quite the setup experience. Now you're ready to dive into the
main part of the assignment.

On to :ref:`Studio Part 2 <comm-log-part2>`!
