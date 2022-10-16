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

### Mark a Task as Complete

The tasks that are now completed can be marked as such by entering the unique number (to find this, they can use the view full list functionality). Then the status is marked as "Complete".

![Image of the console when completing a task](/assets/images/completetask.png)

### View the Full Listing

The view full listing function displays the full list of tasks which are both incomplete and complete, here is where the user finds the information to delete and complete functions.

![Image of the full to-do list output](/assets/images/fullview.png)

### View a Summary Listing

Two summary tables of incomplete tasks are displayed:
- overdue tasks; and
- the three tasks that follow by date.

If there are no pending tasks, a message will be displayed that they are not upcomming tasks.
The first table will only display tasks that are over due, if there are no tasks that are overdue the applications displays a message to show that there are not overdue tasks.
The second table will only show the next three upcoming incomplete tasks, if there are less than three tasks the second table will only show the upcoming incomplete tasks.

![Image of the summary to-do list output](/assets/images/summaryview.png)

## Data Model

Google Sheets was used to create the Data Model to create this application. This Google Sheets is linked to the application and hold all the information to the To-Do-List.

Gspread API was used in order to amend and manipulate data in the spreadsheet.[gspread API](https://docs.gspread.org/en/latest/#).

The integrity of the data is mantained by refusing access of the Google Sheet to the user.

![Image of the underlying Google Sheets document](/assets/images/googlesheet.jpg)

## Testing

### Manual Testing

- Manual use cases have been run to test the functionality of the application.
- The table below shows the user stories, the associated use cases, the task script followed for the test, and whether this passed or failed.

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 1:** I want to review upcoming task as well as tasks completed. | PASS |
| + > **Use Case 1-1:** I want to view both completed and incompleted tasks. | PASS |
| + + + > **Task 1:** Open the Heroku App -> the prompt "Would you like to view or amend the list?" should be displayed -> type in "View" and press Enter -> the prompt "Which view would you like?" should be displayed -> type "Full" and press Enter -> the full list will display | PASS |
| + > **Use Case 1-2:** I want to be able to prioritise tasks using a summary. | PASS |
| + + + > **Task 1:** Open the Heroku App -> the prompt "Would you like to view or amend the list?" should be displayed -> type in "View" and press Enter -> the prompt "Which view would you like?" should be displayed -> type "Summary" and press Enter -> a list of overdue tasks, and a list of the next three due tasks (by date) will display. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 2:** I want to add and delete tasks from the list. | PASS |
| + > **Use Case 2-1:** I want to be able to add a new task to the list. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Add" and press Enter -> input a task name -> input a deadline date -> if successful, the application will display: "This task has been added as item number X" where "X" is the next number along -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the new task has been added to this list at the end. | PASS |
| + > **Use Case 2-2:** A unique number must be assigned to a new task. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Add" and press Enter -> input a task name -> input a deadline date -> if successful, the application will display: "This task has been added as item number X" where "X" is the next number along -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the new task has a unique number compared to the previously existing tasks. | PASS |
| + > **Use Case 2-3:** Tasks that are no longer apply should be deleted. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Delete" and press Enter -> select a task number (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been deleted!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task is no longer on the list. | PASS |

| User Story -> Use Cases -> Tasks | Pass/Fail |
| --- | --- |
| **User Story 3:** Any existing tasks should be easily modified. | PASS |
| + > **Use Case 3-1:** A task should be mark as complete. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Complete" and press Enter -> select a task number that is status "Incomplete" (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been set to Complete!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task has a "Complete" status. | PASS |
| + + + > **Task 2:** Open the Heroku App -> type in "Amend" and press Enter -> type "Complete" and press Enter -> select a task number that is status "Complete" (obtained from the "View" function first if required) -> if successful, the application will display: "Task number X has been set to Complete!" where "X" is the task number selected -> type in "View" and press Enter -> type "Full" and press Enter -> the full list will display -> verify that the selected task continues to have a "Complete" status. | PASS |
| + > **Use Case 3-2:** The name of the task and deadline date for the task should be easily modified. | PASS |
| + + + > **Task 1:** Open the Heroku App -> type in "Amend" and press Enter -> type "Change" and press Enter -> select a task number (obtained from the "View" function first if required) -> the application will display: "Type the updated task name" -> type in an updated task name and press Enter -> the application will display: "What is the revised deadline for this updated task?" -> type in an updated deadline date and press Enter -> if successful, the application will display: "Task number X has been updated!" where "X" is the task number selected -> type "Full" and press Enter -> the full list will display -> verify that the selected task has the updated name and date. | PASS |

### "Negative Testing"

To determine if the application was able to withstand any unexpected inputs from the user the following negative testing was performed:

- Combinations of upper and lower case letters were tested for the selector inputs "view", "amend", "full", "summary", "add", "delete", "complete", and "change" as they appear in the flow of the application. All tested combinations of upper and lower cases (e.g. "View", "VIEW", "view") provided the correct outcome with the application flow continuing as expected.
- The application clearly displayed an error message when the input selectors were different from those required. The user was then prompted to correct their input to a specified input selector.
- Tested inputting a task number that does not exist during the "delete", "complete" and "change" functionality. This resulted in the application stating that the task number did not exist, then repeating the request to input a task number. Therefore, a user cannot perform task list amends for a task that does not exist.
- An invalid task number was entered when using the "delete", "complete" and "change" function which returned a message that the task number did not exist. 
- The application requests a valid date in the correct format (DD/MM/YYYY) when using the "add" or "change" functions. The application then will repeat input request.

### Bugs

#### Fixed Bugs

- As Tasks with long names could not be displayed in the console output. The validation function was been added. To ensure correct viewing output the task names are shorter than 20 caracters long.
- While using the delete task function you could entered a task that did not exist and the application did not return an error message. By including a validation function only existing task numbers can be deleted.
- Summary tables would not run as designed when fewer than three overdue or upcoming tasks were specified. The tables run an show desired output after the addition of "if statement" codes.

### Code Validator Testing

PEP8 is currently not working:
- As a workaround, you can add a PEP8 validator to your Gitpod Workspace directly by following these steps:
- Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
- In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
- Type the word "linter" into the search bar that appears, and click on "Python: Select Linter" from the filtered results.
- Select "pycodestyle" from the list
- PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.
