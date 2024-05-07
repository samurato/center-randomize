import csv


class ParseTSVFile:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, "r", newline="", encoding="utf-8") as file:
            self.reader = csv.DictReader(file, delimiter="\t")

    def get_columns(self):
        return self.reader.fieldnames

    def get_row_count(self):
        return len(list(self.reader))

    def get_column_count(self):
        return len(self.reader.fieldnames)

    def get_rows(self):
        data = []
        for row in self.reader:
            data.append(row)
        return data

    def get_column_data(self, column_name):
        data = []
        for row in self.reader:
            data.append(row[column_name])
        return data

    def get_row_data(self, row_number):
        data = []
        for row in self.reader:
            data.append(row)
        return data[row_number]
