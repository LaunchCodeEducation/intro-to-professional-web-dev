Introduction
============

One of the main benefits of programming is we don't work in isolation. We can import modules that contain code that we can use to help us write our own programs. We use online documentation like MDN, or W3Schools to help us learn how to utilize aspects of a programming language. We use online forums like StackOverFlow, and Google to find answers to specific problems. We even use other people like our classmates, TA's, and the instructor to help figure out how to solve problems. We can also use other people's data in our applications. There are multiple ways of using other people's data in our applications, but in this chapter we will focus on ``fetch()`` and ``JSON``.

In this chapter we will learn how to access the data located in an ``API``, using the ``fetch()`` method in JavaScript.

API
---
When we act as a web user we mainly work with GUIs (Graphical User Interface) which contains buttons, forms, textboxes, etc. However, our program does not know how to use a GUI, it needs an API in order to interact with another application.
Consider the software you use on a daily basis, like Microsoft Word, Google Chrome, or a music streaming device like Spotify. When you open the software a window pops up on your screen, and is filled with text, buttons, search bars, scroll bars, etc. Usually with a little trial and error you can learn how to use the interface easily. This interface we use is called a Graphical User Interface, or GUI for short. Later in this class we will use the command line, and you will learn how to use some Command Line Interfaces, or CLI for short. How we interact with computers is with various interfaces, either GUI, or CLI. However, an application does not know how to use a GUI, or a CLI, and needs it's own interface to communicate with another application. So a new interface was defined so that one application could communicate with another application. This interface was called an Application Programming Interface, or API for short.

API stands for Applicaiton Programming Interface. It is how one application communicates with another application. We will be making a request to an API in order to retrieve information we need for our application.