from database import db
from database.models import User
from Calendarium.Calendars.Google import GoogleCalendarService
from Calendarium.Events.Event import Event
from database.db_transactions import db_transaction
from Calendarium.Calendars.Microsoft import OutlookCalendarService

class SyncUserData:
    _user: User
    _accounts: list
    _events: list[Event]

    def __init__(self):
        # google_account = GoogleCalendarService('calendars/token.json', 'credentials.json')
        #
        # for event in google_account.read_events_from_calendar():
        #     print(event)
        #
        # google_account.add_event_to_calendar()

        outlook_account = OutlookCalendarService()

        response = outlook_account.add_event_to_calendar()

        print(response)




