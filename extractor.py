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


def extract():
    issues = search_issues(project='VDPLAT', months_ago=1)

    metric = time_by_status(issues)

    exporter = CSVExport()
    exporter.export(issues, metric)


extract()
