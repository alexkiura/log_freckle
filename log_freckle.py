"""Helper module to log hours on freckle."""

import datetime
import requests


TODAY = str(datetime.date.today())


def log_hours(
    hours='10:00',
    date=TODAY,
    url='',
    project_name='',
    project_tags='',
    csrf_token='',
    auth_token=''
):
    """Log hours on Freckle.

    Args:
        hours: The number of hours being logged.
        date: The day for which the hours are being logged.
        url: The endpoint to send the logged hours.
            'https://<organization>.letsfreckle/time/entries' where
            organization is the freckle organization you are signed up with.
        project_name: The name of the project you are logging hours for.
        project_tags: Tags describing the project.
                        Examples could be #client_designs, #mockups.
        csrf_token: A token
    """

    cookies = {'auth_token': auth_token}
    data = {
        'entry[minutes]': hours,
        'entry[date]': date,
        'entry[project]': project_name,
        'entry[description]': project_tags,
    }
    request = requests.post(
        url=url, data=data, cookies=cookies)

    return request
