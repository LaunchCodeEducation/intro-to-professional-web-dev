Compiling TypeScript
====================

To work with TypeScript in our Node environment, we'll need to install the TypeScript
module. We talked before about running JavaScript in Node. Unlike JavaScript, TypeScript
cannot be run directly in Node. TypeScript files must first be transformed, or compiled,
into JavaScript.

In this section, you will install the compiler and then practice compiling and
running a small TypeScript program from the terminal.

To install TypeScript, in your terminal, type

.. sourcecode:: bash

   $ npm install -g typescript

Once you have TypeScript installed, you'll be able to run 

.. sourcecode:: bash

   $ tsc -v

``tsc`` is is the TypeScript compiler and ``-v`` is the version flag to show us that
we have TypeScript and it's compiler installed. 

``hello_world.ts``
------------------

In true tutorial form, let's write a quick ``Hello, World`` program so we can see this 
compiling in action.

In your code editor, create a new file called ``hello_world.ts``. In it, initialize a 
variable called ``message`` with the string value ``'Hello, World'``. Print the message.

.. sourcecode:: ts
   :linenos:

    let message: string = 'Hello, World';
    console.log(message);


In the terminal, navigate into the directory that houses your ``hello_world.ts`` file. 
Compile the code with the following command:

.. sourcecode:: bash

   $ cd Desktop/
   $ ls 
   hello_world.ts
   $ tsc hello_world.ts
   $ ls
   hello_world.js hello_world.ts

If your TypeScript file is free of syntax errors, you won't see a response from the
terminal directly. However, you should see that you now have a newly generated file
in your working directory called ``hello_world.js``. Open it up and take a look!

Back in the terminal, run that JavaScript file

.. sourcecode:: bash

   $ node hello_world.js
   Hello, World

Look at that! Your message printed. You're now running your own code straight from 
the terminal!

.. note::

   Changing your TypeScript file won't update the corresponding JavaScript file
   unless you re-compile.

You'll need these compiling and executing steps for the exercises in the following 
section, so refer back here as needed.

