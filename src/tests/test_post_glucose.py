# These tests were created using GPT-o4

import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..modules.api.views.post_glucose import upload_csv_file
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch


@pytest.mark.django_db
class TestUploadCSVFile:
    def setup_method(self):
        self.factory = APIRequestFactory()
        self.url = "/api/upload-csv/"

    def test_upload_csv_file_success(self):
        csv_content = "date,glucose\n2023-01-01,100\n"
        csv_file = SimpleUploadedFile(
            "user1.csv", csv_content.encode("utf-8"), content_type="text/csv"
        )
        request = self.factory.post(
            self.url, {"csv_file": csv_file}, format="multipart"
        )

        with patch(
            "modules.tasks.process_csv_file.process_csv_glucose_file.delay"
        ) as mock_task:
            response = upload_csv_file(request)
            assert response.status_code == status.HTTP_202_ACCEPTED
            assert response.data == {"status": "File is being processed"}
            mock_task.assert_called_once_with(csv_content=csv_content, user_id="user1")

    def test_upload_csv_file_invalid_serializer(self):
        request = self.factory.post(self.url, {}, format="multipart")
        response = upload_csv_file(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_upload_csv_file_encoding_error(self):
        csv_file = SimpleUploadedFile(
            "user1.csv", b"\x80\x81\x82", content_type="text/csv"
        )
        request = self.factory.post(
            self.url, {"csv_file": csv_file}, format="multipart"
        )
        response = upload_csv_file(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"error": "File encoding error"}

    def test_upload_csv_file_general_exception(self):
        csv_content = "date,glucose\n2023-01-01,100\n"
        csv_file = SimpleUploadedFile(
            "user1.csv", csv_content.encode("utf-8"), content_type="text/csv"
        )
        request = self.factory.post(
            self.url, {"csv_file": csv_file}, format="multipart"
        )

        with patch(
            "modules.tasks.process_csv_file.process_csv_glucose_file.delay",
            side_effect=Exception("Test Exception"),
        ):
            response = upload_csv_file(request)
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
            assert response.data == {"error": "Test Exception"}
