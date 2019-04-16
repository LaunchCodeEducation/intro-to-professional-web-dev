Respositories and Commits
=========================

Describe the basic commit flow and commands: status, add, commit, log

When making a commit, the programmer goes through 4 stages.

1. ``git status`` gives the programmer information about files that have been changed.
2. ``git add`` allows the programmers to add specific or all changed files to a commit.
3. ``git commit`` creates the new commit with the files that the programmer added.
4. ``git log`` displays a log of every commit in the repository.

Initialize a new Git repository

In order to get started with a git repository, the programmer must first create one. The command for doing so is ``git init``.

Commit to a local repository

If the programmer has created the Git repository and is ready to commit, they can do so.

Clone a project from a remote Git repository

If the programmer wants to take work off of the internet, they can clone a remote repository by using the ``git clone`` command.

Explain the two Git file statuses: tracked and untracked

Tracked means that Git has an awareness of the file and untracked means that it is an entirely new file that Git has not seen before.

Explain what types of changes should be within a commit

Any time a signifcant change in functionality is made, a commit should be made.
