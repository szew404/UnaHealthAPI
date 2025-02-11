def process_headers(csv_data):
    """
    Processes the CSV headers to get only the data rows.
    Removes the metadata rows and column headers.
    """
    data_start_index = None
    for i, row in enumerate(csv_data):
        if row and row[0] == "Gerät":
            data_start_index = i + 1
            break

    if data_start_index is not None:
        return csv_data[data_start_index:]
    return []
