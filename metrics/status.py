from dateutil import parser

from collections import defaultdict


def time_by_status(issues) -> None:

    metric = {
        'total_status': set(),
        'results': []
    }

    for issue in issues:
        total_seconds_status = defaultdict(float)
        total_seconds_status['key'] = issue.key
        last_event_date = None

        for history in issue.changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    created = parser.isoparse(history.created)

                    metric['total_status'].add(item.toString)
                    metric['total_status'].add(item.fromString)

                    if last_event_date:
                        total_seconds_status[item.toString] += (last_event_date - created).total_seconds()
                    
                    last_event_date = created

        metric['results'].append(total_seconds_status)

    return metric
