from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.tasks.process_csv_file import process_csv_glucose_file
from ..serializers.upload_files import CSVUploadSerializer

import os


class CSVUploadView(APIView):
    """
    Endpoint for uploading glucose data CSV files
    """

    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(
            data=request.data, context={"request": request}
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        csv_file = request.FILES["csv_file"]

        try:
            user_id = os.path.splitext(csv_file.name)[0]
            content = csv_file.read().decode("utf-8")

            # Async task to process the file
            process_csv_glucose_file.delay(csv_content=content, user_id=user_id)

            return Response(
                {"status": "File is being processed"},
                status=status.HTTP_202_ACCEPTED,
            )

        except UnicodeDecodeError:
            return Response(
                {"error": "File encoding error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
