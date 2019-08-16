Introduction
============

One of the main benefits of programming is we don't work in isolation. We can import 
modules that contain code that we can use to help us write our own programs. We use 
online documentation like MDN and W3Schools to help us learn how to utilize aspects of 
a programming language. We use online forums like Stack Overflow and Google to find 
answers to specific problems. We even use other people like our classmates, TAs, and
instructors to help figure out how to solve problems.

We can also use other people's data in our applications. There are multiple ways of 
using other people's data, or external data, in our applications. In this chapter, we 
will focus on using ``fetch()`` and ``JSON`` to request and use data.


API
---

.. index:: ! GUI

.. index::
   single: GUI; graphical user interface

.. index:: ! API

.. index::
   single: API; application programming interface

When using a website, we mainly work with **GUIs (Graphical User Interface)** which 
contain buttons, forms, text boxes, etc. However, our program does not know how to 
use a GUI. Programs use **APIs (Application Programming Interface)** need an to 
communicate with other programs.

Consider the software you use on a daily basis, like Microsoft Word, Google Chrome, 
or a music streaming device like Spotify. When you open the software, a window pops 
up on your screen and is filled with text, buttons, search bars, scroll bars, etc. 
Usually, with a little trial and error, you can learn how to use the interface 
easily. This interface we use is called a Graphical User Interface, or GUI for short.

How we interact with computers is with various interfaces, either GUI, or CLI. 
However, an application does not know how to use a GUI, or a CLI, and needs it's own 
interface to communicate with another application. So a new interface was defined so 
that one application could communicate with another application.
This interface was called an Application Programming Interface, or API for short.

An API is how one application communicates with another application. We will be 
making a request to an API in order to retrieve information we
need for our application.
