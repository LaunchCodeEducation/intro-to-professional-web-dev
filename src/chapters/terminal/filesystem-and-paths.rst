Filesystem and Paths
====================

.. index:: ! filesystem

A **filesystem** is a structure for the operating system to store the files and folders that make up the data of the operating system. 

Inside a filesystem, folders are referred to as **directories**.
Your **root directory** is your Home folder or C drive.
When you open a new terminal window to work in, it opens to your root directory.
The root directory is the **parent directory** for the folders stored inside of it. 

.. admonition:: Example

   Oftentimes, there is a ``Desktop`` folder inside the root directory.
   If there is a folder on your Desktop called "LC101_Homework", then the parent directory of ``LC101_Homework`` is ``Desktop``.
   The parent directory of ``Desktop`` is ``LC101_Homework``. 


A **path** for files and folders is the list of parent directories that the computer must go through to find that particular item.

Computers have two different types of paths: absolute and relative.
The **absolute path** is the path to a file from the root directory.
The **relative path** is the path to a file from the current directory. When working with a relative path, you may find yourself wanting to go up into a parent directory to find a file in a different child directory.
In order to do so, you can use ``..`` in the file path to tell the computer to go up to the parent directory.

.. admonition:: Example

   We have a file inside our ``LC101_Homework`` directory from the above example.
   We named that file ``homework.js``.
   The absolute path for ``homework.js`` is ``/Users/LaunchCodeStudent/Desktop/LC101_Homework`` for Mac users and ``C:\windows\Desktop\LC101_Homework`` for Windows users.
   If the current directory is ``Desktop``, then the relative path for ``homework.js`` is ``/LC101_Homework`` for Mac users and ``\LC101_Homework`` for Windows users.

   If ``homework.js`` was in a different directory called ``CoderGirl_Homework``, which is inside the ``Desktop`` directory, and the current directory was ``LC101_Homework``, then we would use the ``..`` syntax in our relative path.
   The relative path would then be ``/../CoderGirl_Homework`` for Mac users and ``\..\CoderGirl_Homework`` for Windows users.

Many programmers use paths to navigate through the filesystem in the terminal. We will discuss the commands to do so in the next section.