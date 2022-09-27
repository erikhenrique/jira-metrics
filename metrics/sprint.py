import re


def total_sprints(issue, sprint_field) -> int:
    return len(getattr(issue.fields, sprint_field))


def actual_sprint(issue, sprint_field) -> str:
    actual_sprint_id = None
    actual_sprint = None

    for sprint in getattr(issue.fields, sprint_field):
        if not actual_sprint_id:
            actual_sprint_id = sprint.id
            actual_sprint = sprint.name

        if sprint.id > actual_sprint_id:
            actual_sprint_id = sprint.id
            actual_sprint = sprint.name

    return re.sub(r'[^0-9]', '', actual_sprint) if actual_sprint else ''



def sprint_statistics(issues, sprint_field='customfield_10020') -> None:
    metric = {
        'results': []
    }

    for issue in issues:
        if getattr(issue.fields, sprint_field):
            metric['results'].append({
                'key': issue.key,
                'total_sprints': total_sprints(issue, sprint_field),
                'actual_sprint': actual_sprint(issue, sprint_field)
            })
        else:
            metric['results'].append({
                'key': issue.key,
                'total_sprints': '0',
                'actual_sprint': '0'
            })

    return metric

