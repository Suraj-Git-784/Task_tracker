import sys
from task_tracker.task_manager import add_task, list_tasks, update_tasks, delete_tasks, mark_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: task cli <command> [arguments]")
        sys.exit(1)
    command = sys.argv[1]

    if command is 'add':
        description = " ".join(sys.argv[2:])
        task_id = add_task(description)
        print(f"Task added successfully (ID: {task_id})")
    elif command is 'list':
        status = sys.argv[2] if len(sys.argv) > 2 else None
        tasks= list_tasks(filter_status=status)
        for task in tasks:
            print(f"[{task['status'].upper()}] {task['id']} : {task['description']}")
    elif command is 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update <task_id> <new_description>")
            return
        task_id = int(sys.argv[2])
        new_description = " ".join(sys.argv[3:])
        success = update_tasks(task_id, new_description)
        print("Task successfully updated" if success else "Task not found")
    elif command is 'delete':
        task_id = int(sys.argv[2])
        success = delete_tasks(task_id)
        print("Task is successfully deleted" if success else "Task not found")

    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        success = mark_tasks(task_id, "in-progress")
        print("Task marked as in-progress" if success else "Task not found")

    elif command == "mark-done":
        task_id = int(sys.argv[2])
        success = mark_tasks(task_id, "done")
        print("Task marked as done" if success else "Task not found")

if __name__ == "__main__":
    main()