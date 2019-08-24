import csv

def csv_columns(rows, *, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns."""
    reader = csv.reader(rows)
    if headers is None:
        headers = next(reader)
    columns = {header: [] for header in headers}
    for row in reader:
        for i, header in enumerate(headers):
            try:
                columns[header].append(row[i])
            except IndexError:
                columns[header].append(missing)
    return columns