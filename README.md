# About this Repository

This repository is a template used by the LaunchCode Education team for creating LaunchCode education sites for LaunchCode classes. 

## Sites that use this template

[Introduction to Professional Web Development in JavaScript](https://education.launchcode.org/intro-to-professional-web-dev/)

[Java Web Development](https://education.launchcode.org/java-web-development/)

[C# Web Development](https://education.launchcode.org/csharp-web-development/)

[Data Analysis](https://education.launchcode.org/data-analysis/)

[Introduction to Programming in C#](https://education.launchcode.org/intro-to-programming-csharp/)

[Structured Query Language](https://education.launchcode.org/SQL/)

## How to Use this Repository

This template is derived from [LaunchCode's Curriculum Module Template](https://github.com/LaunchCodeEducation/curriculum-module-template) and used for original LaunchCode Education content.

### Creating a New Site

When creating a new LaunchCode Education book, here is how you use this template:
#. Cloning this repo into your new site directory.
#. Remove this repo as the origin. If you use the command `git remote -v`, you should now see no remotes.
#. Add this repo as the upstream repository.
Now you are ready to build curriculum!

#### Customize conf.py

Change ``site_theme_options.navbar_title`` and ``project`` to match your curriculum content.

### Working with an Existing Site

When working on an existing site, you want to make sure that you have two remotes to your local repo. Your origin should point to the remote repo and you should add an upstream that points to `curriculum-book-template`.


