.. _terminal-rm:

``rm`` Command
==============


.. figure:: ./figures/initial.png
    :alt: Sample file tree

    Sample file tree


``rm <item_to_remove>`` removes a given item from the file tree. 

Let's say we decide we no longer need our *cities.sql* data. 
We can remove it from the terminal:

.. sourcecode:: bash
   :linenos:

   $ rm cities.sql
   $ 

The computer does not return anything to you after this command and 
simply responds ready to accept another prompt. 
But we can visualize the results:

.. figure:: ./figures/rm.png
    :alt: Sample file tree with a file removed

    rm removes an item

To remove a directory entry, rather than simply a file, requires an 
option on the command. A common method to remove a directory is to 
use the ``-r`` option, although there are other choices.


Let's say we're back up top in *launchcode_courses* directory and we want
to remove the entirety of the *data_analysis* directory. We can run:

.. sourcecode:: bash
   :linenos:

   $ rm -r data_analysis/
   $ 

Which results in:

.. figure:: ./figures/rm-r.png
    :alt: Sample file tree with a directory removed

    rm -r removes a directory entry