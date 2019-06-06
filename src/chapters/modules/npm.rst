NPM
====

.. index:: ! NPM

.. index::
   single: TDD; node package manager

**NPM**, Node Package Manager, is a tool for finding and installing Node
modules. NPM has two major parts:

#. A registry of modules.
#. Command line tools to install modules.

NPM Registry
-------------

The NPM registry is a listing of thousands of modules that are stored on a
remote server, that can be required and downloaded to your project. The modules
have been contributed by other developers just like you.

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
----------------------------

The NPM command line tool, cli, is installed with Node. The NPM cli is used in
a computer's terminal to install modules into a Node project. Before we can
talk more about the NPM cli we need to discuss the repl.it and NPM.

So far we have coded our Node projects inside of repl.it. Repl.it is great, it
allows us to simulate a development environment WITHOUT having to install any
software on our computers. Next we will detail how using the NPM CLI is
different when using repl.it.

NPM CLI With Local Development Environment
-------------------------------------------

You do not need to follow along. We are going to go over the steps so that you
are familiar with how NPM works outside of repl.it.

1. Install Node on your computer

   * This will also install the NPM CLI tool

2. Use the CLI tool in a terminal to install modules into your project

   * This will add an entry into the ``package.json`` file indicating that your
     project depends on the modules listed.

3. Finally run ``npm install`` in the terminal to download the modules to your
   computer.


NPM CLI With repl.it
---------------------

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
