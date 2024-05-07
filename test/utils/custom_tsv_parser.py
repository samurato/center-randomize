import csv


class ParseTSVFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._read_file()

    def _read_file(self):
        with open(self.file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter="\t")
            return list(reader)

    def get_columns(self):
        return self.data[0].keys()

    def get_row_count(self):
        return len(self.data)

    def get_column_count(self):
        return len(self.data[0].keys())

    def get_rows(self):
        return self.data

    def get_column_data(self, column_name):
        return [row[column_name] for row in self.data]

    def get_row_data(self, row_number):
        return self.data[row_number]
