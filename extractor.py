from jira import JIRA

from metrics.status import time_by_status
from exporters.csv_exporter import CSVExport
from exporters.gsheets_exporter import GSheetsExport


def search_issues(project, months_ago=6):
    jira = JIRA(
        server='',
        basic_auth=('', ''),
    )
    
    query = f'project={project} AND created <= -{months_ago}m'

    return jira.search_issues(query, expand='changelog', maxResults=False)


def extract():
    issues = search_issues(project='VDPLAT', months_ago=6)

    metric = time_by_status(
        issues,
        upstream_statuses=[
            'Backlog',
            'Refining',
            'Priorizados',
            'Detalhamento da Hipótese',
            'A Iniciar',
        ],
        downstream_statuses=[
            'Aguardando Desenvolvimento',
            'In Progress',
            'Code Review',
            'Em Homologação',
        ]
    )

    # exporter = CSVExport()
    # exporter.export(issues, metric)

    sheets = GSheetsExport()
    sheets.export(issues, metric)

extract()
