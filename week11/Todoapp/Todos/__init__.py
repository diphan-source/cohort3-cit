from Todoapp.Todos.resource import Todo_resource

def Todo_routes(api):
    api.add_resource(Todo_resource, '/api/todos')