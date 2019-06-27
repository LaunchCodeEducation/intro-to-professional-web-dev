Why Use JavaScript Libraries
=============================

We use libraries to make our lives as developers easier. We can focus on solving our specific problems if we don't have to spend time figuring out how information flows throughout our project.

When it comes to web based applications there are two very different places code can exist: in the client's browser, and on the host's server.

A best practice is to separate the code bases for the two different locations. Both sides are required for the web app to work, but they can be thought of as two different projects.

An easier way to think of the two different sides of web app development would be to consider the front end as what the user interacts with, and sees. Consider the back end as the logic, or machinations that the user doesn't need ot think about. Similar to how an old mechanical clock works. The front end would be the face with the 12 numbers, and the two moving hands representing hours, and minutes. The user only needs the clock face to determine the time. The back end for the clock would be the various cogs, wheels, and power of the clock.

In this chapter we will use Angular as our front end JavaScript framework. Angular dictates how we will structure our files, and how the information will flow between the different files, and contains a various number of tools that will help us build out the part of the application our user's will interact with.

.. note:: js

   There are many other ways to create front end web applications with JavaScript. Popular frameworks for JavaScript include React, Vue, Ember, and others.

Angular is a component based framework. That means it breaks individual web pages into small components. Angular then combines all the components to create a web page.

Taking this component based approach allows us to separate the individual pieces of our application so we can focus on them one at a time.

Through the next three chapters we will look at the basic building blocks of an Angular application.

TODO: divide this introduction into sections, clean up the long paragraphs