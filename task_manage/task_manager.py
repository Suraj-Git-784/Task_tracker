from datetime import datetime
from storage import load_task, save_task

#Function to add the task
def add_task(description):
    tasks = load_task()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_task(tasks)
    return task_id

#Function to show the list of the tasks
def list_tasks(filter_status=None):
    tasks = load_task()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    return tasks

#Function to update the tasks
def update_tasks(task_id, new_description):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().isoformat()
            save_task(tasks)
            return True
        return False

# Function to delete the task
def delete_tasks(task_id):
    tasks = load_task()

    update_task_after_delete = [task for task in tasks if task["id"] != task_id]

    if len(update_task_after_delete) < len(tasks):
        save_task(update_task_after_delete)
        return True
    return False

#Function to handle status for the tasks
def mark_tasks(task_id, status):
    tasks = load_task()
    for task in tasks:
        if task["id"]  == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_task(tasks)
            return True
        return False