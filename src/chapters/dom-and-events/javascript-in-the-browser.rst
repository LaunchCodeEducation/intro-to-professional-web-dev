JavaScript and the Browser
==========================

.. index:: ! static, ! dynamic,

Taking JavaScript on the Web
----------------------------

So far, we have created web pages with HTML and CSS. These pages have been **static**, meaning that the page appears the same each time it loads. 
However, many web pages are actually **dynamic**, meaning that the web page can appear different each time it loads.

.. admonition:: Example 

   A bank's website is dynamic. Each account holder sees a different home page based on how many accounts they have and how much money they have in those accounts.
   When the web page loads for the user, the information about their accounts is sent from the server to the browser for rendering.

JavaScript can be used in the browser to make an HTML page dynamic. 

We have been running all of our JavaScript homework in Node.js, but now it is time to use JavaScript in the browser to make dynamic web pages.
Node is an intepreter for JavaScript with access to lots of different JavaScript libraries. 
When running JavaScript in the browser, each browser has an engine for running it and it remains client-side. 
Firefox uses an engine called Spider Monkey to run client-side JavaScript in the browser. 

The ``<script>`` Tag
--------------------
In the HTML chapter we learned that an HTML page is made up of elements that are written as tags. Those
elements have different purposes. The ``script`` element's purpose is to include JavaScript into the
web page. A ``<script>`` tag can contain JavaScript code inside of it or reference an external JavaScript file.

JavaScript Console
^^^^^^^^^^^^^^^^^^
Using the Developer Tools, you can access a JavaScript console. There you can mess around with fun JavaScript statements or you can use it to see the outputs of the client-side JavaScript you have written.

Inline JavaScript
^^^^^^^^^^^^^^^^^
.. admonition:: Example

   Notice the ``<script>`` tag below contains JavaScript code that will be executed by the browser.

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
            <title>Embedded JavaScript Example</title>
            <script>
               // JavaScript code goes here!
               console.log("Hello from inside the web page");
            </script>
      </head>
      <body>
            contents
      </body>
      </html>

   **Output**

   screen shot of firefox console? Codio? Repl.it?

External JavaScript
^^^^^^^^^^^^^^^^^^^

However, some programmers have large amounts of JavaScript to add to an HTML document.
Using an external JavaScript file can help in these cases.
You can still use the ``<script>`` tag to connect the two while using the ``src`` attribute for the path to the JavaScript file.

.. admonition:: Example

   This is how the HTML file for the web page might look if we wanted to link an external JavaScript file.

   .. sourcecode:: html

      <!DOCTYPE html>
         <html>
         <head>
            <title>External JavaScript Example</title>
            <script src = "myjs.js"></script>
         </head>
         <body>
            <!-- content -->
         </body>
         </html>

   Then the JavaScript file, ``myjs.js`` might look something like this.

   .. sourcecode:: js

      // JavaScript code goes here!
      console.log("Hello from inside the web page");


Also used to reference JavaScript files that are hosted on external servers.
Some of the external will be files that you did not write yourself, but you want to include in your web site.


