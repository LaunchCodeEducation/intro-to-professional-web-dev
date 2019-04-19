Naming Functions
================

As with variables, choosing good, descriptive names for the functions you write is important. It makes your code more readable, and therefore more maintainable and more bug-resistent.

Use Camel Case
--------------

As with variables, use camel case. All functions in JavaScript should begin with a lowercase letter, with the first letter of subsequent words capitalized.

.. admonition:: Example

   **Good**

   - ``const astronautCount = 7;``
   - ``const fuelTempCelsius = -225;``
   - ``let isReady = false;``
   

   **Bad**

   - ``const AstronautCount = 7;``
   - ``const fuel_temp_celsius = -225;``
   - ``let is_ready = false;``

Use Verb/Noun Pairs When Applicable
-----------------------------------

A function carries out an action, and it often produces some specific output or effect. Therefore, using a verb/noun pairs can go a long way toward making it clear what a functions does. A good verb can describe the action, and a good noun can describe the output, or the object that is being affected by the function.

.. admonition:: Example

   **Good**

   - ``prepareForLiftoff``
   - ``fillFuelTank``
   - ``getCoundownStatus``
   - ``isReadyForLiftoff``

   **Bad**

   - ``liftoff``
   - ``fillup``
   - ``countdownStatus``
   - ``isReady``

As we noted earlier, for boolean functions it is conventional that their names start with "is" or "has" whenever possible. 

Creating a verb/noun pair for a function name doesn't always make sense, but when it does, you should use this format to create a good, descriptive name.

Use Descriptive Names
---------------------

We've said it before that you should use descriptive names, but now we want to expand on the point a bit. You should *prefer long, descriptive names over short, abbreviated names*. If you can read a function name and understand what it does from that along, that is ideal.

.. admonition:: Example

   **Good**

   - ``convertCelsuisToFahrenheit``
   - ``isValidLaunchCode``
   - ``updateMissionControl``
   

   **Bad**

   - ``convertC``
   - ``validCode``
   - ``msgToMC``

.. _comments_lie:

If you find yourself writing a comment to describe what your function does, consider whether a better name might remove the need for such additional explanation. The best function (and variable) names are those that are *self-documenting*. In other words, they are descriptive enough as to not need explanatory comments. 

Using self-documenting names means that the code that *uses* your function will be more readable---your explanatory comments are not visible where the function is used. Additionally, it is easy for comments to become inaccurate; when you update your code to change behavior, there is nothing forcing you to also update your comments. For this reason, some programmers live by the maxim, "Comments lie." While we won't go so far as to say that you should never use comments in your code, we *do* believe that comments should not be used to make up for poor function and variable names.
