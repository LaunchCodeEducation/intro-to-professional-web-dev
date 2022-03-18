.. _tested-code:

Tested Code
===========


We created this page to introduce you to working within projects that contain unit tests. 
We use unit tests to ensure that any code you create meets desired specifications. 
Unit tests can verify datatypes, variable declarations, and even proper spelling. 
These tests make sure everything works as intended.

LaunchCode uses tests to assist with grading assignments, starting with Assignment 1. 
This is not meant to deter you.  Tests help us provide you with feedback more quickly.  
By using tests, there will be more code in the starting codebase.  
When you open an assignment, you might not recognize all the code, and that is okay.
Instructions will always be available either in the starter code or the textbook.

In this demo, you will learn how to work within wrapper functions and run the tests to verify your code. 
Use this appendix entry as a reference for any future assignments.


Opening a New Project
---------------------

When opening any new codebase, take a moment and look at what it contains. 
This project contains many files and folders, constant variables, and functions. 
As you scan through the starter code, take note of any comments. 
Comments will either contain instructions or notes about the code.  Look for "TODO" or section numbers.  
Don't forget to use the textbook instructions too.



First Glance at any Tests
-------------------------

When working with code that has unit tests as part of the starter code, first make a point to look for any comments.  
It sounds simple, but code with unit tests can be more visually cluttered than you might be used to. 
Take a few minutes to really explore for any comments.  

Next, read through the names of any code elements.  Are there any variables?  What are they called?  Have then been instantiated yet?
Are there any other elements that have names, like functions, or constants?  Focus on the names right now.  Don't worry about what these things are right now.
Do you see the names used in the codebase?  In the same file?  In a different file?

Comments and names are great places to start.  Let's look at an example.  Fork and open this `replit <https://replit.com/@launchcode/Wrapper-Demo>`_.  
Look for comments and the names of elements.  Don't code yet.

``index.js``
^^^^^^^^^^^^
This file contains comments and a constant.
Complete the directions.  You should see the following output:

.. sourcecode:: bash
   
   node index
   Hello!

Great.  That is all that you need to worry about in this file.


``hello.js``
^^^^^^^^^^^^

Find the file pane.  It should be left to the left of the code editor.  
You should see a list of files, including ``index.js``, as well as, a folder called ``spec``, and another file called ``hello.js``.
Open the ``hello.js`` file.  Before you start coding, read through for comments and anything with a name.

This file contains a function called ``hello``.  Read the commented instructions within this file and code appropriately.

If you followed the instructions, you should have the following output:

.. sourcecode:: bash
   
   node index
   Hello, World!


``hello.spec.js`` 
^^^^^^^^^^^^^^^^^

So far, you have worked with the test function, ``hello``, but you have not actually performed any tests. 
The tests are located within the spec folder in a file called ``hello.spec.js``. 
As the comments will tell you, there is nothing that you need to change in this file. 
This file runs the test on our hello function from the ``hello.js`` file. 
The test expectations have already been provided for you.

.. admonition:: note 

   Make sure that you are following the directions exactly.

Running the Tests
^^^^^^^^^^^^^^^^^

So far, we have not actually performed any of the tests.
They are not activated until we call them from the terminal.

To run your tests, type ``npm test`` in the command line of the terminal.
Since we are using replit, that means type this below any output in the very right screen of the replit IDE.

.. sourcecode:: bash
   
   node index
   Hello, World!
   npm test

If your output screen looks like this, hit enter and your tests will run.

If you have written the correct code, the tests will pass.  
When a test runs, the console will log information about the test.  The dot in **Line 6** is a quick indicator that we passed. 
In replit, this will be green for a pass.


.. sourcecode:: bash 
   :linenos:
   
   > working-within-tests@1.0.0 test /home/runner/Working-Within-Tests-Demo
   > jasmine

   Randomized with seed 21669
   Started
   .


   1 spec, 0 failures
   Finished in 0.008 seconds
   Randomized with seed 21669 (jasmine --random=true --seed=21669)



What happens if you fail a test?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return to the ``hello.js`` file.  Replace the string inside the ``hello`` function with something that is *not* "Hello, World!" 
Maybe say hello to your friend or pet? 

.. admonition:: note

   "Hello, Coder!" was used for demoing the failed test.

   If your console is too crowded, you can clear it in two ways.  Either clear it by clicking the "X" in the top right corner or type ``clear`` directly into the console.

Once you have changed the string, run the program.

.. sourcecode:: bash

   node index
   Hello, Coder!

The program ran beautifully.  As it should.  We updated the input that will be printed to the console.
Let's check our output with the tests.  Type ``npm test`` directly into the console.  What did you get?  
In replit, the ``F`` on **line 6** will be red to better stand out.  

.. sourcecode:: bash
   :linenos:

   > working-within-tests@1.0.0 test /home/runner/Working-Within-Tests-Demo
   > jasmine

   Randomized with seed 04579
   Started
   F

   Failures:
   1) Test Example Solution outputs the correct message
   Message:
      Expected 'Hello, Coder!' to be 'Hello, World!'.
   Stack:
      Error: Expected 'Hello, Coder!' to be 'Hello, World!'.
         at <Jasmine>
         at UserContext.<anonymous> (/home/runner/Working-Within-Tests-Demo/spec/hello.spec.js:10:19)
         at <Jasmine>

   1 spec, 1 failure
   Finished in 0.01 seconds
   Randomized with seed 04579 (jasmine --random=true --seed=04579)
   npm ERR! Test failed.  See above for more details.

This is great!  Output like this can help you troubleshoot any potential code breakage or deviation.  
The message tells us exactly what needes to be changed.  Change the string back to ``Hello, World!`` and run the tests again.

Congrats! You passed! 

Why Tests?
----------

For now, you just need to know that tests are written to see if the code meets the requirements of the instructions. 
We will be covering more on how we know what to test in a later chapter. 
At this moment in your learning, testing focuses on elements covered in each lesson.  
If you recently learned about loops, you can expect a test about a loop. 
Testing can provide you with specific feedback about your code that you can use to improve your code. 

TL;DR
-----

Some of the projects and starter codebases you will work on within this class contain unit tests. 
The number of tests and testing code will vary by project.  
Read through the code and the instructions before changing anything. 
Your TAs will use the tests to return feedback to you more quickly. 
You can run the tests too, by typing ``npm test`` directly into the console and changing your code as needed.

Happy coding!