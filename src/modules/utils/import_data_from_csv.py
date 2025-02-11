import csv
from datetime import datetime
from django.utils import timezone

from .process_headers import process_headers
from ..api.models.glucose import Glucose

DATE_TIME_FORMAT = "%d-%m-%Y %H:%M"


def import_glucose_from_csv(user_id, csv_file):
    """
    Import glucose CSV data.

    We'll process all rows first and create Glucose model objects from them
    and perform a bulk create. This way, no records will be inserted unless
    all records are good.
    """

    csv_data = []

    decoded_file = csv_file.read().decode("utf-8").splitlines()
    reader = csv.reader(decoded_file, delimiter=",", quotechar='"')

    for row in reader:
        csv_data.append(row)

    glucose_objects = []

    # Remove headers
    csv_data = process_headers(csv_data)

    for row in csv_data:
        if not row or len(row) < 6:
            continue

        record_type = row[3]
        glucose_value_str = None

        # Check the type of recording to obtain the correct glucose value
        if record_type == "0":
            glucose_value_str = row[4]
        elif record_type == "1":
            glucose_value_str = row[5]
        else:
            continue

        if not glucose_value_str.strip():
            continue

        try:
            # Parse date and time
            record_datetime = datetime.strptime(row[2], DATE_TIME_FORMAT)
            record_datetime = timezone.make_aware(record_datetime)

        except (ValueError, IndexError):
            continue

        glucose_objects.append(
            Glucose(
                user_id=user_id,
                glucose_value=float(glucose_value_str),
                record_date=record_datetime.date(),
                record_time=record_datetime.time(),
            )
        )

    Glucose.objects.bulk_create(glucose_objects)
