import csv

from exporters.exporter import Exporter


class CSVExport(Exporter):

    rows = [
        'key',
        'summary',
        'issuetype',
        'labels',
        'assignee',
        'created',
        'resolutiondate',
        'customfield_10024',
        'status',
        'In Progress',
        'A Iniciar',
        'Testes',
        'Concluído',
        'Validação 2',
        'Pool de Ideias',
        'Aguardando Desenvolvimento',
        'Em Homologação',
        'Atividade bloqueada',
        'Backlog',
        'Pronto p/ DEV',
        'Detalhamento da Hipótese',
        'Code Review',
        'Cancelado',
        'Priorizados',
        'Discovery Concluído',
        'Em desenvolvimento',
        'Atividade finalizada',
        'Refining',
        'Done',
        'upstream',
        'downstream'
    ]


    def export(self, issues, metric) -> None:
        issues_merged = self.merge_metric(issues, metric)

        with open('csv_exporter.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.rows)
            writer.writeheader()

            for issue in issues_merged:
                writer.writerow(issue)
