import gspread


from exporters.exporter import Exporter


class GSheetsExport(Exporter):

    details_rows = [
        'key',
        'summary',
        'issuetype',
        'labels',
        'assignee',
        'created',
        'resolutiondate',
        'customfield_10024',
        'status',
    ]

    statistical_rows = [
        'upstream',
        'downstream'
    ]

    sprint_statistical_rows = [
        'total_sprints',
    ]

    rows = details_rows + statistical_rows


    def __init__(self, url, upstream_statuses, downstream_statuses, sprint_field):
        self.url = url
        self.all_rows =  self.rows + upstream_statuses + downstream_statuses

        if sprint_field:
            self.all_rows = self.all_rows + self.sprint_statistical_rows

        self.google = gspread.oauth()        


    def export(self, issues, metrics) -> None:
        sheet = self.google.open_by_url(self.url)

        issues_merged = self.merge_metric(issues, metrics)

        sheet = self.google.open_by_url(self.url)

        worksheet = sheet.get_worksheet(0)
        worksheet.clear()

        worksheet.append_row(self.all_rows)

        formatted_sheet = []

        for issue in issues_merged:
            row = []
            for field in self.all_rows:
                if issue.get(field):
                    row.append(str(issue.get(field)))
                else:
                    row.append('')
            formatted_sheet.append(row)

        worksheet.append_rows(
            formatted_sheet,
            value_input_option='USER_ENTERED'
        )
