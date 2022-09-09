


def sprint_statistics(issues, sprint_field='customfield_10020') -> None:

    ## total de sprints que a tarefa ficou
    ## primeira sprint
    ## sprint ativa

    metric = {
        'results': []
    }

    for issue in issues:

        if getattr(issue.fields, sprint_field):
            metric['results'].append({
                'key': issue.key,
                'total_sprints': len(getattr(issue.fields, sprint_field))
            })

    return metric

