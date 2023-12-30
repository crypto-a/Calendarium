from database import db
from database.models import User
from Calendarium.Calendars.Google import GoogleCalendarService
from Calendarium.Events.Event import Event
from database.db_transactions import db_transaction
from Calendarium.Calendars.Microsoft import OutlookCalendarService
from Calendarium.account import Account


class SyncUserData:
    _user: User
    _accounts: list
    _events: list[Event]

    def __init__(self, user_id=None):
        self._accounts = [{'type': 'Google'}, {'type': 'Microsoft'}]
        self._events = []
        self.sync_user_data()

    def sync_user_data(self):

        # Loop through all the accounts
        for account_details in self._accounts:
            # Connect to account
            account = Account(account_details)

            events = account.read_events_from_calendar()

            # Split the events into old and new
            old_events, new_events = self.check_if_event_exists(events)

            # ToDo: Delete deleted events
            # ToDo: does event already exist

            # Push new events to other accounts
            self.push_events_to_other_accounts(new_events, account_details)


    def check_if_event_exists(self, events):

        old_events = []
        new_events = []

        # Loop through all the events
        for event in events:
            if any(event_id in recorded_events.event_ids for recorded_events in self._events for event_id in event.event_ids):
                old_events.append(event)

            else:
                new_events.append(event)

        return old_events, new_events

    def push_events_to_other_accounts(self, new_events, account_details):
        remaining_accounts = [account for account in self._accounts if account != account_details]

        for account_details in remaining_accounts:

            account = Account(account_details)

            for new_event in new_events:
                new_event.event_ids[account_details['type']] = account.add_event_to_calendar(new_event)

        self._events.extend(new_events)



