Respositories and Commits
=========================

In order to get started with a git repository, the programmer must first create one. The command for doing so is ``git init``.

Any time a signifcant change in functionality is made, a commit should be made.

If the programmer has created the Git repository and is ready to commit, they can do so by following the commit process. Git does have a simple commit command, however, making a proper commit requires that the programmers follow a longer procedure than just one command.
The procedure for making a commit to a Git repository includes 4 stages.

1. ``git status`` gives the programmer information about files that have been changed.
2. ``git add`` allows the programmers to add specific or all changed files to a commit.
3. ``git commit`` creates the new commit with the files that the programmer added.
4. ``git log`` displays a log of every commit in the repository.

If the steps above are followed correctly, the programmer will find their latest commit at the top of the log.

When using ``git status``, the output is split into two categories: modified tracked files and modified untracked files.
Tracked means that Git has an awareness of the file and untracked means that it is an entirely new file that Git has not seen before.

What if a programmer wants to start collaborating with their colleagues on a new project? They might need to start with the work that one of their colleagues has already done.
In this particular case, the programmer has to import the work that is being stored in an online repository onto their local machine.
They can clone a remote repository by using the ``git clone`` command. Github and other online Git systems give users the option to clone the repository through HTTP or SSH depending on their Github profile is set up.
Throughout this book, HTTP will be used.
