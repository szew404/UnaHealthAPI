from django.urls import path

from .views.post_glucose import upload_csv_file
from .views.get_glucose import GlucoseListView, GlucoseDetailView, get_task_status


urlpatterns = [
    path("upload-csv/", upload_csv_file, name="upload-csv-file"),
    path("glucose/", GlucoseListView.as_view(), name="glucose-list"),
    path("api/v1/levels/<int:pk>/", GlucoseDetailView.as_view(), name="glucose-detail"),
    path("api/task-status/<str:task_id>/", get_task_status, name="task-status"),
]
