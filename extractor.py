from jira import JIRA


from metrics.status import time_by_status
from exporters.csv_exporter import CSVExport


def search_issues(project, months_ago=6):
    jira = JIRA(
        server='',
        basic_auth=('', ''),
    )
    
    query = f'project={project} AND created <= -{months_ago}m'

    return jira.search_issues(query, expand='changelog', maxResults=False)



def merge_metrics(issues, metrics):
    fields = [
        'created',
        'summary',
        'labels',
        'assignee',
        'issuetype',
        'status',
        'votes',
        'resolutiondate',
        'customfield_10024' # votação
    ]

    result = []

    for issue in issues:
        issue_dict = { 'key': issue.key }

        for field in fields:
            issue_dict[field] = getattr(issue.fields, field)

        for metric in metrics['results']:
            if metric['key'] == issue.key:
                issue_dict = dict(issue_dict, **metric)

        result.append(issue_dict)

    return result



def extract():
    issues = search_issues(project='VDPLAT', months_ago=6)

    metric = time_by_status(issues)

    issues_merged = merge_metrics(issues, metric)

    exporter = CSVExport()
    exporter.export(issues_merged)



extract()
