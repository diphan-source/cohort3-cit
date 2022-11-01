from Tasks.user.user_resource import Users

def user_routes(api):
    api.add_resource(Users , '/api/users' , '/api/users/<int:user_id>')