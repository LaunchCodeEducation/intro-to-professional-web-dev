How the Internet Works
======================

Most people use the Internet without fully understanding how it works. Without much trouble, they can open a browser, navigate to a site, and interact with it. They do not need to know precisely *how* the Internet works in order to use it.

For web developers, however, fundamental understanding of the flow of information across the Internet is essential.

Servers and Clients
-------------------

.. index:: ! client-server model, ! client, ! server

The Internet uses the **client-server model**. A **server** is an application that provides resources---such as raw data, web pages, or images. A **client** is an application that requests resources from a server.

When navigating the web, the client is the web browser on your computer or smartphone. When you click on a link or type in an address and hit *Enter*, the client/browser makes a request to a server that sits in a building somewhere out in the world. The server receives the request, and sends a response back to the client. The client then displays the content of the response.

.. todo:: insert or create client/server diagram

.. admonition:: Fun Fact

   In the client-server model, the server may sometimes be on the same computer as the client. This is typically the case when a programmer is building a web application. Their development version of the application is on their laptop, as is their browser. 

Web Addresses
-------------

.. index:: ! URL, ! web address

When a client requests a resource from a server, it does so using a **uniform resource locator (URL)**. URLs are also called **web addresses**.

.. admonition:: Examples

   As a regular user of the Internet, you are already familiar with URLs like these:

   - ``https://launchcode.org``
   - ``https://en.wikipedia.org/wiki/Client–server_model``
   - ``https://duckduckgo.com/?q=javascript``

A URL encodes a lot of information about the request, including *what* is being requested and *where* the request should be sent. They are made up of several components, each of which plays a role in enabling both client and server to understand what is being requested.

We will generally work with URLs with this structure:

::

   protocol://domain:port/path?query_string

The five components of this URL are:

- Protocol
- Domain
- Port
- Path
- Query String

Let's look at each of these in detail.

Protocol
^^^^^^^^

Domain
^^^^^^

Port
^^^^

Path
^^^^

Query String
^^^^^^^^^^^^


Protocols
---------

HTTP
^^^^

TCP/IP
^^^^^^

DNS
^^^

Check Your Understanding
------------------------

.. admonition:: Question

   Which protocal is responsible for turning a name like ``launchcode.org`` into a server address?

.. admonition:: Question

   Why is this URL malformed?

   ::

      https://launchcode.org?city=miami/lc101

   #. It uses HTTPS when it should use HTTP.
   #. It doesn't contain a fragment.
   #. It doesn't contain a port.
   #. The query string comes before the path.


