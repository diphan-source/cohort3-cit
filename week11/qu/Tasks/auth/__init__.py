from Tasks.auth.app_auth import Login , Register

def auth_routes(api):
    api.add_resource(Login , '/api/login')
    api.add_resource(Register , '/api/register')