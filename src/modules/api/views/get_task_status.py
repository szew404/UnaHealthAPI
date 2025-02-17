from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from celery.result import AsyncResult


@api_view(["GET"])
def get_task_status(request, task_id: str) -> Response:
    """GET to check the status of a task"""
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result,
    }
    return Response(result, status=status.HTTP_200_OK)
