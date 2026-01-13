tasks = []
current_id = 1

def create_task(title, description, priority="media"):
    global current_id
    task = {
        "id": current_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pendente"
    }
    tasks.append(task)
    current_id += 1
    return task


def list_tasks():
    return tasks

def update_task(task_id, new_title, new_description):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            task["description"] = new_description
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
