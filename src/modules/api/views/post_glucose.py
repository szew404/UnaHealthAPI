from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema

from modules.tasks.process_csv_file import process_csv_glucose_file
from ..serializers.upload_files import CSVUploadSerializer

import os


@extend_schema(
    request=CSVUploadSerializer,
)
@api_view(["POST"])
def upload_csv_file(request) -> Response:
    """POST to upload a csv file"""

    serializer = CSVUploadSerializer(data=request.data, context={"request": request})

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    csv_file = request.FILES["csv_file"]

    try:
        user_id = os.path.splitext(csv_file.name)[0]
        content = csv_file.read()

        # Async task to process the file
        task = process_csv_glucose_file.delay(csv_content=content, user_id=user_id)

        return Response(
            {"status": "File is being processed", "task_id": task.id},
            status=status.HTTP_202_ACCEPTED,
        )

    except UnicodeDecodeError:
        return Response(
            {"error": "File encoding error"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
