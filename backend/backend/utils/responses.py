from rest_framework.response import Response

def send_json(message, body={}, status_code=200):
    return Response({"message":message, "body": body}, status=status_code)