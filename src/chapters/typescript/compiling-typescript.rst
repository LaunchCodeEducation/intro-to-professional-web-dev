Compiling TypeScript
====================

To work with TypeScript in our Node environment, we'll need to install TypeScript. 
In your terminal, type 

``npm install -g typescript``.

Once you have TypeScript installed, you'll be able to run 

``tsc -v``.

``tsc`` is is the TypeScript compiler we'll need to run TypeScript programs in our terminal. 

To compile a TypeScript file, you'll run 

``tsc <ts_file.ts>``.

This compiles your TypeScript into a separate JavaScript file. If you look in your file
tree, or the directory where your ``ts_file.ts`` resides, you'll see a newly generated 
``ts_file.js`` file. Open it up and take a look!

Now, to run that JavaScript file, back in the terminal, type

``node <ts_file.js>``