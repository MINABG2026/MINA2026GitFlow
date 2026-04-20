tasks = []

def add_task(name):
    task = {
        "id": len(tasks),  # ❌ BUG: ID może się powtarzać po usunięciu
        "name": name,
        "done": False
    }
    tasks.append(task)
    return task

def get_tasks():
    return tasks
