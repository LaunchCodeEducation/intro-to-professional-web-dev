Background
==========

.. index:: ! tag, ! element

So far, this book has covered a lot about Javascript and why Javascript is a key language for web developers. However, it has not covered how Javascript can be used in a web application or how the content on a web page appears on screens around the world.
First, a programmer creates the web page using not only Javascript, but also the languages covered in these two chapters: HTML and CSS.
When a user goes to their browser to check out the programmer's web page and click on the URL, two main steps happen:

1. The browser sends a **request** to the server for the web page and the server **responds** with the code that makes up the web page. This can include lots of different languages, but will almost always include HTML and CSS.
2. The browser takes the code and renders it to present the web page that the code creates. 

So how does the browser read this code and turn it into the beautiful web page that the programmer intended it to be?
The short answer to this question can be found by understanding what HTML and CSS is and how to use those languages.

.. admonition:: Note

   There is a lot to how the internet works and in later chapters, this book will go into greater depth into the request and response between servers and the browser.

What is HTML?
-------------

.. index:: ! hypertext, ! markup language

Indicators of how HTML works are in it's name. HTML is short for Hypertext Markup Language.
**Hypertext** is the text that the user sees that includes references to other text known as hyperlinks. Then what is a markup language?

With coding languages, there is a family of languages called **markup languages**. Markup languages are used to annotate the text of a document and define the structure. In the case of HTML, it is the markup language that is defining the structure of hypertext.
Beyond the content that the user will see, HTML has two components for outlining the structure of a web page: elements and tags.

HTML Elements
-------------

An HTML **element** is a type of section of the page. When creating the structure of a web page, many programmers break their pages down into sections based on the type of content that goes into that section.


HTML tags
---------

A HTML **tag** is the code that the computer processes to determine the type and content of an HTML element.

Each tag has the following structural elements:

1. ``<`` to start a tag and ``>`` to close it.
2. The type of tag it is.
3. Any additional information needed about the element that the tag is about.

Just as important as letting the computer know when an HTML element starts is letting it know when the element ends. Closing tags include the same information as the opening tag with a ``\`` before the ``>`` bracket.

Just as there are different ways to write Javascript, there are different ways to write HTML. Semantic HTML helps programmers communicate through code and may be easier to pick up at first.
Semantic HTML is not just about the appearance of the web page, but also the specific meaning. Programmers can make a paragraph larger than a page title, however, by looking at the HTML another programmer can understand which is the paragraph and which is the page title.
Making code work is important and so is making it easier for other programmers to read. Not every piece of a code a programmer has read is something they have written.
Another benefit to semantic HTML is that it is easier for beginning programmers to visualize the end results. Some examples of semantic HTML tags are: ``<p>``, ``<h1>``, ``<h2>`` , and ``<div>``.

Check Your Understanding
------------------------

.. admonition:: Question

   HTML stands for what?

   #. Happy Tickles Make Laughter
   #. Hypertext Markup Language
   #. Hypertext Mockup Language
   #. Hyperlink Markup Layout

