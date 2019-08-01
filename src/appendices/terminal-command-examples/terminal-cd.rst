.. _terminal-cd:

``cd`` Command
==============

.. figure:: ./figures/initial.png
    :alt: Sample file tree
    
    Sample file tree


``cd <path_name>`` relocates you to the provided path. 

Imagine you are inside of this file system. Starting at the top directory,
*launchcode_courses*, entering ``cd lc_101`` puts you inside of the *lc_101*
directory.

.. sourcecode:: bash
   :linenos:

   $ cd lc_101/
   $ 

The computer does not return anything to you after this command and 
simply responds ready to accept another prompt.

If you wanted to return back to your *launchcode_courses* directory,
you can do so with ``cd ..``.
See :ref:`terminal-parent-dir` for notes on hwo to reference a parent 
directory.

Back inside of *launchcode_courses*, say you would like to move into
*unit_1* in one step. You can do that!

.. sourcecode:: bash
   :linenos:

   $ cd lc_101/unit_1
   $