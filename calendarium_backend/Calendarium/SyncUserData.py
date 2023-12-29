from database import db
from database.models import User
from Calendarium.Calendars.Google import GoogleCalendarService
from database.db_transactions import db_transaction

class SyncUserData:
    _user: User
    _accounts: list
    _events: list

    def __init__(self):
        google_account = GoogleCalendarService('calendars/token.json', 'credentials.json')

        for event in google_account.read_events_from_calendar():
            print(event)

        google_account.add_event_to_calendar()


