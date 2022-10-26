from flask import Flask , Blueprint , jsonify , request 


errors = Blueprint('errors', __name__)

# 404 - Not Found
@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": f"resource {request.path} not found"
    }), 404
    
    

