from Tasks.user_tasks.task_resource import TaskResource as todo

def task_routes(api):
    api.add_resource(todo, '/api/tasks' , '/api/tasks/<int:task_id>')