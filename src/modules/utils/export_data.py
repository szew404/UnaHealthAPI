import pandas as pd
from django.http import HttpResponse
from typing import List
import json

from ..api.models.glucose import Glucose
from ..api.serializers.glucose import ExportGlucoseSerializer


def export(format: str, queryset: List[Glucose]):
    if format == "json":
        serializer = ExportGlucoseSerializer(queryset, many=True)

        response = HttpResponse(content_type="application/json")
        response["Content-Disposition"] = 'attachment; filename="glucose.json"'

        # Write data
        response.write(json.dumps(serializer.data, indent=4))

        return response

    else:
        data = {
            "User ID": [glucose.user_id for glucose in queryset],
            "Glucose Value mg/dL": [glucose.glucose_value for glucose in queryset],
            "Date": [glucose.record_date for glucose in queryset],
            "Time": [glucose.record_time for glucose in queryset],
        }

        df = pd.DataFrame(data)

        types = {
            "excel": {
                "content_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "content-disposition": 'attachment; filename="glucose.xlsx"',
            },
            "csv": {
                "content_type": "text/csv",
                "content-disposition": 'attachment; filename="glucose.csv"',
            },
        }

        response = HttpResponse(content_type=types[format]["content_type"])
        response["Content-Disposition"] = types[format]["content-disposition"]

        # Write data
        if format == "excel":
            df.to_excel(response, index=False)
        if format == "csv":
            df.to_csv(response, index=False)

        return response
