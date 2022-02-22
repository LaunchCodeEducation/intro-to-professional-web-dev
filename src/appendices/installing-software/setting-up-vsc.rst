.. _vsc-install:

Setting Up Visual Studio Code
=============================

.. index:: ! IDE, ! integrated development environment

Before we start coding on our computer, we need to make sure we have the right tools! Programmers use **integrated development environments** (IDE) to write and run their code.
The development environment we will be using for this class is Visual Studio Code.
In addition to simply writing and running code, Visual Studio Code has tools that recognize errors in our code and has an integrated terminal so we can navigate through our filesystem to find the files that need our attention.

.. note::

   Visual Studio Code is very customizable. Once you have everything set up, you can take additional steps to personalize your workspace such as changing the theme.

Go to the Visual Studio Code `download page <https://code.visualstudio.com/download/>`_ and download the appropriate version for your operating system.

Open your new copy of Visual Studio Code. To open one of your coding projects, go to `File > Open` and select the project you want to work on.

To start working with the terminal, go to `Terminal > New Terminal`. The new terminal window will open on the bottom right.

Windows Users
-------------

The terminal is in powershell, not Git Bash. To change this, open the Command Palette by going to `View > Command Palette`. Type "Select Default Profile" in the search window and select "Terminal: Select Default Profile" from the menu.
Change the default to Git Bash.

Now every time you open the terminal, it will default to bash!

.. admonition:: Note

   If Git Bash is not an option when attempting to change the terminal profile, try downloading the `Github Pull Requests and Issues extension <https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github>`__.
   This extension comes with terminal integration.

   Restart Visual Studio Code and then go into the Command Palette again to change the terminal profile.



