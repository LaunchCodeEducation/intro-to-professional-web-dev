.. _terminal-basics-tutorial:

Terminal Basics Tutorial
========================

As mentioned in the terminal chapter, the essence of the command line is 
is text. Since this is quite different from how many may be used to using
their computers, this tutorial is meant to help you picture how your
machine is responding when you input common commands into the terminal.

Your computer is basically a file storage system. Sure, you may have many
applications installed. But where do they all live? In folders. Aka,
directories. The basics of terminal usage involve navigating these
directories.

Let's take a look at a given project opened in your VSCode editor:

.. figure:: ./figures/init_tree.png
    :alt: File tree in VSCode

    Sample file tree in VSCode

When working in the terminal, it can be helpful to think of yourself as
physically inside of the project's file system. File trees, like the one
above, are common visualization tools. Here's another map-like option
for imagining your file system:

.. figure:: ./figures/init.png
    :alt: Sample file system map

    Sample file system map

We'll navigate through and edit this sample project folder for the 
remainder of this tutorial. 

.. _terminal-current-dir:

Current Directory (``.``)
-------------------------

Imagining you are inside of this file system, ``.`` is a reference 
to your location, or **current directory**.

Starting at the top directory, *launchcode_courses*, ``.`` represents 
your current location.

.. figure:: ./figures/locate_launchcode_courses.png
    :alt: Inside top directory

    Your current directory is *launchcode_courses*.

Here, your terminal will look something like this:

.. figure:: ./figures/init_terminal.png
    :alt: Terminal view in launchcode_courses

    Your current directory is *launchcode_courses*.

Most of what you see to the left of the command prompt symbol, 
**$** will be different on your machine. The basic structure here is 
<machine_name>:<current_directory> <user_name>$
   
.. note::

   Some users choose to alter what they see before the command prompt.


``.`` itself isn't a command. If you type only ``.`` into the terminal,
you're not really telling the machine to do anything just yet. 

If you're curious, try it. 

.. note::

   Most commands require you to press *Enter* when you are ready to run.


You'll probably see a somewhat cryptic message, like this:

.. figure:: ./figures/current_dir_terminal.png
    :alt: Current directory prompt response

    Entering the symbol for your current directory only

That's ok! Basically, we just entered an incomplete command. Our syntax
wasn't quite right. Keep reading and we'll see how to properly use ``.``.

If you move into *lc_101*, ``.`` then refers to that directory. We'll 
cover how to move locations in detail down in :ref:`terminal-cd`.

.. figure:: ./figures/change_current_dir_terminal.png
    :alt: Change directory to lc_101

    We're now in *lc_101*

You may notice that the <current_directory> has updated but apart from 
that, the computer doesn't give us much response. This is quite common
and is a reason why our file system visuals come in handy to help remind 
us what we're doing.

Back in our map, we've done this:

.. figure:: ./figures/lc101_current_dir.png
    :alt: Current directory lc_101

    We're now in *lc_101*



.. _terminal-parent-dir:

Parent Directory (``..``)
-------------------------

``..`` is a reference to your **parent directory**, aka the directory 
that CONTAINS your current location.

Remember the VSCode file tree? That containment structure is represented
through indentation:

.. figure:: ./figures/init_tree.png
    :alt: File tree in VSCode

    *launchcode_courses* contains *data_analysis* and *lc_101*.


By the end of the :ref:`terminal-current-dir`, we found ourselves inside 
of *lc_101*.

.. figure:: ./figures/lc101_current_dir.png
    :alt: Current directory lc_101

    We're still in *lc_101*

*launchcode_courses* is the parent directory of both the *lc_101* and 
*data_analysis* directories. While we're in *lc_101*, ``..`` refers to 
*launchcode_courses*.

Moving further down into *unit_1*, 

.. figure:: ./figures/cd_unit1_terminal.png
    :alt: lc_101 to unit_1

    Moving into *unit_1*.

.. figure:: ./figures/unit1_current_dir.png
    :alt: unit_1 location

    We're now in *unit_1*.

``..`` now refers to *lc101*. 
``../..`` here refers to *launchcode_courses*.

Like ``.`` (:ref:`terminal-current-dir`), ``..`` isn't a command itself, but rather a notation. We're
now ready to tackle our first command!


.. _terminal-pwd:

``pwd`` Command
---------------

Entering the ``pwd`` command in your terminal returns your current 
location, aka your **working directory**.

.. figure:: ./figures/pwd_unit1_terminal.png
    :alt: pwd unit_1

    *unit_1* is the working directory.

The working directory is another term for the current directory. Think of this 
command as like the 'You are here' star on our file maps. 

.. figure:: ./figures/unit1_current_dir.png
    :alt: unit_1 location

    We're still in *unit_1*.

You're basically just telling the computer to give you your current location. 
This may seem basic, but this one is essential. *You need to know your current 
location when working in the terminal.* A lot of beginner programmers simply enter 
commands into the terminal without mind to where they are. ``pwd`` is like a sanity
check -  a quick way to ensure that you know where you are and what you're doing.
It's the file system counterpart to Git's ``git status``.

.. _terminal-ls:

``ls`` Command
--------------

Entering the ``ls`` command in your terminal returns the contents of your 
current directory. Recall, we're in *unit_1*.

.. figure:: ./figures/unit1_current_dir.png
    :alt: unit_1 location

    We're still in *unit_1*.
    
.. figure:: ./figures/ls_unit1_terminal.png
    :alt: unit_1 contents

    The innards of *unit_1*.

All of that looks to be in order. Let's move back out into *lc_101* and run ``ls``
from there.

.. figure:: ./figures/ls_lc101_terminal.png
    :alt: lc101 contents

    *lc101* contains the *unit_1* directory.

Notice that :ref:`terminal-pwd` after we moved. Also pay attention that ``ls`` 
only gives us a view one level deep. Now let's talk about how we move between
directories.

.. _terminal-cd:

``cd`` Command
--------------

``cd <path_name>`` relocates you to the provided path. We've seen it before, now
let's explore this command some more.

Remember, we're inside *lc_101*, 

.. figure:: ./figures/lc101_current_dir.png
    :alt: lc101 location

    We're in *lc_101*.


To change directories to our :ref:`terminal-parent-dir`, we run the following:

.. figure:: ./figures/cd_lc101_to_parent_terminal.png
    :alt: move to parent dir

    We're in *lc_101*.

It's pretty self-explanatory, now we're back in *launchcode_courses*.

.. figure:: ./figures/locate_launchcode_courses.png
    :alt: launchcode_courses location

    We're back to *launchcode_courses*.

Not surprisingly, to go down into *data_analysis*, we run ``cd ./data_analysis/``

.. figure:: ./figures/cd_data_analysis_terminal.png
    :alt: move to data_analysis

    Moving down into *data_analysis*.

.. figure:: ./figures/locate_data_analysis.png
    :alt: inside data_analysis

    We've made it to *data_analysis*.

Ok, so we know how to move one level above our current location (into our parent 
directory) and how to move one level below our working directory. But what if we 
wanted to get back to *lc_101* from where we are now, in *data_analysis*?

In order to move to a directory that is contained within the same parent as our 
working directory, we need to first go back up into the parent. 

.. figure:: ./figures/cd_sibling_terminal.png
    :alt: move to a peer directory

    Moving to a peer directory.

Do you see the faulty command? We tried running ``cd lc_101`` from inside 
*data_analysis* but the terminal did not recognize that path name from inside
the *data_analysis* directory. 

We already know how to move to a parent directory, ``cd ..``, above we see how we
can move into a parent directory and down into one of its children all in one command,
``cd ../lc_101/``. 

Here's a visual of where we've just been

.. figure:: ./figures/cd_sibling.png
    :alt: path to a peer directory

    Path to move to a peer directory.

For practice, let's go from our current spot in *lc_101*, down into *final_project*.

.. figure:: ./figures/lc101_to_final_project.png
    :alt: path from lc_101 to final_project

    Extended path to get to *final_project* from *lc_101*.

Above, we check our location as we navigate to make sure we know where we're going. 
If we're really confident though, we accomplish moving from *lc_101* to *final_project*
all in one go. Let's say we moved back to *lc_101* already.

.. figure:: ./figures/cd_shorter.png
    :alt: shorter path from lc_101 to final_project

    Quicker path to get to *final_project* from *lc_101*.

Are you starting to see how terminal navigation can get you places
swiftly?

Let's do one more quick move for fun. To go back to *lc_101*, all we need to do is
``cd ../../lc_101/``.

.. figure:: ./figures/final_project_to_lc101.png
    :alt: to lc_101 from final_project

    Quickly getting back to *lc_101* from *final_project*.

Perhaps you noticed that the computer does not return anything to you after a 
successful ``cd`` command. In the navigation samples above, we frequently rely on the 
:ref:`terminal-pwd` and the :ref:`terminal-ls` to remind us where we are and what paths
are available to us.

.. _terminal-mkdir:

``mkdir`` Command
-----------------

``mkdir <new_directory_name>`` creates a new directory *inside* your current 
location. 

We're in the *lc_101* directory. 

.. figure:: ./figures/lc101_current_dir.png
    :alt: lc_101 location

    We're back in *lc_101*.

Here, let's create a directory for Unit 2 materials.

.. figure:: ./figures/mkdir_unit2_terminal.png
    :alt: Making a new directory

    *unit_2* is created!

Again, the computer does not return anything to you after this command 
and simply responds ready to accept another prompt. But we can see from our helpful
:ref:`terminal-ls` that a new directory has been created.

And we can visualize our changes like this:

.. figure:: ./figures/new_unit2.png
    :alt: Sample file tree with a new directory

    mkdir creates a new directory

.. note::

   While ``mkdir`` creates a new directory, it does not place us into that directory.
   Additionally, we don't need to be in the parent of the newly created directory.
   We can run ``mkdir`` from anywhere within the file system, as long as we use the
   appropriate file path.


.. _terminal-rm:

``rm`` Command
--------------

``rm <item_to_remove>`` removes a given item from the file tree. 

Let's say we decide we no longer need our *cities.sql* data. 
We can remove it from the terminal:

.. sourcecode:: bash
   :linenos:

   $ rm cities.sql
   $ 

Once again, the computer does not return anything to you after this 
command and simply responds ready to accept another prompt. 
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


.. _terminal-cp:

``cp`` Command
--------------

``cp <source_path> <target_path>`` copies the item at the source and
puts it in the target path.

Take our sample file tree above. Say we're in *data_analysis* 
and we want to copy *cities.sql* into *final_project*. We can do this 
with ``cp``.

.. sourcecode:: bash
   :linenos:

   $ cp ./cities.sql ./final_project/
   $ 

Here's what that gives us:

.. figure:: ./figures/cp.png
    :alt: Sample file tree with a file copied

    cp copies an item


.. _terminal-mv:

``mv`` Command
--------------

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


.. _terminal-touch:

``touch`` Command
-----------------

``touch <new_file_name>`` creates a new file.

Back in *data_analysis*, lets add a new file to our *final_project* 
directory. 

.. sourcecode:: bash
   :linenos:

   $ touch ./final_project/more_sql.sql
   $ 

Here's what that gives us:

.. figure:: ./figures/touch.png
    :alt: Sample file tree with a new file

    touch adds a file


.. _terminal-ctrlc:

``ctrl + c`` Details
--------------------

*ctrl + c* can be used to exit a running program.

Some programs take different commands to exit. *ctrl + c* 
is sometimes used to prompt the running program for an 
exit command.


.. _terminal-clear:

``clear`` Command
-----------------

``clear`` wipes your terminal window of any previously run commands 
and outputs in case you need a clean screen to think straight. 

You probably won't encounter a scenario where you NEED to clear your
terminal, but it can be a nice command to know if you're a minimalist.

.. sourcecode:: bash
   :linenos:

   $ clear
   $ 


.. _terminal-man:

``man`` Command
---------------

``man`` is your best friend. Running ``man <command>`` gives you a manual
entry of what that command does, what options it takes, and more
documentation than you could ever need. It's so thorough, it makes this
guide blush. Any command you think you may need but you're not sure how 
to use it, or maybe you want to do something specific and are wondering if
there's a specialized option for it, use ``man`` to get more info!

Practice looking up some of the commands you know; maybe you'll learn a 
new option or two!

Some other terminal stuff you should know when using the manual:

- Some entries are very long! They will probably need to be scrolled 
    through. You'll know there's more to read if you see ``:`` at the 
    bottom of your terminal window. You can use your keyboard's arrow keys to
    navigate the entry. If you reach the bottom of the entry,
    you'll see a line that reads ``END``.

- Once you're finished reading, you'll need to exit the manual page 
    using the :ref:`terminal-q` command. 

.. _terminal-q:

``q``
-----

``q`` is another command for exiting a running program.
