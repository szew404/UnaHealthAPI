# tu_app/tasks.py
from celery import shared_task
from io import StringIO
from ..utils.import_data_from_csv import import_glucose_from_csv


@shared_task
def process_csv_glucose_file(csv_content):
    try:
        csv_file = StringIO(csv_content)
        import_glucose_from_csv(csv_file)

    except Exception as e:
        print(f"Error processing CSV: {str(e)}")
