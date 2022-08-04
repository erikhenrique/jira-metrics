import csv


from exporters.exporter import Exporter


class CSVExport(Exporter):
    def export(self, issues) -> None:

        headers = self.build_headers(issues)

        with open('csv_exporter.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for issue in issues:
                writer.writerow(issue)
