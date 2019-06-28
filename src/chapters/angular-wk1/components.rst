Components
----------

Angular builds a web page by combining multiple components together. Splitting our page into individual components makes our application more organized, and increases our ability to focus on one section of our web application at a time.

Everything in Angular is built on top of this component concept. So it is crucial to understand the individual pieces of a component, and how to get component to work together.

Component Files
---------------

A component consists of 3 files:
    - an HTML file (.html)
    - a CSS file (.css)
    - a typescript file (.ts)

TODO: picture?

All three of these files will be found in a folder named after the component. All three files will also be named after the component.

As an example, if we create a new component named task-list our three files would be found in the task-list folder and would be called:
    - task-list.html
    - task-list.css
    - task-list.ts

In this example each file of our component will contain only the information necessary for this component. task-list.html will only contain the HTML required for the task-list, task-list.css will only contain the styling information required for this task-list, and task-list.ts will only contain the typescript required by this component.

Adding a Component to the Main Component
----------------------------------------

Each component is it's a part of the entire web application. In important thing to understand is how new components are added to the main component. The main component is the base component that comes standard with all Angular applications. It's the container that holds all of the components, and organizes them into the web application.

Once we have created a new component we will need to make sure it is added to the main component.

When you generate a new component using a tool like Stackblitz, or the Angular CLI it is automatically added to the main component, but let's still look at how is added.

TODO: picture

Code is added in two places:
    - main.html
    - app.module

Component Nesting
-----------------

Components can be put inside of other components. In essence this is how the main component work. It is the component that holds all other components.

However, in some instances you may want to nest a component inside of another component that isn't the main component.

In this case you follow the same steps to nest a component inside of the main component, but for the component that is holding the nested component.

TODO: picture

You also will have to make sure this new component isn't also nested inside of the main component, or you may see the component has been duplicated.
