.. _terminal-parent-dir:

``..`` Details
==============

.. figure:: ./figures/initial.png
    :alt: Sample file tree

    Sample file tree


Imagine you are inside of this file system. ``..`` is a reference 
to your **parent directory**, aka the directory that CONTAINS your
current location.

Starting at the top, *launchcode_courses* is the parent directory
of both the *lc_101* and *data_analysis* directories.

If you move into *lc_101*, ``..`` then refers to *launchcode_courses*.

Moving further down into *unit_1*, ``..`` would then refer to *lc101*. 
``../..`` here refers to *launchcode_courses*.