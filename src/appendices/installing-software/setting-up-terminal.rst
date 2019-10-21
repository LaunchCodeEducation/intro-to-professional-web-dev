.. _terminal-setupinstructions:

Setting Up Your Terminal
========================

The command line is a vital tool to learn for any programmer. Over the course of this program and your career, you will find yourself navigating to it frequently.

.. note::

   Once you have your terminal setup on your machine, make sure to pin it to the taskbar or add it to your dock!

Mac Users
---------

Good news! The Terminal application comes with every Mac.

You can access it one of two ways:

Through the Finder
^^^^^^^^^^^^^^^^^^

1. Open a new Finder window and navigate to the Applications folder.
2. Inside the Applications folder, you will find inside a Utilities folder.
3. Open the Utilities folder and inside is the Terminal application!

Through LaunchPad
^^^^^^^^^^^^^^^^^

1. If you are a fan of the LaunchPad features on Apple computers, hit the F4 key.
2. Inside the Other or Utilities folder, you can find the Terminal.

If you are still struggling to find the Terminal application, you can do a simple search in the Finder for it!

.. _terminal-setupinstructions-sudo:

.. index:: ! sudo

``sudo`` Commands
^^^^^^^^^^^^^^^^^

Some terminal commands require the addition of **sudo** at the front of the command. This name
gives the user *super user* rights. ``sudo`` is often required when installing software from the terminal.

.. sourcecode:: Bash

   $ sudo install mocha
   Password:
   
The Terminal will ask you for your machine's password. 

.. tip::
   
   When typing, don't be alarmed if you don't see your keystrokes while typing 
   your password. Your machine is still receiving this information.
      
Press *enter* when you are finished. If you're attempting to run a command from the terminal and receive a permissions error, 
check if adding ``sudo`` to your command will resolve the error.

Windows Users
-------------

1. In order to get your CLI up and running, you have to first install `Git Bash <https://git-scm.com/downloads/>`_.

   .. note::

      When you are doing your Git Bash setup, you only need to leave the default selected.

2. Once Git Bash is installed on your machine, you can find the folder for it through the Home screen.
3. Inside the folder, simply select Git Bash to open the appropriate CLI.
