import gspread


from exporters.exporter import Exporter


class GSheetsExport(Exporter):
    url = 'https://docs.google.com/spreadsheets/d/1tRq9cyAAKWqe7hcp6aRVBl4bjw90So7UuUKrHZAU6ag/edit?usp=sharing'

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


    def __init__(self):
        self.google = gspread.oauth()        


    def export(self, issues, metric) -> None:
        sheet = self.google.open_by_url(self.url)

        issues_merged = self.merge_metric(issues, metric)

        sheet = self.google.open_by_url(self.url)

        worksheet = sheet.get_worksheet(0)
        worksheet.clear()

        worksheet.append_row(self.rows)

        formatted_sheet = []
        for issue in issues_merged:
            row = []
            for field in self.rows:
                if issue.get(field):
                    row.append(str(issue.get(field)))
                else:
                    row.append('')
            formatted_sheet.append(row)

        worksheet.append_rows(
            formatted_sheet,
            value_input_option='USER_ENTERED'
        )
