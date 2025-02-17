from django.urls import path

from .views.post_glucose import upload_csv_file
from .views.get_glucose import GlucoseListView, GlucoseDetailView
from .views.get_task_status import get_task_status


urlpatterns = [
    path("upload-csv/", upload_csv_file, name="upload-csv-file"),
    path("levels/", GlucoseListView.as_view(), name="glucose-list"),
    path("levels/<int:pk>/", GlucoseDetailView.as_view(), name="glucose-detail"),
    path("task-status/<str:task_id>/", get_task_status, name="task-status"),
]
