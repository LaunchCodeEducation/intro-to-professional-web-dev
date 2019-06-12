What are Modules?
==================

Just like functions should be kept small and accomplish only one thing, we want
to apply the same idea for the different parts of our program. **Modules**
allow us to keep the features of our program in separate, smaller pieces. We
code these smaller chunks and then connect the modules together to create the
big project.

Modules are like Legos. Each piece has its own distinct shape and function, and
the same set of pieces can be combined in lots of different ways to create
unique results.

One Possible Scenario
----------------------

Imagine we want to create a program that quizzes students on their JavaScript
skills.

What would go into this app? Features could include:

#. Selecting questions from a stored array or object.
#. Presenting the questions to the students and collecting their answers.
#. Scoring the quizzes.
#. Storing the results.

This would be a useful app, but we could make it better by adding some
other features. Instead of just quizzing students, maybe we could add some
tutorial pages. Our app now provides some teaching and assessment content.

Next, how about adding some non-graded practice to make sure the students are
ready for their final quiz? Once we accomplish that, we could continue adding
to our app to make it better and better.

Let's pause a moment to consider what happened to the size of our project. As
the program evolved from the straightforward quiz app to one that included
tutorials and practice tasks, the number of lines of code increased. Now
imagine we replicate all of these features for two or three other programming
languages.

We can picture our app as follows:

   TODO: Add image.

The result is a mammoth program that contains thousands of lines of code. How
would this impact debugging? How about keeping the code DRY? Do any of the
features overlap? How easy is it to add new features?\

Why Use Modules
----------------

Modules help us keep our project organized. If we find a bug in the quiz part
of our program, then we can focus our attention on the quiz module rather than
the entire collection of code.

Modules also save us effort in other projects - another example of the DRY
concept. We have already practiced condensing repetitive tasks into loops or
functions. Similarly, if we design our quiz module in a generic way, then we
can use that same module in other programs.

Even better, we can SHARE our modules with other programmers and use someone
else's work (with permission) to enhance our own. Writing the imaginary
quiz/tutorial/practice app from scratch would take us many, many weeks.
However, someone in the coding community might already have modules that we can
immediately incorporate into our own project---saving us time and effort.

   Modules keep us from reinventing the wheel.

Some modules also provide us with useful shortcuts.
:ref:`readline-sync <readline-sync>` allowed us to collect input from a user,
and this module contains lots of other methods besides the ``.question`` we
used in our examples. Rather than making every developer write their own code
for interacting with the user through the console, ``readline-sync`` makes the
process easier for all by providing a set of ready-to-use functions. We do not
need to worry about HOW the module works. We just need to be able to pull it
into our projects and use its functions.
