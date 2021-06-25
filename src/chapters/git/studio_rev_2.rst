.. _comm-log-part2:

Studio: Communication Log (cont.)
=================================

.. admonition:: Warning

   As you go through these steps, you'll be working with *branches*.
   
   It's very likely you will make changes to the code only to realize that you
   did so in the wrong branch. When this happens (and it happens to all of us)
   you can use ``git stash`` to cleanly move your changes to another branch.
   Read about how to do this in our :ref:`git-stash` tutorial.

Part 5: First Message Exchange
------------------------------

#. **Pilot**: Use the *File* menu in Visual Studio Code to open the cloned
   ``communication-log`` directory. Double click the ``index.html`` file to
   open it in the editor.

   Modify the HTML code to add your response to mission control. Be creative,
   the communication can go anywhere! Just don't ask your partner what you
   should write.
#. **Pilot**: After you finish, commit your change with the usual
   ``git status/git add ./git commit -m`` process.
#. **Pilot**: Push up your changes up to GitHub so **Control** can see them as
   well. Use the command:

   ::

      $ git push origin main
      Counting objects: 9, done.
      Delta compression using up to 4 threads.
      Compressing objects: 100% (9/9), done.
      Writing objects: 100% (9/9), 1.01 KiB | 0 bytes/s, done.
      Total 9 (delta 8), reused 0 (delta 0)
      remote: Resolving deltas: 100% (8/8), completed with 8 local objects.
      To git@github.com:username/communication-log.git
         511239a..679de77  main -> main

#. **Control**: Pull Pilot's changes down from GitHub with the command

   ::

      $ git pull origin main
      remote: Counting objects: 3, done.
      remote: Compressing objects: 100% (2/2), done.
      remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
      Unpacking objects: 100% (3/3), done.
      From github.com:username/communication-log
         e0de62d..e851b7e  main     -> origin/main
      Updating e0de62d..e851b7e
      Fast-forward
      index.html | 1 +
      1 file changed, 1 insertion(+)

#. **Control**: Notice that the code your local ``index.html`` file changes to
   reflect the line(s) Pilot added. Cool!

   Respond by adding a new HTML element and some text. Save, commit, and push
   your changes up to GitHub.
#. **Pilot and Control**: Play with the ``pull/edit/push`` process for a while!
   Repeat the cycle a few more times to add to your story.

.. admonition:: Tip

   In VS Code, right-click on the ``index.html`` tab. Choose the *Copy Path*
   option.

   .. figure:: figures/studio/copy-path.png
      :alt: Menu options that appear after right-clicking a file tab in VS Code. "Copy Path" is highlighted.
      :width: 30%

   Next, open a web browser and paste the path into the address bar. Ta da!
   Your webpage appears. By opening ``index.html`` in your browser, you can
   track your progress by refreshing the page after applying each change.
   
   Notice that the path in the address bar looks very similar to the result we
   would see from the ``pwd`` command in the terminal.

Step 5: Join the Project and Push
---------------------------------

Lorem ipsum...

Step 6: Pull Pilot's Line and Add Another Line
----------------------------------------------

Lorem ipsum...

