Filesystem and Paths
====================

.. index:: ! filesystem, directory, subdirectory, root directory, parent directory

A **filesystem** is a structure for the computer to store the files and folders
that make up the data of the operating system.

Inside a filesystem, folders are referred to as **directories**. Folders that exist inside other folders are 
called **subdirectories**. A **root directory** can refer to a few different things but essentially means the 
top-most directory of a given system. In other words, a root directory is not a sub-directory - but it will probably 
contain its own subdirectories. Inside the machine you work with called your computer, the root directory is the 
location of primary hard drive - in Windows, that's your C drive; in a Mac, the root directory is represented as ``/``.
The root directory is the **parent directory** for the folders stored inside of it.

.. admonition:: Example

   Most of you have a ``Desktop`` folder on your computer. If there
   is a folder on your Desktop called "LC101_Homework", then the parent directory
   of ``LC101_Homework`` is ``Desktop``. 

A **path** for files and folders is the list of parent directories that the computer must go through to find that particular item.

Filesystems have two different types of paths: absolute and relative.
The **absolute path** is the path to a file from the root directory.
The **relative path** is the path to a file from the current directory. When working with a relative path, you may find yourself wanting to go up into a parent directory to find a file in a different sub, or child, directory.
In order to do so, you can use ``..`` in the file path to tell the computer to go up to the parent directory.

.. admonition:: Example

   We have a file inside our ``LC101_Homework`` directory from the above example.
   We named that file ``homework.js``.
   The absolute path for ``homework.js`` is ``/Users/LaunchCodeStudent/Desktop/LC101_Homework`` for Mac users and ``C:\windows\Desktop\LC101_Homework`` for Windows users.
   If the current directory is ``Desktop``, then the relative path for ``homework.js`` is ``/LC101_Homework`` for Mac users and ``\LC101_Homework`` for Windows users.

   If ``homework.js`` were in a different directory called ``CoderGirl_Homework``, which is inside the ``Desktop`` directory, and the current directory were ``LC101_Homework``, then we would use the ``..`` syntax in our relative path.
   The relative path would then be ``/../CoderGirl_Homework`` for Mac users and ``\..\CoderGirl_Homework`` for Windows users.

Many programmers use paths to navigate through the filesystem in the terminal.
We will discuss the commands to do so in the next section.
