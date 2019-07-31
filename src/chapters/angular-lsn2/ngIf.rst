``ngIf``
=========

The ``*ngIf`` structural directive evaluates a boolean expression and then
adds or removes elements from the DOM based on the result.

The examples below show the basic usage of ``*ngIf``. If you want to explore
more details about this directive, refer to the following resources:

#. `Angular documentation <https://angular.io/guide/template-syntax#ngif>`__.,
#. `Malcoded website <https://malcoded.com/posts/angular-ngif-else/>`__.

``*ngIf`` Syntax
-----------------

In general, the syntax for ``*ngIf`` is:

::

   *ngIf = "condition"

``*ngIf`` statements are added inside an HTML tag. The ``condition`` can either
be a boolean or an expression that returns a boolean. If ``condition``
evaluates to ``true``, then the HTML tag is added to the webpage, and the
content gets displayed. If ``condition`` returns ``false``, then the HTML tag
is NOT generated, and the content stays off the webpage.

.. admonition:: Note

   ``*ngIf`` determines if content is displayed or REMOVED from a page. This is
   different from determining if content should be displayed or HIDDEN.

   *Hidden* content still occupies space on a page and requires some amount of
   memory. *Removed* content is absent from the page---requiring neither space
   on the page nor memory. This is an important consideration when adding
   images or videos to your website.

.. admonition:: Example

   Let's modify our movie list code as follows:

   .. sourcecode:: html+ng2
      :linenos:

      <div class='movies' *ngIf = "movies.length > 3">
         <h3>Movies to Watch</h3>
         <ol>
            <li *ngFor = "let movie of movies">{{movie}}</li>
         </ol>
      </div>

Adding the ``*ngIf`` statement inside the ``<div>`` tag determines whether
that element and any content it contains gets added to the webpage. If the
condition ``movies.length > 3`` evaluates to ``true``, then the ``div``,
``h3``, ``ol``, and ``li`` tags all get generated. If the condition returns
``false``, then none of the tags are added to the HTML code.

Logical Operators With ``*ngIf``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just like ``if`` statements, we can use the operators AND (``&&``), OR
(``||``), and NOT (``!``) to modify the condition checked by ``*ngIf``.

.. admonition:: Examples

   Logical AND:

   .. sourcecode:: html+ng2

      <p *ngIf = "conditionA && conditionB">Some text</p>

   ``Some text`` appears on the webpage only if ``conditionA`` and
   ``conditionB`` both return ``true``.

   Logical OR:

   .. sourcecode:: html+ng2

      <p *ngIf = "conditionA || conditionB">Some text</p>

   ``Some text`` appears on the page if either ``conditionA`` or ``conditionB``
   return ``true``.

   Logical NOT:

   .. sourcecode:: html+ng2

      <p *ngIf = "!arrayName.length == 0">Some text</p>

   ``Some text`` appears when ``arrayName.length == 0`` returns ``false``,
   since the ``!`` operator flips the result. If the array is empty, then
   nothing gets added to the webpage.

   Note that the Angular syntax uses ``==`` rather than the ``===`` we prefer
   in JavaScript.
