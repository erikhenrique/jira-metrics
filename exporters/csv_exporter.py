import csv

from exporters.exporter import Exporter


class CSVExport(Exporter):

    def export(self, issues, metric) -> None:
        issues_merged = self.merge_metric(issues, metric)

        headers = self.build_headers(issues_merged)

        with open('csv_exporter.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for issue in issues_merged:
                writer.writerow(issue)
