from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from ..models.glucose import Glucose
from ...utils.export_data import export


class ExportGlucoseView(APIView):
    """GET endpoint"""

    formats_availables = ["json", "csv", "excel"]
    file_format = "json"  # Default

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            file_format = self.request.query_params.get("file_format")

            if file_format:
                if file_format not in self.formats_availables:
                    raise ValidationError(
                        {
                            "message": _("Invalid file format query"),
                            "formats-available": str(self.formats_availables),
                        }
                    )

                self.file_format = file_format

            else:
                raise ValidationError(
                    detail=_("Missing format"),
                )

            try:
                response = export(format=self.file_format, queryset=queryset)
                return response

            except Exception as e:
                return Response(
                    {"error": _("An unexpected error occurred."), "detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(
                {"error": _("An unexpected error occurred.")},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        limit = self.request.query_params.get("limit")
        queryset = Glucose.objects.all()

        if user_id and type(user_id) is str:
            queryset = Glucose.objects.by_user(user_id=user_id)

        if start_date and end_date:
            queryset = Glucose.objects.by_date(
                record_date__range=[start_date, end_date]
            )

        if limit:
            try:
                queryset = queryset[: int(limit)]

            except ValueError as e:
                raise ValidationError(
                    {
                        "message": _("Invalid limit query"),
                        "detail": str(e),
                    }
                )

        else:
            queryset = queryset[:20]

        return queryset
