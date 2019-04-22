Branches
========

.. index:: ! branch

A **branch** in Git is a way for programmers to keep two separate versions of their work. 

Branches can be used for storing and testing new features for software before it goes live.
If a lot of people are working on different aspects of software, they can do their work in separate branches and then merge them together once they are done.

Many programmers keep the live version of their code in the master branch. For that reason, the master branch is the default branch and work should be done off of a new branch.

So a programmer is on master and they want to start building a new feature in a new branch. Their first step would be to create a new branch for their work.
To create a branch, the command is ``git checkout -b <branch name>``. By using this command, not only is a new branch created, but also the programmer is switched to their new branch.

If the branch already exists, the programmer may want to just switch to that branch. To do so, the command is ``git checkout <branch name>``.
Feature branches are for storing individual features before incorporating them into a larger piece of software.