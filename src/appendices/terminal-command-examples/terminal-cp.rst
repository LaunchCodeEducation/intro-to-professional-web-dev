.. _terminal-cp:

``cp`` Command
==============


.. figure:: ./figures/initial.png
    :alt: Sample file tree

    Sample file tree


``cp <source_path> <target_path>`` copies the item at the source and
puts it in the target path.

Take our sample file tree above. Say we're in 
*data_analysis* and we want to copy
*cities.sql* into *final_project*. We can do this with ``cp``.

.. sourcecode:: bash
   :linenos:

   $ cp ./cities.sql ./final_project/
   $ 

Here's what that gives us:

.. figure:: ./figures/cp.png
    :alt: Sample file tree with a file copied

    cp copies an item
