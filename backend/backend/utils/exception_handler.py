from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied, ValidationError
from .responses import send_json


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print("Exception type: ", type(exc).__name__)
    print("Exception detail: ", exc)
    print("Exception Context: ", context)
    

    if response is None:
        err_msg, err_body, err_code = "Internal Server Error", {}, 500
    else:
        err_msg, err_body, err_code = type(exc).__name__, response.data, response.status_code

    
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed, PermissionDenied)):
        err_msg, err_body, err_code = "Unauthorized", {}, 401

    if isinstance(exc, ValidationError) and isinstance(response.data, dict) and 'email' in response.data:
        if 'unique' in response.data['email'][0].lower():
            err_msg = 'User already exists.'
        
    return send_json(message=err_msg, body={"errors": err_body}, status_code=err_code)


