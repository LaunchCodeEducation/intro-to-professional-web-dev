How to Do Stuff in the Terminal
===============================

Navigating the Terminal Window
------------------------------

Moving from a GUI to a CLI can be difficult when we are so used to dragging our files from one folder to another.
Here are some key indicators that the terminal gives us to show where we are:

.. index:: ! prompt

.. sourcecode:: bash

   LaunchCode-Super-Computer:~ lcstaffmember$

This line is called the **prompt**. The prompt lets us know that the terminal is ready to accept commands.
``LaunchCode-Super-Computer`` is the name of the computer. The ``~`` tells us we are currently in the Home directory. The Home directory is the folder that contains everything in the computer.
``lcstaffmember`` is the username of the person who has logged onto the terminal. We will be typing all of our commands after the ``$``.

As we navigate through our filesystem, the terminal will rarely output a line to let us know that the change has occurred.
We have to keep our eye out on our prompt as we enter our commands. The name of the computer and the username will not change, however, the space where the ``~`` is, will.
That indicates our current directory.

Basic Commands
--------------

There are many commands you can use in the terminal to move through the filesystem of your computer and projects.

.. list-table:: Basic Terminal Commands
   :header-rows: 1
   :widths: auto

   + - Command
     - Result
   + - ``ls``
     - Lists all files and folders in the current directory.
   + - ``cd <new-directory>`` 
     - Navigates from the current directory to ``new-directory``.
   + - ``pwd``
     - Prints the path of the current directory.
   + - ``mkdir <new-folder>``
     - Creates ``new-folder`` inside the current directory.
   + - ``touch <new-file>``
     - Creates a file called ``new-file`` in the current directory.  
   + - ``rm <old-file>``
     - Removes ``old-file`` from the current directory. 

.. note::

   ``rm`` will permanently remove items from the computer and cannot be undone.

Beyond these basic commands, there are some shortcuts if you don't want to type out the full name of a directory or simply can't remember it.

.. list-table:: Directory Shortcuts
   :header-rows: 1
   :widths: auto

   + - Shortcut
     - Where it goes
   + - ``~``
     - The Home directory
   + - ``.``
     - The current directory
   + - ``..``
     - The parent directory of the current directory

