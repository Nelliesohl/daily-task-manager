
# Planning  

This document outlines the structured approach taken to plan and develop my third portfolio project.

## Project Constraints

| Type | Requirement |
|--------------------------|------------------------------------------|
| Application          | Command Line Interface (CLI)  |
| Programming Language | Python                                   |
| Demo Tool            | Web-based mock terminal provided by Code Institute |
| Dimensions           | 80 columns x 24 rows                     |
| Hosting Platform     | Heroku                                   |
| Timeline             | 1 week :  Plan, Develop, Test, Deploy and Document      |



## Project Idea  

Develop a Minimum Viable Product (MVP) for a command-line interface (CLI) to-do list application.  


## Goals and Objectives
- Provide a simple and intuitive command-line interface tool to manage daily tasks.
- Enable users to view, add, complete and remove tasks with immediate visual feedback.
- Allow users to track their progress with visual markers for to-do / done status.
- Store task data in Google Sheets for secure, reliable cloud storage.
- Sync data in real-time for accurate and up-to-date task display.
- Preserve historical data for review by utilizing a soft deletion mechanism.
- Validate user inputs to ensure predefined rules and constraints are met.
- Display helpful error messages for invalid inputs.
- Implement error handling for data retrieval issues.
- Provide clear and instructive documentation for ease of use.  
- Showcase the app’s functionality via a web-based mock terminal hosted on Heroku.


## Target Audience

- Individuals seeking a simple task management tool.  
- Developers looking for a terminal-based task manager to support workflow. 
- Developers or learners exploring Python integrations with Google APIs.  
- Beginners seeking hands-on coding experience with CRUD operations and API integration.


## Features
The application will include the following features, designed to align with the project's goals and objectives:  

### User Interface
- Simple and clutter free design to foster productivity.
- Includes application heading, to-do list, and interactive menu. 
- Instantly reflects changes (added, completed, or deleted tasks) to user. 

### Task Management
(CRUD Operations)
  - **Create**: Add new tasks to the list.
  - **Read**: View tasks and track progress.
  - **Update**: Mark tasks as complete.
  - **Delete**: Remove tasks from the list.

### Status Tracking
Visual indicators for task progress:
- **To-do**: Empty checkbox, normal text.
- **Done**: Checked box and strikethrough text.

### Error Handling & Validation
- Ensures that a valid spreadsheet and worksheet exist before attempting data operations.
- Validates all user input to ensure predefined rules and constraints are met.
- Provides user with helpful feedback for any missteps.

### Cloud Storage
- Utilizes Google Sheets to securely store and manage task data.
- Eliminates data loss risks with real-time API synchronization.
- Soft deletion ensures task history is preserved for review without cluttering the active to-do list.

### Live Demo
- Live demonstration available via a web-based mock terminal hosted on Heroku.  


## Features Left Out

Certain features were intentionally excluded from this version of the project to keep it focused as an MVP.

Examples:
- Grouping tasks under categories or priorities (e.g., "Work", "Personal" / "Low", "Mid", "High"). 
- Filtering tasks by category, priority or status.
- Display task history from choosen time-period (e.g., "Monthly")
- Automated deletion of inactive tasks after set time-period (e.g., "Yearly")
- Adding login functionality to allow multiple users to have personalized task lists.


## Data Storage  

[Google Sheets](https://workspace.google.com/products/sheets/)  
[Google Sheets API](https://developers.google.com/sheets/api/guides/concepts)  for cloud-based data management.  

| Field        | Type         | Description                                                  |  
|--------------|--------------|--------------------------------------------------------------|  
| `to_do_list` | Spreadsheet  | The primary Google Spreadsheet. |  
| `tasks` | Worksheet    | Worksheet containing all task-related data. |  


## Data Model

The `tasks` worksheet holds detailed information about each task. The fields are structured as follows:  

| Field      | Type   | Description                                   |  
|------------|--------|-----------------------------------------------|  
| `item_id`  | int    | A unique identifier for each task |  
| `name`     | str    | The name or description of the task.          |  
| `done`     | bool   | Indicates whether the task is completed (`True`) or not (`False`). |  
| `active`   | bool   | Indicates whether the task is active (`True`) or inactive (`False`), enabling soft deletion. |  
| `created_on` | datetime | Timestamp of task creation. | 


## Flow Chart
![Flow chart](https://www.mermaidchart.com/raw/04747b91-f62b-40ce-8fba-e29f15ef4f00?theme=light&version=v0.1&format=svg)

Flow chart created using [Mermaid Chart](https://www.mermaidchart.com/) 


## Visual Design
Layout constraints (80 col x 24 rows) was taken under consideration during design phase

### Heading

```
___  __      __   __             __  ___
 |  /  \    |  \ /  \    |    | /__`  | 
 |  \__/    |__/ \__/    |___ | .__/  |
```
Heading created using [ASCII Generator](https://www.asciiart.eu/text-to-ascii-art)  
Font used: JS Stick Letters


### List Container
```
--------------------------------------------------------------------------------
Empty
--------------------------------------------------------------------------------
```

### Status Symbols

**Complete**
```
[x]
```
**Incomplete**
```
[ ]
```
### Strikethrough text
```
 W̶a̶t̶e̶r̶ ̶p̶l̶a̶n̶t̶s̶
```
Found resource on how to accomplish strikethrough text here -> [Stackoverflow Thread](https://stackoverflow.com/questions/25244454/python-create-strikethrough-strikeout-overstrike-string-type)


## Credits and Aknowledgements

Documentation refined using [ChatGPT](https://openai.com/chatgpt/overview/).

Soft-delete approach suggested by my mentor, [Dick V.](https://www.linkedin.com/in/dick-vlaanderen/) 

Frequently visited the [Markdown Cheat Sheet](https://markdown-it.github.io/) as a helpful tool in the documentation process.

Used the gspread documentation to learn about potential [gspread exceptions](https://docs.gspread.org/en/latest/api/exceptions.html).




---