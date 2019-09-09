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

Set Up Your Local Development Environment
------------------------------------------

As we continue to shift away from online work in repl.it to *local* development
on your computer, you need to install some specific software.

#. If you have not already done so, download and install
   :ref:`Visual Studio Code <vsc-install>` on your machine.
#. :ref:`Install Node on your computer <node-install>`, which also installs the
   NPM Command Line Interface (CLI). We discussed this briefly in the
   :ref:`Modules <npm-cli>` chapter, but now you are ready to use the tool
   outside of the automatic structure provided by repl.it.

The NPM CLI tool provides you with an efficient and deliberate way to install
other software and modules onto your computer. As you proceed through the next
four chapters, you will use the NPM CLI in the terminal to perform these
installations.
