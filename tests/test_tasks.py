from src.app import create_task, list_tasks

def test_create_task():
    task = create_task("Estudar Engenharia de Software", "Revisar conteúdo")
    tasks = list_tasks()
    assert task in tasks
