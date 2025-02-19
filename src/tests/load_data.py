# This file works for uploading CSV sample files,
# this file was only used to test the POST endpoint '/api/v1/upload-csv/'.

import os
import requests

url = "https://unahealthapi.onrender.com/api/v1/upload-csv/"

sample_data_dir = "src/tests/sample-data"

for filename in os.listdir(sample_data_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(sample_data_dir, filename)

        with open(file_path, "rb") as csv_file:
            files = {"csv_file": (filename, csv_file, "text/csv")}

            response = requests.post(url, files=files)

            print(f"Response for {filename}: {response.status_code}")
            print(response.json())
