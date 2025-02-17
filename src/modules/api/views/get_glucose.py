from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from ..models.glucose import Glucose
from ..serializers.glucose import GlucoseSerializer


class GlucoseDetailView(generics.RetrieveAPIView):
    """GET endpoint that Retrieve a particular glucose level by id."""

    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


class GlucosePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class GlucoseListView(generics.ListAPIView):
    """GET endpoint that Retrieve a list of glucose levels for a given
    user_id , filter by start and stop timestamps (optional). Supports
    pagination, sorting, and limit the number of
    glucose levels returned."""

    serializer_class = GlucoseSerializer
    pagination_class = GlucosePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["record_date", "record_time"]
    ordering_fields = ["record_date", "record_time"]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        queryset = Glucose.objects.all()

        if user_id:
            queryset = Glucose.objects.by_user(user_id=user_id)

        if start_date and end_date:
            queryset = Glucose.objects.by_date(
                record_date__range=[start_date, end_date]
            )

        return queryset
