from Calendarium.Calendars.Base.CalendarAccount import CalenderService
from Calendarium.Calendars.Google import GoogleCalendarService
from Calendarium.Calendars.Microsoft import OutlookCalendarService

from Calendarium.Events.Event import Event

from datetime import datetime
class Account:
    _account: dict
    _calendar: CalenderService

    def __init__(self, account):
        self._account = account

        if self._account['type'] == "Google":
            self._calendar = GoogleCalendarService('token.json', 'credentials.json')

        elif self._account['type'] == "Microsoft":
            self._calendar = OutlookCalendarService('ms_graph_api_token.json')

    def read_events_from_calendar(self):

        event_objects = []

        events = self._calendar.read_events_from_calendar()

        if self._account['type'] == "Google":
            for event in events:
                event_objects.append(Event({'Google': event['id']},
                                           event['summary'],
                                           datetime.fromisoformat(event['start']['dateTime']),
                                           datetime.fromisoformat(event['end']['dateTime'])))

        elif self._account['type'] == "Microsoft":
            for event in events:
                event_objects.append(Event({'Microsoft': event['id']},
                                           event['subject'],
                                           datetime.fromisoformat(event['start']['dateTime']),
                                           datetime.fromisoformat(event['end']['dateTime'])))

        return event_objects

    def add_event_to_calendar(self, event_object):
        if self._account['type'] == "Google":
            event = {
                'summary': event_object.event_summary,
                'start': {
                    'dateTime': event_object.event_start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': event_object.event_end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                    'timeZone': 'UTC',
                },
            }

        elif self._account['type'] == "Microsoft":
            event = {
                    "subject": event_object.event_summary,
                    'start': {
                        'dateTime': event_object.event_start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                        'timeZone': 'UTC',
                    },
                    'end': {
                        'dateTime': event_object.event_end_time.strftime('%Y-%m-%dT%H:%M:%S'),
                        'timeZone': 'UTC',
                    },
                    }

        new_event_id = self._calendar.add_event_to_calendar(event)

        return new_event_id