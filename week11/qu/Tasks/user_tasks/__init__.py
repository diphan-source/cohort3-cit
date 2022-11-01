from Tasks.user_tasks.task_resource import Tasks

def task_routes(api):
    api.add_resource(Tasks , '/api/tasks' , '/api/tasks/<int:task_id>')