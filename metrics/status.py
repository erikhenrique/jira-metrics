from dateutil import parser

from collections import defaultdict



def time_by_status(issues, upstream_statuses, downstream_statuses) -> None:
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

                    metric['all_statuses'].add(item.toString)
                    metric['all_statuses'].add(item.fromString)

                    if last_event_date:
                        total_time_in_hours = int(
                            (last_event_date - created).total_seconds() / 60
                        )
                        total_hours_status[item.toString] += total_time_in_hours

                        if item.toString in upstream_statuses:
                            total_hours_status['upstream'] += total_time_in_hours

                        if item.toString in downstream_statuses:
                            total_hours_status['downstream'] += total_time_in_hours
                    
                    last_event_date = created

        metric['results'].append(total_hours_status)

    return metric
