The DOM
=======
.. index:: ! DOM

In JavaScript you can define classes to represent specific entities. An instance of a class is called
an instance. The **Document Object Model (DOM)** is a set of objects that represent the browser, HTML
document, and all the elements on the page. The DOM objects are instances of classes that model the
structure of the browser, HTML document, HTML elements, element attributes, and CSS.

TODO: figure of the DOM as a tree (w3schools has an example of this)

Global DOM Variables
--------------------
.. index::
   pair: variable; global

To utilize the DOM in JavaScript, use the DOM global variables. **Global variables** are variables that are
usable in code without having to declare or import them. We will learn much more about these variables and their types soon,
but fow now let's get used to the idea of using JavaScript to interact with the DOM.

To start we are going to use the ``window`` and ``document`` global variables. The ``window`` represents the browser
window, while ``document`` represents the HTMl document inside of the window.
As mentioned above, we will go into more detail on these later.

.. admonition:: Example

   Here the ``window`` and ``document`` variables are used to print information to the browser's console.

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
            <title>Using DOM Variables</title>
            <script>
               console.log("the page title:", document.title);
               console.log("the protocol:", window.location.protocol);
            </script>
      </head>
      <body>
            contents
      </body>
      </html>

   **Output**

   ::

      the page title: Using DOM Variables
      the protocol: https:


Dynamic Web Page Using the DOM
------------------------------
Sometimes it is necessary to update a web page after the page has been loaded. The DOM plays a key part
in making web pages dynamic. Since the DOM is a code version of the web page, you can write code
to alter the web page. The browser will re-render the web page anytime changes are made via the DOM.

In order to add or edit HTML elements with cod we need to be able to get reference to them. The method
``document.getElementById`` will search for a matching element and return a reference to it. With that
referrence we can call methods on the element to add or edit it. We will go into more detail
on this method and many more in the DOM methods section.

.. admonition:: Example

   Use ``document.getElementById`` and ``element.append`` to add text to a ``<p>`` tag.

   .. sourcecode:: html

      <!DOCTYPE html>
      <html>
      <head>
            <title>Add content using DOM</title>
      </head>
      <body>
            <p id="main-text">Words about things...</p>
            <script>
               let p = document.getElementById("main-text");
               p.append("More words about things");
               console.log(p.innerHTML);
            </script>
      </body>
      </html>

   **Output**

   ::

      Words about things... More words about things

Where to Put the ``<script>``
-----------------------------

In the previous example, notice the ``<script>`` is placed below the ``<p>`` in the HTML document.
That is important because HTML documents are executed top down. A ``<script>`` must come after
any other elements that will be affected by the code inside the ``<script>``. In the Events section
we will learn about another way to handle this.

Check Your Understanding
------------------------

.. admonition:: Question

   What do the DOM objects represent?

   1. Word documents you have downloaded
   2. Directives of memory
   3. The browser window, HTML document, and the elements

.. admonition:: Question

   What is the difference between the document and window variables?

