# Example using Python with the google-api-python-client library
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from Calendarium.Calendars.Base.CalendarAccount import CalenderService
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleCalendarService(CalenderService):

    _SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']

    def __init__(self, token_json, credentials_json):
        # Set up OAuth 2.0 credentials
        creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self._SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self._SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        # Build the service
        self._service = build('calendar', 'v3', credentials=creds)

    def read_events_from_calendar(self):
        # Call the API to get events
        events_result = self._service.events().list(calendarId='primary', timeMin='2023-01-01T00:00:00Z',
                                              timeMax='2024-01-30T23:59:59Z', maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()


        return events_result.get('items', [])

    def add_event_to_calendar(self, event):
        # Define the event
        # event = {
        #     'summary': 'Event Summary',
        #     'location': 'Event Location',
        #     'description': 'Event Description',
        #     'start': {
        #         'dateTime': '2023-12-26T10:00:00',
        #         'timeZone': 'UTC',
        #     },
        #     'end': {
        #         'dateTime': '2023-12-26T12:00:00',
        #         'timeZone': 'UTC',
        #     },
        # }

        # Insert the event
        event = self._service.events().insert(calendarId='primary', body=event).execute()

        return event['id']

