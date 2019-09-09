Why TypeScript?
===============

.. index:: ! statically typed language, ! dynamically typed language

The final chapters of the first unit cover a framework called Angular.
Angular runs on TypeScript for a couple of reasons.

First, TypeScript is a superset of JavaScript.
This means that you can write JavaScript code and use it in TypeScript files.

Second, TypeScript is a **statically typed language**.
A statically typed language is a language where the type of a variable is given
at the time the program is compiled. This is often achieved by adding the type
of the variable to the variable declaration. However, this is not what we have
been doing so far. JavaScript is a **dynamically typed language**. In a
dynamically typed language, the type of the variable is determined at runtime
and is based on the value inside the variable, not the variable declaration.

Statically typed languages are considered by many to be more stable and less
prone to production errors, because the errors will occur in development.

CLI With Local Development Environment
---------------------------------------

The following describes the steps for working with NPM outside of repl.it. Do
not worry about following along. We are simply reviewing these to familiarize
you with the general process.

#. `Install Node on your computer <https://nodejs.org/en/download/>`__, which
   also installs the NPM CLI tool.
#. Use the CLI tool in a terminal to install modules into your local project.
   The syntax is ``npm install <package_name>``, and running it downloads the
   module to your computer and adds an entry into a ``package.json`` file.
   This entry indicates that your project depends on the module called
   ``package_name``.
#. More detailed instructions can be found in the
   `NPM documentation <https://docs.npmjs.com/downloading-and-installing-packages-locally>`__.