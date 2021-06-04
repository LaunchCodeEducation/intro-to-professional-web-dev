Exercises: Git
==============

Working in a Local Repository
-----------------------------

We will use our new terminal powers to move through the Git exercises.

#. In whichever directory you are keeping your coursework, make a new directory called ``Git-Exercises`` using the ``mkdir`` command. 
#. Inside the ``Git-Exercises`` directory, initialize a new Git repository using ``git init``.
#. Use ``git branch`` to check the default branch name. If necessary, change the
   branch name to ``main``.
#. Add a file called ``exercises.txt`` using the ``touch`` command in the terminal.
#. Commit your local changes using the ``git commit`` procedures.
#. Add ``"Hello World!"`` to the file called ``exercises.txt``.
#. Commit your local changes following the same steps that you used for step 5.
#. Run the ``git log`` command. Take a screenshot of the result. Make note of
   what you see!

Setting up a Github Account
---------------------------

For our remote repositories, we will be using `GitHub <https://github.com/>`__. 

To create your account, follow these steps:

#. Navigate to GitHub's site using the link above.
#. Sign up for an account on the homepage either by filling out the form or clicking the "Sign Up" button.
#. Once you have an account, you are ready to store your remote work.

Before August 13, 2021, each time users pushed changes to a remote repository
(or pulled new content from it), they were prompted to enter their GitHub
username and password. However, a username/password combination is not the most
secure method available. This is especially true for people who reuse the same
credentials across multiple websites. (You know who you are. Stop doing that!)

After 8/13/2021, GitHub changed its policy in an effort to boost account
security. Users must now create a *Personal Access Token* or an *SSH key* to
verify their identity.

Setting up a token for your account is fairly straightforward.

Create a Personal Access Token (PAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: personal access token

To use HTTPS to push and pull from GitHub, users must create a
**personal access token**. A PAT takes the place of a password, and the token
process is considered more secure than a username/password verification.

Once you create your PAT, you will use it instead of your password when
performing Git operations over HTTPS.

.. sourcecode:: bash

   $ git clone https://github.com/username/repo.git
   Username: your_username
   Password: your_token

Some users question the need for a PAT, since it looks like yet another
password they have to remember. Rather than diving into the lengthy debate and
justification, we'll focus on the main point: GitHub requires a PAT or similar
token. The platform is incredibly helpful, and we want to use it, so we'll
follow their advice.

GitHub provides detailed instructions for setting up your PAT. Follow steps
1 - 9 for `Creating a Token <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token>`__
carefully.

**Tips**:

#. The checkboxes in step 7 allow you to select which actions you're allowed
   to perform from the command line (terminal). For now, select the *repo*
   option.

   There's no harm in selecting more options, but you won't need any of them
   for this course.
#. After you generate your PAT in step 8, *copy and save it somewhere safe*!
   Your new PAT will NOT be an easy-to-remember sequence of characters (that's
   the whole point), so you need to record it somewhere.

   If you use a password manager, that's a perfect place to keep your PAT.
   If you use an unsecured spreadsheet or a folded piece of paper, you want to
   break that habit now.
#. If you will be pushing and pulling from a repository multiple times in
   quick succession, you can save your PAT in memory for a short time. Run the
   command:

   .. sourcecode:: bash

      $ git config credential.helper 'cache --timeout=3600'

   The next time you access your remote repo, Git will ask for your username
   and PAT. It will then remember your credentials for a certain amount of
   time. In the example above, ``timeout-3600`` saves your information for 1
   hour (3600 seconds). You can adjust the amount of time up or down as needed.

Create an SSH Key
-----------------

Difference between SSH and PAT...

Link to GitHub SSH docs...
