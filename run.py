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
    return f"[x] {task['name']}" if task['done'] == 'TRUE' else f"[ ] {task['name']}"


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


tasks = retrieve_data(TASKS_WORKSHEET)
active_tasks = exclude_inactive_tasks(tasks)
print(APP_HEADING)
display_formatted_tasks(active_tasks)