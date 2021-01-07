How the Internet Works
======================

Most people use the Internet without fully understanding how it works. Without much trouble, they can open a browser, navigate to a site, and interact with it. They do not need to know precisely *how* the Internet works in order to use it.

For web developers, however, fundamental understanding of the flow of information across the Internet is essential.

Servers and Clients
-------------------

.. index:: ! client-server model, ! client, ! server

The Internet uses the **client-server model**. A **server** is an application that provides resources---such as raw data, web pages, or images. A **client** is an application that requests resources from a server.

When navigating the web, the client is the web browser on your computer or smartphone. When you click on a link or type in an address and hit *Enter*, the client/browser makes a request to a server that sits in a building somewhere out in the world. The server receives the request, and sends a response back to the client. The client then displays the content of the response.

.. figure:: figures/client-server.png
   :alt: A server surrounded by several client computers, connected by arrows.
   :height: 400px

   Several clients communicating with a server.

.. admonition:: Fun Fact

   In the client-server model, the server may sometimes be on the *same* computer as the client. This is often the case when a programmer is building a web application. The in-progress, development version of the application is on their laptop, as is their browser that they use to test the app.

Protocols
---------

.. index::
   single: url; protocol

A **protocol** is a standard for communication between computers. Most web communication uses *three* protocols, in fact.

.. list-table:: Common Web Protocols
   :header-rows: 1

   * - Protocol
     - Full Name
     - Role
   * - HTTP
     - Hypertext Transfer Protocol
     - High-level web communication for transferring files and information, including:

       - HTML, CSS, and JavaScript files
       - images and other media
       - form submissions

   * - TCP/IP
     - Transmission Control Protocol / Internet Protocol
     - Low-level web communication for transferring small chunks of raw data known as *packets*
   * - DNS
     - Domain Name Service
     - Translates human-friendly names into server addresses

A thorough understanding of each of these protocols is well beyond the scope of this class. However, as a web developer it is important you have a general understanding of their roles. Each protocol has a different and critical job in enabling web communication.

HTTP
^^^^

.. index:: ! HTTP, ! HTTPS

**HTTP** is the most important protocol for web developers to understand, which you may have guessed from the title of this chapter. It specifies how requests for common web data---such as HTML files or images---should be structured, as well as responses to such requests. The details of request and response message structure are the topic of the rest of this chapter. 

**HTTPS** refers to the HTTP protocol used with a secure connection. A secure connection encrypts so that it can't be read while in-transit. The data is encrypted by the server/client before being transmitted, and decrypted once it is received by the client/server. The precise details of how such encryption works is beyond the scope of this course. 

TCP/IP
^^^^^^

.. index:: ! TCP/IP

**TCP/IP** is a low-level protocol that is quite complicated. For our purposes, it is important only to know that TCP/IP is the standard that allows *raw data* to get from one place to another on the Internet. 

When a server sends a file back to a client, that file must physically be sent across a series of network components, including cables, routers, and switches. Files are broken down into *packets*---small chunks of a standard size---that are individually sent from one location to the next, until arriving at their final destination and being reassembled.

.. admonition:: Fun Fact

   You can think of the Internet as a `"series of tubes." <https://www.youtube.com/watch?time_continue=15&v=_cZC67wXUTs>`_ This phrase was used by a U.S. Senator in 2006 and widely mocked. However, we think it's actually a reasonable analogy. TCP/IP allows data to be passed from one tube to another until reaching the final destination.

DNS
^^^

.. index:: ! DNS, ! IP address

**DNS** is the address book of the Internet. It enables us to use readable and memorable names for servers, such as ``www.launchcode.org`` or ``mail.google.com``. Such names are called **domain names**, and they function as aliases for the actual server addresses.

Every server on the internet has a numerical address known as an **IP address**. When a message is addressed using a domain name, the corresponding IP address must be determined before it can be sent. 

.. admonition:: Example

   The IP addresses of ``www.launchcode.org`` and ``mail.google.com`` are ``104.25.127.113`` and ``172.217.5.229``, respectively.

The sending computer will attempt to *resolve* the domain name by looking it up on a nameserver. A **nameserver** is a directory of domains and IP addresses, and there are thousands of them on the Internet. Most internet service providers (such as Charter or AT&T) provide DNS servers for their customers to use. Once the sending computer knows the IP address, it can send the request to the correct server.

.. admonition:: Try It!

   It's easy to look up the IP address of any domain name using freely-available tools. 

   Use the popular site `MX Toolbox <https://mxtoolbox.com/DNSLookup.aspx>`_ to look up the IP address of ``help.launchcode.org``. Does this site live on the same server as ``launchcode.org``?

.. admonition:: Fun Fact

   Every computer uses the special IP address ``127.0.0.1`` to refer to *itself*. This is known as the **loopback address**, and it often has the alias ``localhost``. If you use the loopback address when making a request, the request will be sent to a service on the *same* machine as the client.

Web Addresses
-------------

.. index:: ! URL, ! web address

When a client requests a resource from a server, it does so using a **uniform resource locator (URL)**. URLs are also called **web addresses**.

.. admonition:: Examples

   As a regular user of the Internet, you are already familiar with URLs like these:

   - ``https://www.launchcode.org``
   - ``https://en.wikipedia.org/wiki/Client–server_model``
   - ``https://duckduckgo.com/?q=javascript``

A URL encodes a lot of information about the request, including *what* is being requested and *where* the request should be sent. URLs are made up of several components, each of which plays a role in enabling both client and server to understand what is being requested.

We will generally work with URLs with this structure:

::

   scheme://host:port/path?query_string

The five components of this URL are:

- Scheme
- Host
- Port (optional)
- Path (optional)
- Query String (optional)

A properly-formed URL must have these components in the *exact* order shown here. Only scheme and host are required.

Let's look at each of these in detail.

Scheme
^^^^^^^^

.. index::
   single: url; scheme

The first portion of every URL specifies the **scheme**. Common schemes are ``http``, ``https``, ``ftp``, ``mailto``, and ``file``. Most often, the scheme specifies the *protocol* to be used in making a request. For us, this will always be ``http`` or ``https``. If left off, a web browser will insert the scheme http/s for you. 

The scheme is *always* followed by ``://``.

Host
^^^^^^

.. index::
   single: url; domain

The **host** portion of a URL specifies *where* the request should be sent. The host can be either an IP address, like ``104.25.128.113``, or a domain name, like ``www.launchcode.org``.

Port
^^^^

.. index::
   single: url; port

Following the host is an optional **port** number. While the host determines the *server* that the request should be sent to, the port determines the specific *application* on the server that should handle the request. This is important because a single server may run several applications capable of handling requests.

Conventionally, a given type of application will always use the same port, though this is not a hard rule. For example, web servers typically use port 80 or 443, for regular and encrypted messages, respectively. On the other hand, MySQL databases typically use port 3306.

.. admonition:: Example

   Suppose a server at ``mydomain.com`` is running both a web server and MySQL database server on the standard ports. Requests to ``mydomain.com:80`` will be given to the web server, while requests to ``mydomain:3306`` will be given to the database server.

If a port number is not specified, then a default value based on the scheme is used. When using ``http://`` the default port is 80. When using ``https://`` the default port is 443.

Path
^^^^

.. index::
   single: url; path

Following the domain and optional port is the **path**, which consists of a series of names separated by ``/``. The path provides information that tells the server *what* is being requested. It can consist of a series of names, such as ``/blog/entries/2018/``, or it can end with an explicit file name, such as ``/blog/index.html``.

.. admonition:: Example

   A request to ``https://www.launchcode.org/blog/`` asks for the resource that lives at the path ``/blog/`` on the server ``www.launchcode.org``. This resource happens to be the homepage of the LaunchCode blog.

   A request to the (very long) URL below asks for the LaunchCode logo, which lives at the path ``/assets/dabomb-2080d6e...57f.svg`` (truncated here for space).

   ::

      https://www.launchcode.org/assets/dabomb-2080d6e23ef41463553f203daaa15991fd4c812676d0b098243b4941fcf4b57f.svg

If a path is not specified, then the **root path** ``/`` is used. The root path typically refers to the home page for a given site.

Query String
^^^^^^^^^^^^

.. index::
   single: url; query string

Following the path is an optional **query string**, which begins with ``?`` and contains a set of key-value pairs. Each pair is joined by ``=`` and is separated from the other pairs by ``&``. For example, the query string of a `search on duckduckgo.com <https://duckduckgo.com/?q=launchcode&atb=v167-5__&ia=web>`_ looks like this:

::

   ?q=launchcode&atb=v167-5__&ia=web

This query string has *three* key-value pairs:

- ``q`` : ``launchcode``
- ``atb`` : ``v167-5__``
- ``ia`` : ``web``

Notice that these pairs are separated by ``&`` in the query string.

While the path specifies *what* the request is asking for, the query string provides additional data that may be needed to fulfill the request. As an analogy, you can think of the path like a function name, and the query string as the function arguments.

Putting It All Together
-----------------------

We just covered a *lot* of information! While these nuts-and-bolts details are important, they aren't nearly as important as the high-level picture of how we access resources on the internet.

To tie these ideas together, watch these two videos on URLs and the Internet as a whole:

- `How Do URLs Work? <https://www.youtube.com/watch?v=OvF_pnJ6zrY>`_
- `How the Internet Works <https://www.youtube.com/watch?v=7_LPdttKXPc>`_


Check Your Understanding
------------------------

.. admonition:: Question

   Which protocol is responsible for turning a name like ``launchcode.org`` into a server address?

.. admonition:: Question

   Why is this URL malformed?

   ::

      https://launchcode.org?city=miami/lc101

   #. It uses HTTPS when it should use HTTP.
   #. It doesn't contain a fragment.
   #. It doesn't contain a port.
   #. The query string comes before the path.


