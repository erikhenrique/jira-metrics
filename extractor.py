from jira import JIRA

from metrics.status import time_by_status
from exporters.csv_exporter import CSVExport
from exporters.gsheets_exporter import GSheetsExport


def search_issues(project, months_ago):
    jira = JIRA(
        server='',
        basic_auth=('', ''),
    )
    
    query = f'project={project} AND created <= -{months_ago}m'

    return jira.search_issues(query, expand='changelog', maxResults=False)


def extract(project, upstream_statuses, downstream_statuses, months_ago=1, google_sheets_url=None):
    issues = search_issues(project=project, months_ago=months_ago)

    metric = time_by_status(
        issues,
        upstream_statuses=upstream_statuses,
        downstream_statuses=downstream_statuses
    )

    # exporter = CSVExport()
    # exporter.export(issues, metric)

    sheets = GSheetsExport(
        url=google_sheets_url,
        upstream_statuses=upstream_statuses,
        downstream_statuses=downstream_statuses
    )
    sheets.export(issues, metric)


def extract_produto_busca():
    extract(
        project='VDPLAT',
        upstream_statuses=[
            'BACKLOG',
            'REFINING',
            'PRIORIZADOS',
            'DETALHAMENTO DA HIPÓTESE',
            'A INICIAR',
        ],
        downstream_statuses=[
            'AGUARDANDO DESENVOLVIMENTO',
            'IN PROGRESS',
            'CODE REVIEW',
            'EM HOMOLOGAÇÃO',
        ],
        google_sheets_url=''
    )


def extract_im():
    extract(
        project='IM',
        upstream_statuses=[
            'POOL DE IDEIAS',
            'A INICIAR',
            'DETALHAMENTO DA HIPÓTESE',
            'CRIAÇÃO',
            'REFINING',
            'AGUARDANDO DESENVOLVIMENTO',
        ],
        downstream_statuses=[
            'PRIORIZADOS',
            'AGUARDANDO DESENVOLVIMENTO',
            'DISCOVERY CONCLUÍDO',
            'IN PROGRESS',
            'AGUARDANDO TESTES',
            'EM DESENVOLVIMENTO',
            'EM HOMOLOGAÇÃO',
            'AGUARDANDO HOMOLOGAÇÃO',
            'TESTES',
            'VALIDAÇÃO 1',
            'VALIDAÇÃO 2',
            'CODE REVIEW',
            'AJUSTES V1',
            'PRONTO P/ CODE REVIEW',
            'ACEITO',
            'PRONTO P/ DEPLOY EM PROD',
        ],
        google_sheets_url=''
    )


extract_im()
