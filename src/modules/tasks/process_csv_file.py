from celery import shared_task
from io import BytesIO

from ..utils.import_data_from_csv import import_glucose_from_csv


@shared_task
def process_csv_glucose_file(user_id, csv_content):
    try:
        csv_file = BytesIO(csv_content)
        import_glucose_from_csv(user_id, csv_file)

    except Exception as e:
        print(f"Error processing CSV: {str(e)}")
