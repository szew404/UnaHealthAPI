from django.urls import path

from .views.post_glucose import CSVUploadView

urlpatterns = [
    path("upload-csv/", CSVUploadView.as_view(), name="upload-csv-file"),
]
