.. _terminal-mv:

``mv`` Command
==============

.. figure:: ./figures/initial.png
    :alt: Sample file tree

    Sample file tree


``mv <item_to_move> <target_path>`` moves an item to the target path.

Back in *data_analysis*, lets move *cities.sql* into *final_project*. 

.. sourcecode:: bash
   :linenos:

   $ mv ./cities.sql ./final_project/
   $ 

Here's what that gives us:

.. figure:: ./figures/mv.png
    :alt: Sample file tree with a file moved

    mv moves an item