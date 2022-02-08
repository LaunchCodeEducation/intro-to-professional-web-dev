JavaScript and the Browser
==========================

.. index:: ! static, ! dynamic,

Taking JavaScript on the Web
----------------------------

So far, we have created web pages with HTML and CSS. These pages have been **static**, meaning that the page appears the same each time it loads. 
However, you may find that you want to create a web page that changes after it's been loaded. In order to create such a page, you would use JavaScript.
Web pages that can change after loading in the browser are called **dynamic**.
This is useful to programmers and users alike because they can interact with an application without refreshing the page.
Having to constantly refresh the page would be a poor experience for the user and JavaScript helps programmers alleviate this burden.

.. admonition:: Example 

   When you are on a social media page, you may like someone's post.
   When you do like their post, you may notice that several things happen.
   The counter of how many likes the post has received increases by one and the 
   like button may change color to indicate to you that you liked the post.
   This is an example of how JavaScript could be used to create an application 
   that dynamically updates without the page having to be refreshed.

We have been running all of our JavaScript code in Node.js, but now it is time to use JavaScript in the browser to make dynamic web pages. 
Node.js, or just Node, is a JavaScript interpreter with access to lots of different JavaScript libraries. 
Each browser has its own engine for running JavaScript. JavaScript run in the browser is called client-side JavaScript. 
Firefox uses an engine called Spider Monkey to run client-side JavaScript. 
Since each browser uses its engine, each browser may handle HTML, CSS, or JavaScript differently. 
This can lead to discrepancies between browsers.  

.. admonition:: Warning

   The website `Can I Use <https://caniuse.com/>`_ is a great resource to check browser usability of any JavaScript, HTML or CSS.



The ``<script>`` Tag
--------------------
In the HTML chapter, we learned that an HTML page is made up of elements that are written as tags. Those
elements have different purposes. The ``script`` element's purpose is to include JavaScript into the
web page. A ``<script>`` tag can contain JavaScript code inside of it or reference an external JavaScript file.

JavaScript Console
^^^^^^^^^^^^^^^^^^
Using the Developer Tools, you can access a JavaScript console. There, you can mess around with fun JavaScript statements or you can use it to see the outputs of the client-side JavaScript you have written.

Inline JavaScript
^^^^^^^^^^^^^^^^^
.. admonition:: Example

   Notice the ``<script>`` tag below contains JavaScript code that will be executed by the browser.

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
      <head>
            <title>Embedded JavaScript Example</title>
            <script>
               // JavaScript code goes here!
               console.log("Hello from inside the web page!");
            </script>
      </head>
      <body>
            contents
      </body>
      </html>

   **Console Output**

   ::

      Hello from inside the web page!

External JavaScript
^^^^^^^^^^^^^^^^^^^

Some programmers have large amounts of JavaScript to add to an HTML document.
Using an external JavaScript file can help in these cases.
You can still use the ``<script>`` tag to include the JavaScript file within the 
HTML document. In this case, you'll need to use the ``src`` attribute for the path 
to the JavaScript file.

.. admonition:: Example

   This is how the HTML file for the web page might look if we wanted to link an external JavaScript file.

   .. sourcecode:: html
      :linenos:

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
      :linenos:

      // JavaScript code goes here!
      console.log("Hello from inside the web page");


.. note::

   You can use the ``<script>``  tag to reference JavaScript files hosted on external servers.
   Some of these JavaScript files will be files that you have not written yourself but you will want to include in your application.

Check Your Understanding
------------------------

.. admonition:: Question

   What is the difference between dynamic and static web pages?

.. admonition:: Question

   Does Node.js run in the browser environment?


