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
#. Click the *Sign Up* button and follow the on-screen directions.
#. Once you have an account, you are ready to store your remote work.

Before August 13, 2021, when users pushed changes to a remote repository (or
pulled new content from it), they were prompted to enter their GitHub username
and password. However, a username/password combination is not the most
secure method available. This is especially true for people who reuse the same
credentials across multiple websites. (You know who you are. Stop doing that!)

In an effort to boost account security, GitHub changed its policy. Users must now
create a *Personal Access Token* or an *SSH key* to verify their identity.

Setting up a token for your account is fairly straightforward.

Create a Personal Access Token (PAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: personal access token

To use HTTPS to push and pull from GitHub, users must create a
**personal access token**. A PAT takes the place of a password, and the token
process is considered more secure than a username/password verification.

Once you create your PAT, you will use it instead of your password to perform
HTTPS Git operations.

.. sourcecode:: bash

   $ git clone https://github.com/username/repo.git
   Username: your_username
   Password: your_token

Some users question the need for a PAT, since it looks like another password
they have to remember. Rather than diving into a lengthy debate and
justification, we'll focus on the main point: *GitHub requires a PAT or similar
token*. The platform is incredibly helpful, and we want to use it, so we'll
follow their advice.

GitHub provides detailed instructions for setting up your PAT, so we will use
their documentation. Follow steps 1 - 9 for `Creating a Token <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token>`__
carefully.

**Tips**:

#. The checkboxes in step 7 select the actions you're allowed to perform from
   the command line (terminal). For now, just choose the *repo* option.

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
   time. In the example above, ``timeout=3600`` saves your information for 1
   hour (3600 seconds). You can adjust the amount of time up or down as needed.
#. **Mac Users**: At the bottom of the PAT documentation page, you can find
   some OPTIONAL instructions for saving your PAT in the MacOS *Keychain* app.

Optional: The SSH Key
---------------------

As an alternative to interacting with GitHub via HTTPS, developers can use the
SSH protocol instead. A description of the differences between HTTPS and SSH is
beyond the scope of this text. However, we don't need to understand the nuts
and bolts of SSH. We just need to be able to use it.

With an SSH key, you can connect to your GitHub repositories without needing to
enter your username and PAT each time you push, pull, or perform some other
action. This sounds great! The drawback is that it takes more work to set up.

As we mentioned before, this book assumes the HTTPS protocol. However, the
GitHub developers make it easy to use either one. If you would like to explore
how to create an SSH key, here are the relevant instructions:

#. `General info about GitHub and SSH <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh>`__
#. `Generate a new SSH key <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`__
#. `Add the SSH key to your GitHub account <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`__
#. `Protecting your SSH key <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/working-with-ssh-key-passphrases>`__

.. admonition:: Warning

   For each page, make sure you click on the tab that matches your operating
   system (Mac, Windows, Linux).
