from rest_framework.response import Response
from rest_framework import status


def FinalResponse(code,message=None,**kwargs):

    if not message:
        if status.is_informational(code): # 100 - 199
            message = "informational message"
        elif status.is_success(code): # 200 - 299
            message = "successful response"
        elif status.is_redirect(code): # 300 - 399
            message = "redirect"
        elif status.is_client_error(code): # 400 - 499
            message = "client side error"
        elif status.is_server_error(code): # 500 - 599
            message = "server error"
        else:
            message = "..."

    response = {"message" : message, "code" : code}

    for k,v in kwargs.items():
        response[k] = v
    return Response(response)