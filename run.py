from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open('to_do_list')
TASKS_WORKSHEET = SPREADSHEET.worksheet('tasks')

APP_HEADING = r'''
___  __      __   __             __  ___
 |  /  \    |  \ /  \    |    | /__`  | 
 |  \__/    |__/ \__/    |___ | .__/  |
'''
HORIZONTAL_LINE = "-" * 80


def retrieve_data(worksheet):
    '''
    Retrieves worksheet data as a list of dictionaries,
    where each dictionary represents a row in the worksheet.

    Returns: list[dict] or list[]
    '''
    return worksheet.get_all_records()


def exclude_inactive_tasks(tasks):
    '''
    Takes worksheet task data: list of task dictionaries,
    and filters out inactive tasks (soft deleted entries).
    
    Returns: list[dict] or list[]
    '''
    active_tasks = []

    for task in tasks:
        if task['active'] == 'TRUE':
            active_tasks.append(task)
    
    return active_tasks


def strikethrough(text):
# https://stackoverflow.com/questions/25244454/python-create-strikethrough-strikeout-overstrike-string-type
    '''
    Converts normal characters to strikethrough characters and returns the result.
    '''
    return ''.join(char + '\u0336' for char in text)


def format_task(task):
    '''
    Formats task: dictionary into a presentable string for display.

    Status symbols:
    - [x] Applied to completed task
    - [ ] Applied to pending task

    Task name:
    - Strikethrough applied to completed task name

    Returns: Formatted string with visual progress markers.
    '''
    return f"[x] {strikethrough(task['name'])}" if task['done'] == 'TRUE' else f"[ ] {task['name']}"


def display_formatted_tasks(active_tasks):
    '''
    Applies string formatting to active tasks: list of task dictionaries,
    and displays formatted tasks in terminal.

    Shows "Empty" if there's no active tasks to display.
    '''
    if active_tasks:
        for task in active_tasks:
            print(format_task(task))
    else:
        print("Empty")


def display_todo_list(active_tasks):
    '''
    Displays formatted to-do list with:
    heading, visual list container and list contents.
    '''
    print(APP_HEADING)
    print(HORIZONTAL_LINE)
    display_formatted_tasks(active_tasks)
    print(HORIZONTAL_LINE)


def get_menu_choice():
    '''
    Prompts user for menu choice until a valid choice is entered.

    Options:
    - add
    - complete
    - delete
    - exit program

    Returns: Valid user input (str)
    '''
    while True:
        choice = input("\nEnter: (a) to add, (c) to complete, (d) to delete, (e) to exit\n").lower()
        if validate_menu_choice(choice):
            break
    
    return choice


def validate_menu_choice(choice):
    '''
    Takes choice: user input (str),
    and checks if it's a valid menu choice.

    Raises ValueError: if choice is not a valid menu option.

    Returns: True / False
    '''
    try:
        if choice not in ['a','c','d','e']:
            raise ValueError("Invalid menu choice")
    except ValueError as e:
        print(HORIZONTAL_LINE)
        print(f"Error: {e}. Please try again!")
        print(HORIZONTAL_LINE)
        return False
    return True


def generate_new_id(tasks):
    '''
    Takes tasks: list of all tasks and generates a new unique item_id
    based on the length of the task list.
    '''
    return len(tasks) + 1


def get_task_name():
    '''
    Prompts user for task name until input entered is not empty.
    
    Returns: Valid user input (capitalized str)
    '''
    while True:
        name = input("\nTask to add:\n").capitalize()
        if validate_task_name(name):
            break

    return name


def validate_task_name(name):
    '''
    Takes name: user input (str),
    and checks if input contains characters.

    Raises ValueError: if input is empty.

    Returns: True / False
    '''
    try:
        if not name:
            raise ValueError("Task name cannot be empty")
    except ValueError as e:
        print(HORIZONTAL_LINE)
        print(f"Error: {e}. Please try again!")
        print(HORIZONTAL_LINE)
        return False
    return True


def get_current_date():
    '''
    Returns: the current date in format YYYY-MM-DD
    '''
    return datetime.today().strftime('%Y-%m-%d')


def add_task_to_sheet(new_task):
    '''
    Takes new task data: [item_id, name, done, active, created_on]
    and appends it as a new row in the tasks worksheet.
    '''
    TASKS_WORKSHEET.append_row(task_data)


def add_task(tasks):
    '''
    Creates and adds a new task to the tasks worksheet.

    - Generates unique item_id
    - Prompts user for task name
    - Sets default values for done and active fields
    - Retrieves the current date as created_on
    
    Appends list of new task data to sheet.
    '''
    item_id = generate_new_id(tasks)
    name = get_task_name()
    done = False
    active = True 
    created_on = get_current_date()

    new_task = [item_id, name, done, active, created_on]

    add_task_to_sheet(new_task)


def complete_task(active_tasks):
    '''
    '''


def handle_menu_choice(choice, tasks, active_tasks):
    '''
    Takes:
        choice: user input (str), 
        tasks: unfiltered list of task dictionaries,
        active tasks: filtered list of task dictionaries,
    to handle corresponding menu actions.
    '''
    if choice == 'a':
        add_task(tasks)
    elif choice == 'c':
        complete_task(active_tasks)
    elif choice == 'd':
        print("deleting task")
    elif choice == 'e':
        print("exiting program")


tasks = retrieve_data(TASKS_WORKSHEET)
active_tasks = exclude_inactive_tasks(tasks)
display_todo_list(active_tasks)
choice = get_menu_choice()
handle_menu_choice(choice, tasks, active_tasks)