# Task Tracker CLI

A simple command-line interface to track and manage tasks.

## Features
- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List tasks by status

## Usage
```bash
# Add a new task
python task_tracker/main.py add "Your task description"

# List all tasks
python task_tracker/main.py list

# Update a task
python task_tracker/main.py update <task_id> "New description"

# Mark a task as done
python task_tracker/main.py mark-done <task_id>

# Delete a task
python task_tracker/main.py delete <task_id>