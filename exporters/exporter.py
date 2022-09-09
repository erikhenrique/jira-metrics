from abc import ABC, abstractmethod

import dateutil.parser


class Exporter(ABC):

    def build_headers(self, issues):
        headers = set()
        for issue in issues:
            headers.update(issue.keys())
        return headers

    def parse_date(self, date):
        return dateutil.parser.isoparse(date).strftime("%m/%d/%Y %H:%M:%S") if date else ''

    def format_field(self, field, value):
        if field in ('created', 'resolutiondate'):
            return self.parse_date(value)
        return value

    def merge_metric(self, issues, metrics):
        fields_to_extract = [
            'created',
            'summary',
            'labels',
            'assignee',
            'issuetype',
            'status',
            'resolutiondate',
            'customfield_10024' # votação
        ]

        result = []

        for issue in issues:
            issue_dict = { 'key': issue.key }

            for field in fields_to_extract:
                issue_dict[field] = self.format_field(
                    field,
                    getattr(issue.fields, field)
                )

            for metric in metrics:
                for metric_result in metric['results']:
                    if metric_result['key'] == issue.key:
                        issue_dict = dict(issue_dict, **metric_result)


            result.append(issue_dict)

        return result
    
    @abstractmethod
    def export(self, issues) -> None:
        pass
