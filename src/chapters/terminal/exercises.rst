Exercises: Terminal
===================


#. If you haven't done so already, set up your command line environment with
   instructions from the :ref:`terminal-setupinstructions` appendix.

#. Using your terminal, navigate to your Home directory using ``cd ~``.

#. Use ``ls`` to view the contents of your Home directory.

#. Use ``cd`` to move into your Desktop directory. For most, the command to do
   this is ``cd Desktop/`` since the Desktop is most often a child of the Home
   directory.

#. In the terminal, use ``mkdir`` to create a folder on the Desktop called
   'my_first_directory'. Look on your Desktop. Do you see it?

#. Use ``cd my_first_directory/`` to move inside that directory.

#. ``pwd`` to check your location.

#. There, make a file called 'my_first_file.txt' with
   ``touch my_first_file.txt``.

#. Open the file and write yourself a message!

#. Back in the terminal, list the contents of your current directory from the
   terminal with ``ls``.

#. Make a copy of your 'my_first_file.txt' from it's current spot to directly
   on the Desktop with ``cp my_first_file.txt ../my_first_copy.txt``.

#. Move back out to your Desktop directory from the terminal with ``cd ..``.

#. Use ``ls`` in the terminal to verify your 'my_first_copy.txt' on your
   Desktop. Open it up. Is it the same as your first file?

#. Move your copied file into your 'my_first_directory' with
   ``mv my_first_copy.txt my_first_directory/``.

#. Use ``ls`` to see that the copied file is no longer on your Desktop.

#. Type ``cd my_first_directory/``, followed by ``ls`` to confirm that your
   copy has been moved into 'my_first_directory'.

#. ``cd ..`` to get back out to your Desktop.

#. Type ``rm -r my_first_directory/`` and do a visual check, as well as ``ls``
   on your terminal, to verify that the directory has been removed.

