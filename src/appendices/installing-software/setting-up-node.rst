.. _node-install:

Setting Up Node
================

Installing Node on your computer also installs the NPM Command Line Interface
(CLI), which allows you to run specialized commands in the
:ref:`terminal <terminal-chapter>`.

#. Follow this link to the `Node website <https://nodejs.org/en/download/>`__,
   and examine the selection screen:

   .. figure:: ./figures/node-download-screen.png
      :alt: Image of Node download screen.

      Node download screen.

#. The *LTS* version of Node is an older, reliable build that has been tested,
   debugged, and runs well. The *Current* version brings in newer features,
   but it is still being tested. Either option works for this course, but we
   recommend downloading the LTS version.
#. Click on the Windows or MacOS icon to download the installer to your
   computer. If you have a different operating system, select its 64-bit option
   from the list below the icons.
#. Run the installation program and follow the on-screen instructions.

   a. Accept to the licence agreement. Hopefully, doing so does not require you
      to give up your first born child.
   b. When asked for the installation location, etc. use the default options.

#. Verify that the installation was successful by opening the terminal and
   running the command ``node -v``. The output should match the version you
   downloaded.

   .. sourcecode:: bash

      $ node -v
      v##.##.#

