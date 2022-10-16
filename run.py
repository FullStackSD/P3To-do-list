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


ascii_banner = pyfiglet.figlet_format("To Do List")
print(ascii_banner)
print("Welcome to your To Do List!")
print("Please click 'Run Program' above to restart at any time.")
main()