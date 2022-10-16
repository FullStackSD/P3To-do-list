from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import pyfiglet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')


function_options = {
    "type": ["view", "amend"],
    "view": ["full", "summary"],
    "amend": ["add", "delete", "complete", "change"]
}


def select_function():
    """
    Asks the user which function they want to use
    Between amending the list and viewing the list
    """
    while True:
        print("\nWould you like to view or amend the list?")

        function_response = input("Type 'View' or 'Amend' here: \n")
        if validate_input(function_response, "type"):
            break

    if function_response.lower() == 'view':
        select_view_function()
    else:
        select_amend_function()


def select_view_function():
    """
    If the user has selected 'View' from the first question
    This function allows the user to select which type of view they would like
    """
    while True:
        print("Which view would you like?")

        view_response = input("Type 'Full' or 'Summary' here: \n")
        if validate_input(view_response, "view"):
            break

    if view_response.lower() == 'full':
        view_full()
    else:
        view_summary()        
        

def select_amend_function():
    """
    If the user has selected amend in the first question
    This function allows the user to select which type of amendment they want
    """
    while True:
        print("What amendment would you like?")

        amend_message = "Type 'Add', 'Delete', 'Complete' or 'Change' here:"
        amend_response = input(f"{amend_message}\n")
        if validate_input(amend_response, "amend"):
            break

    if amend_response.lower() == 'add':
        add_task()
    elif amend_response.lower() == 'delete':
        delete_task()
    elif amend_response.lower() == 'complete':
        complete_task()
    else:
        change_task()


def validate_input(response, option):
    """
    Checks that the user has input a valid response
    The valid responses are per the function_options dictionary
    Allows the user to input either upper or lower case
    """
    functions = function_options.get(option)
    if response.lower() in functions:
        return True
    else:
        print("\nResponse is not valid!")
        return False


def view_full():
    """
    Formats and displays the full to-do list
    Uses PrettyTable to format the table
    """
    data = SHEET.worksheet('to_do').get_all_values()
    full_list = PrettyTable()
    full_list.field_names = data[0]
    for i in range(len(data)-1):
        full_list.add_row(data[i+1])
    print(full_list)


def view_summary():
    """
    Formats and displays a summary of the list
    First table is all overdue tasks
    Second table is the next three upcoming tasks
    """
    data = SHEET.worksheet('to_do').get_all_values()
    completion_list = SHEET.worksheet('to_do').col_values(4)
    today = datetime.today()
    incomplete_list = []
    for count, item in enumerate(completion_list):
        if item == 'Incomplete':
            incomplete_list.append(data[count])

    overdue_list = []
    for count, item in enumerate(incomplete_list):
        if datetime.strptime(item[2], '%d/%m/%Y') < today:
            overdue_list.append(item)

    count_overdue = len(overdue_list)
    overdue_table = PrettyTable()
    overdue_table.field_names = data[0]

    if count_overdue == 0:
        overdue_table.add_row(["", "You have no overdue tasks", "", ""])
    else:
        for count, item in enumerate(overdue_list):
            overdue_table.add_row(item)

    print("\nHere are all of the overdue tasks:")
    print(overdue_table)

    upcoming_list = []
    for count, item in enumerate(incomplete_list):
        if datetime.strptime(item[2], '%d/%m/%Y') >= today:
            upcoming_list.append(item)

    upcoming_list.sort(key=lambda x: datetime.strptime(x[2], '%d/%m/%Y'))
    count_upcoming = len(upcoming_list)

    upcoming_table = PrettyTable()
    upcoming_table.field_names = data[0]

    if count_upcoming == 0:
        upcoming_table.add_row(["", "You have no upcoming tasks", "", ""])

    if count_upcoming > 0:
        upcoming_table.add_row(upcoming_list[0])
        if count_upcoming > 1:
            upcoming_table.add_row(upcoming_list[1])
            if count_upcoming > 2:
                upcoming_table.add_row(upcoming_list[2])

    print("\nHere are the next three upcoming tasks:")
    print(upcoming_table)


class Task:
    """
    Class to hold the information needed for each task
    Follows the same format as the underlying Google Sheet
    """
    def __init__(self, number, name, date, status):
        self.number = number
        self.name = name
        self.date = date
        self.status = status

    def to_list(self):
        """
        Method returns the task in list format
        The list format is needed for the add_task function
        """
        return [self.number, self.name, self.date, self.status]


def add_task():
    """
    Requests the user to input a new task
    Adds the task to the google sheet list at the end
    """
    while True:
        new_task_name = input("Type the name of the task here: \n")
        if validate_add_task_name(new_task_name):
            break

    while True:
        print("What is the deadline for this new task?")
        new_date = input("Use the format DD/MM/YYYY?: \n")
        if validate_add_task_date(new_date):
            break

    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    task_numbers.remove('Number')
    task_numbers_int = list(map(int, task_numbers))
    new_index = max(task_numbers_int, default=0) + 1

    task = Task(new_index, new_task_name, new_date, 'Incomplete')

    list_worksheet = SHEET.worksheet('to_do')
    list_worksheet.append_row(task.to_list())

    print(f"This task has been added as item number {new_index}.")


def validate_add_task_name(name):
    """
    Checks if the new task name is within 20 characters
    This ensures that the task will be able to be viewed in the console
    If over 20 characters, an error message is provided
    """
    if len(name) <= 20:
        return True
    else:
        print("The task name must be 20 character max.")
        return False


def validate_add_task_date(input_date):
    """
    Validates that the date input by the user is in the correct format
    Will provide an error message if incorrect and request the date again
    """
    try:
        datetime.strptime(input_date, '%d/%m/%Y')
        return True
    except ValueError:
        print("\nEnsure the date is valid and in the format DD/MM/YYYY.")
        return False


def delete_task():
    """
    Requests the user input a task number from the full table list
    Deletes the task from the google sheet
    """
    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    while True:
        task_selection = input("Which task number would you like to delete?\n")
        if validate_task_number(task_selection):
            break

    task_position = int(task_numbers.index(task_selection))
    list_worksheet.delete_rows(task_position + 1)
    print(f"Task number {task_selection} has been deleted!")


def complete_task():
    """
    Requests the user input a task number from the full table list
    Sets the task status to Complete
    """
    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    while True:
        task_selection = input("Which task number is complete? \n")
        if validate_task_number(task_selection):
            break

    task_position = int(task_numbers.index(task_selection))
    list_worksheet.update_cell(task_position + 1, 4, 'Complete')
    print(f"Task number {task_selection} has been set to Complete!")


def change_task():
    """
    Requests the user to input a task number from the full table list to change
    Asks for an updated name and deadline date
    """
    list_worksheet = SHEET.worksheet('to_do')
    task_numbers = list_worksheet.col_values(1)
    while True:
        task_selection = input("Which task number would you like to change?\n")
        if validate_task_number(task_selection):
            break

    task_position = int(task_numbers.index(task_selection))

    while True:
        update_name = input("Type the updated task name: \n")
        if validate_add_task_name(update_name):
            break

    while True:
        print("What is the revised deadline for this updated task?")
        update_date = input("Use the format DD/MM/YYYY?: \n")
        if validate_add_task_date(update_date):
            break
    list_worksheet.update_cell(task_position + 1, 2, update_name)
    list_worksheet.update_cell(task_position + 1, 3, update_date)
    print(f"Task number {task_selection} has been updated!")


ascii_banner = pyfiglet.figlet_format("To Do List")
print(ascii_banner)
print("Welcome to your To Do List!")
print("Please click 'Run Program' above to restart at any time.")
main()