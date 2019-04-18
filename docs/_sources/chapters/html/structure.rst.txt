HTML Structure
==============

.. index:: ! head , ! title , ! html , ! doctype , ! body

HTML files need to be structured in a specific way in order for the content to show up properly on the page. Though some of the rules may seem redundant and unnecessary to programmers, the tags used to lay out the over-arching structure are vital to the browser being able to render the page correctly.

Document Structure Rules
------------------------

1. Every HTML file needs a ``doctype`` tag, specifying that the file is in fact, HTML.
2. The ``<html>`` tag denotes the beginning and end of the HTML the programmer has written. This tag may seem unnecessary if the file only contains HTML, but as you incorporate JavaScript into your HTML, the ``<html>`` tag will become more and more important.
3. The ``<head>`` tag holds everything that goes at the head of the document.
4. The ``<body>`` tag holds everything that appears on the page of the document. 
5. The ``<title>`` tag goes in the ``<head>`` of the document and is required. It gives the title of the webpage.

Document Head
-------------

Every document head needs to include the title of the document. It may also include links to other files.


Document Body
-------------

After the programmer has written the head of the document, it is time to move on to the body of the document. The body of the document contains all of the content that appears on the web page.
Inside the body, programmers can add images, write text, and even add code samples with the plethora of HTML tags available. As always, the body tag needs a corresponding closing tag at the end of the content.

Something else to note is adding whitespace to HTML. While spacing and tabbing over helps many programmers quickly read through theirs and their colleagues' code, it can effect HTML rendering in the browser, though that is a relatively rare instance.
In order to make HTML more readable without risking the page they are developing appearing wonky, programmers frequently write comments in HTML. In order to add a comment, the programmer simply uses ``<!--`` to indicate the start and ``-->`` to end the comment.
