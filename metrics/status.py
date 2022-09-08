from dateutil import parser

from collections import defaultdict



def time_by_status(issues, upstream_statuses, downstream_statuses):
    metric = {
        'all_statuses': set(),
        'results': []
    }

    for issue in issues:
        total_hours_status = defaultdict(float)
        total_hours_status['key'] = issue.key
        last_event_date = None

        for history in issue.changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    created = parser.isoparse(history.created)

                    status_to_string = item.toString.upper()
                    status_from_string = item.fromString.upper()

                    metric['all_statuses'].add(status_to_string)
                    metric['all_statuses'].add(status_from_string)

                    if last_event_date:
                        total_time_in_days = (last_event_date - created).days
                        total_hours_status[status_to_string] += total_time_in_days

                        if status_to_string in upstream_statuses:
                            total_hours_status['upstream'] += total_time_in_days

                        if status_to_string in downstream_statuses:
                            total_hours_status['downstream'] += total_time_in_days

                    last_event_date = created

        metric['results'].append(total_hours_status)

    return metric
