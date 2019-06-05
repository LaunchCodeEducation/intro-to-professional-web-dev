.. _modules-index:

Modules
=======

.. toctree::
   :maxdepth: 3

   what-are-modules


High Level Plan

- Explain why modules are useful for organizing and sharing code
  - Code written by other developers that be included
  - don't reinvent the wheel, you don't have to build every app from scratch

- Use ``require`` to import modules(Core)
  - the module is an object or a function
  - Reference and use properties from the module

- Where does node look for the module
  - Core, Local, NPM
  - what happens when you require a module that can't be found

- Create a module and import it within another file in the same project
  - Use the ``module.exports`` object to expose module properties

- What is npm and use it require a module
  - a module is also called a package. aka node package manager
  - npm registry and website
  - npm cli (can this be done in repl.it?)

   - open terminal/shell in repl.it
   - right click in code editor window
   - click Command Palette
   - type in shell in search box, choose Open Shell

- simple overview of package.json
- Understand difference between repl.it and local env
- compare local npm to repl.it npm
