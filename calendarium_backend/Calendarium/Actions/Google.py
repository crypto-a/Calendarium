# Example using Python with the google-api-python-client library
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Set up OAuth 2.0 credentials
creds = Credentials.from_authorized_user_file('token.json')
if not creds.valid:
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())


# Build the service
service = build('calendar', 'v3', credentials=creds)

# Call the API to get events
events_result = service.events().list(calendarId='primary', timeMin='2023-01-01T00:00:00Z',
                                      timeMax='2023-12-31T23:59:59Z', maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    print(event['summary'])