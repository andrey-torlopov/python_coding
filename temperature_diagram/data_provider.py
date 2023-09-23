import csv


class DataProvider:

    def __init__(self, file_name: str):
        self.data = []
        self._parse_data(file_name)
        if len(self.data) > 1:
            self.has_data = True
        self.current_year = 1
        self.year_temperatures = []
        self.parse_temperatures()

    def _parse_data(self, file_name: str) -> None:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                row_data = [str(cell) for cell in row]
                self.data.append(row_data)

    @property
    def months(self) -> [str]:
        return self.data[0][1:13]

    @property
    def boundDates(self) -> [str]:
        return [self.data[1][0], self.data[-1][0]]

    def parse_temperatures(self) -> None:
        if not self.has_data:
            # self.year_temperatures = []
            self.year_title = "No data"
            return

        self.year_title = self.data[self.current_year][0]
        # self.year_temperatures = []
        row = self.data[self.current_year][1:13]
        if len(row) != 12:
            # self.year_temperatures = []
            self.year_title = "No data"
            self.has_data = False
            return

        for item in row:
            try:
                value = item.replace('.', '0.')
                self.year_temperatures.append(float(value))
            except ValueError:
                self.year_temperatures.append(0.0)

    def next_year(self) -> None:
        self.current_year += 1
        if self.current_year >= len(self.data):
            self.current_year = 1
            self.has_data = False
            # self.year_temperatures = []
            self.year_title = ""

        self.parse_temperatures()
