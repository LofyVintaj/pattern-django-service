from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def jira_console_log_view(request):
    return Response({"200": "OK"})