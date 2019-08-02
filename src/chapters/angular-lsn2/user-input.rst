Responding to User Input
=========================

So far, if we want to change the number of items in our movie and chore lists,
we have to go into the code and alter the arrays. Obviously, it would be better
if we could make the changes on the screen.

Change Practice Folder
-----------------------

From the ``lesson2`` folder in VSCode, open the
``examples/input-practice/src/app/movie-list`` folders and select the
``movie-list.component.html`` file.

The starter code should match this:

.. sourcecode:: html+ng2
   :linenos:

   <div class='movies col-4'>
      <h3>Movies to Watch</h3>
      <ol>
         <li *ngFor ="let movie of movies">{{movie}}</li>
      </ol>
      <hr>

   </div>

In the terminal, navigate into the ``input-practice`` folder and enter
``ng serve``. The webpage should look like this:

.. figure:: ./figures/input-start.png
   :alt: Starting setup for Angular input practice.

Now let's modify the code to accept user input. Be sure to code along with each
step.

Setting Up an Input Box
------------------------

Recall that the :ref:`HTML input tag <input-tag>` creates a box where the user
can enter data. This data is retrieved by referencing the input element's
``value`` property.

#. Add ``<input type='text' placeholder="Enter Movie Title Here"/>`` to line 7,
   then reload the page.

.. figure:: ./figures/inputstep1.png
   :alt: Added an input box.

Typing characters into the box does not do anything yet, since we have not
included any instructions to deal with the data.

2. Angular extends the ``input`` element by declaring a *reference variable*
   and also an *event* that triggers data collection. Modify the input element
   in line 7 by adding ``#newMovie`` inside the tag:

   .. sourcecode:: html+ng2

      <input #newMovie type='text' placeholder="Enter Movie Title Here"/>

#. To store the typed characters into the ``newMovie`` variable, we need to
   wait for a particular event to occur. One of the simplest is to wait for a
   ``keyup``. Modify line 7 one more time:

   .. sourcecode:: html+ng2

      <input #newMovie (keyup)='true' type='text' placeholder="Enter Movie Title Here"/>

``(keyup)='true'`` waits for the user to tap and release a key when the cursor
is in the input box. When this happens, any characters in the box are stored in
``newMovie``. However, we still need a place for the data to *go*.

4. Add one more line to your code, then save and reload the page:

   .. sourcecode:: html+ng2
      :linenos:

      <div class='movies col-4'>
         <h3>Movies to Watch</h3>
         <ol>
            <li *ngFor ="let movie of movies">{{movie}}</li>
         </ol>
         <hr>
         <input #newMovie (keyup)='true' type='text' placeholder="Enter Movie Title Here"/>
         <p>{{newMovie.value}}</p>
      </div>

When the ``keyup`` event is triggered, data gets stored in the ``newMovie``
variable. The ``newMovie.value`` placeholder on line 8 displays that data on
the screen.

.. admonition:: Try It

   Save your work, reload the page, and then play! Type into the input box to
   verify your code works.

   .. figure:: ./figures/input-keyup.png
      :alt: Keyup input practice.

   As you add or remove characters from the input box, you should see a
   real-time update of the text on the screen.

Changing the Event
-------------------

Changing the Movie Array
-------------------------
