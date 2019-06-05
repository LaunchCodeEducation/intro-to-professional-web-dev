Require Modules
===============

Previous in this book we used the ``readline-sync`` module to get
use input. Below you will see the require statement on line 1 which
makes the ``readline-sync`` module accessible in your file.

.. sourcecode:: js
   :linenos:

   const input = require('readline-sync');

   const name = input.question("What is your name?");
   console.log(`hello ${name}`);

Modules are either objects or functions. If the module returns an object,
you can use dot notation to call functions on it. If the module returns
a single function you can use the variable reference to execute the function.

.. admonition:: Example

   What is the type of ``input`` from line ``const input = require(`readline-sync`);``?

   .. sourcecode:: js

      const input = require('readline-sync');

      console.log(typeof input);

      const name = input.question("What is your name?");
      console.log(`hello ${name}`);

   **Console Output**

   ::

      object

The string ``"object"`` is returned because the ``readline-sync`` module returns an object
when required. If a module returns a function, then the result of ``typeof`` would have been
``"function"``.


Where Do Modules Come From?
---------------------------
Modules can come from three places:

1. Local file on your computer
2. Node itself, known as Core modules
3. External registry such as NPM

How Does Node Know Which Place to Look?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Where Node looks for a module depends on the string value passed into ``require``.

1. For relative path values

   * A relative path starts with ``./`` or ``../``
   * ``const hello require("../hello");``

2. For non-relative paths

   a. Node looks for Core module with a matching name
   b. Node looks to NPM for a matching name

.. admonition:: Example

   Where does ``readline-sync`` get imported from?

   .. sourcecode:: js
      :linenos:

      const input = require('readline-sync');

   The value passed to ``require`` is NOT relative, so it must be a Core module or from
   NPM. The answer is NPM, let's learn more about NPM and how we can check that.


NPM
---
.. index:: ! NPM

.. index::
   single: TDD; node package manager

**NPM**, Node Package Manager, is a tool for finding and installing Node modules. NPM
has three major parts, a registry of modules and command line tool to install modules.

Package.json File
^^^^^^^^^^^^^^^^^
``package.json`` is a list of all the modules your project uses.

.. note::

   You not have seen this yet because by default repl.it hides this file. We will talk
   more about this later.

NPM Registry
^^^^^^^^^^^^
The NPM registry is a listing of thousands of modules that are stored on a remote server,
that can be required and downloaded to your project. The modules have been contributed
by other developers just like you.

There is an `online version of the registry <https://www.npmjs.com/>`_ that can be used to
search for a module by name or desired functionality.

.. admonition:: Example

   Go to `online NPM registry <https://www.npmjs.com/>`_ and enter "readline-sync" into the
   search packages input box.

   .. figure:: ./figures/readline-sync-npm-results.png

   A module that is an exact match appears as the first result. That is the ``readline-sync``
   module that we required. If you click on the first result you will be taken to the
   NPM page detailing the ``readline-sync`` module.

   On the details page you will see:

   * Usage statistics (how often the module is used)
   * Instructions on how to use the module (example code)
   * Version information
   * The author(s)
   * Sourcecode repository

   .. figure:: ./figures/readline-sync-npm-page.png

NPM Command Line Tool (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The NPM command line tool, cli, is installed with Node. The NPM cli is used in a computer's terminal
to install modules into a Node project. Before we can talk more about the NPM cli we need to discuss
the repl.it and NPM.

So far we have coded our Node projects inside of repl.it. Repl.it is great, it allows us to simulate
a development environment WITHOUT having to install any software on our computers. Next we will detail
how using the NPM CLI is different when using repl.it.

NPM CLI With Local Development Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You do not need to follow along. We are going to go over the steps so that you are familiar with
how NPM works outside of repl.it.

1. Install Node on your computer

   * This will also install the NPM CLI tool

2. Use the CLI tool in a terminal to install modules into your project

   * This will add an entry into the ``package.json`` file indicating that your project depends
   on the modules listed.

3. Finally run ``npm install`` in the terminal to download the modules to your computer.


NPM CLI With repl.it
^^^^^^^^^^^^^^^^^^^^
This you can follow along with because you are familiar with repl.it.

.. admonition:: Example

   Fork this `example repl.it <https://repl.it/@launchcode/npm-with-replit-starter>`_.

   Because we are in repl.it we can not use the NPM CLI. We will have to use the repl.it
   interface to add the modules we want.

   1. Click on the Packages icon in the left menu
   2. Then enter "readline-sync" in the search box
   3. Click on the top matching result

   .. figure:: ./figures/replit-search-for-module.png

   4. Verify this is the module you want, then click on the plus icon.

   .. figure:: ./figures/replit-add-module.png

   Clicking the plus icon adds a ``package.json`` file that includes a dependency listing for
   ``readline-sync``. Notice that the results tab shows console output indicating that
   the module has been installed.

   .. figure:: ./figures/replit-package-json-added.png

   Even though we have added ``readline-sync`` to our package.json, our code still fails
   because ``input`` is not defined. The final step of requiring ``readline-sync`` will
   fix that.
   
   6. Add ``const input = require("readline-sync");`` to line 1.

   .. sourcecode:: js
      :linenos:

      const input = require("readline-sync");

      const name = input.question("What is your name?");
      console.log(`hello ${name}`);

.. note::

   So far we have used repl.it without a ``package.json`` file. That was possible because
   repl.it is trying to make the development experience as easy as possible. Coding in a
   local development environment is not so kind.
