"""Log freckle entries for multiple days."""
from log_freckle import log_hours
from datetime import timedelta
import datetime

url = 'https://andela.letsfreckle.com/time/entries'
auth_token = 'your_auth_token_here'
project_name = 'ProjectName'
project_tags = '#projct tags here'


start = datetime.date(2018, 1, 3)
end = datetime.date(2018, 3, 12)


if __name__ == '__main__':
    dates = [str(day) for day in (
        start + timedelta(days=num)
        for num in range(0, (end-start).days + 1)) if day.isoweekday() <= 5]

    for date in dates:
        request = log_hours(
            date=date, url=url, project_name=project_name,
            project_tags=project_tags, auth_token=auth_token
        )
        if request.status_code is 200 or 201:
            print('Successfully logged for {}'.format(str(date)))
