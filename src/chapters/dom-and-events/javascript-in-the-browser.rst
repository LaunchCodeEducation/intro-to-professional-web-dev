JavaScript and the Borwser
==========================

Taking JavaScript on the Web
----------------------------
Differentiate between dynamic and static web pages
Describe how the JavaScript environment of a browser is different from other JavaScript environments, such as Node.js


The ``<script>`` Tag
--------------------
In the HTML chapter we learned that an HTML page is made up of elements that are written as tags. Those
elements have different purposes. The ``<script>`` element's purpose is to include JavaScript into the
web page. A ``<script>`` tag can contain JavaScript code inside of it or reference an external JavaScript file.

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


JavaScript Console
------------------
Something about how to see output in the console.


External JavaScript
-------------------
Keeps HTML and JavaScript separate. Also used to reference JavaScript files that are hosted on external servers.
Some of the external will be files that you did not write yourself, but you want to include in your web site.


