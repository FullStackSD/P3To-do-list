# To Do App

This "To Do List" App is a console web application which runs using the Code Institute mock terminal on Heroku.

It is an interface design with simplicity in order to provide the user with a place to keep track of their tasks.

[Live version of the application.](https://to-do-list-shaz.herokuapp.com/)

![Images to demostrate the responsiveness of the web application](/assets/images/responsive.png)


## Features

The starting point of the application requires an input from the user where they are asked which function of the application they wish to use. The flowchart below demostrates the various options that can be selected by the user as well as a description of their function. 

![Flowchart of options for the to-do-list application](/assets/images/flowplanner.png)

An error will be shown and the same question will be repeated if the application is uneable to validate a response as suitable. The input from the user may consist of any combination of upper or lower cases letters, therefore ensuring less sencibility with regards to a users response making the use of the app more enjoyable.

### Add a New Task

The name of the task should be added to the input by the user, and given a deadline to be completed by. The task is then added to the list by the application and given a number within that list. Each task corresponds with a unique number, so tasks can be marked as completed or deleted using the functions using the app. A new task can be added an "Incomplete" status will show as default.
The deadline date that has been added by the user must take the form of DD/MM/YYYY for the app to recognise the input.

![Image of the console when adding a task](/assets/images/addtask.png)

### Delete an Existing Task

The unique number that corresponds with the task is entered by the user to the input space provided (to find this, they can use the view full list functionality). The task will then be permantly deleted from the list, and so no longer appears on any of the functionalities.

![Image of the console when deleting a task](/assets/images/deletetask.png)

### Change the Name/Date of an Existing Task

The unique task number that the user wishes to change is entered, the user is then prompted by the application to update the name and also the deadline date. This will overwrite this task.

![Image of the console when changing a task](/assets/images/changetask.png)
