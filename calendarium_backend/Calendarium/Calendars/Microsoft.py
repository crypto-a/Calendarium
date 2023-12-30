import requests

from Calendarium.Calendars.Base.CalendarAccount import CalenderService

import webbrowser
from datetime import datetime
import json
import os
import msal


class OutlookCalendarService(CalenderService):
    """
    Microsoft Outlook Calendar Service
    """

    _SCOPES = ['Calendars.ReadWrite']
    _GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'
    _APP_ID = '60109714-43af-4fde-ac6c-db47725dfefd'

    def __init__(self, token_json):

        # Save Session Token as a token file
        access_token_cache = msal.SerializableTokenCache()

        # read the token file
        if os.path.exists(token_json):
            access_token_cache.deserialize(open(token_json, "r").read())
            token_detail = json.load(open(token_json, ))
            token_detail_key = list(token_detail['AccessToken'].keys())[0]
            token_expiration = datetime.fromtimestamp(int(token_detail['AccessToken'][token_detail_key]['expires_on']))
            if datetime.now() > token_expiration:
                os.remove(token_json)
                access_token_cache = msal.SerializableTokenCache()

        # assign a SerializableTokenCache object to the client instance
        client = msal.PublicClientApplication(client_id=self._APP_ID, token_cache=access_token_cache)

        accounts = client.get_accounts()
        if accounts:
            # load the session
            token_response = client.acquire_token_silent(self._SCOPES, accounts[0])
        else:
            # authetnicate your accoutn as usual
            flow = client.initiate_device_flow(scopes=self._SCOPES)
            print('user_code: ' + flow['user_code'])
            webbrowser.open('https://microsoft.com/devicelogin')
            token_response = client.acquire_token_by_device_flow(flow)

        with open(token_json, 'w') as _f:
            _f.write(access_token_cache.serialize())

        self._access_token = token_response
        self._headers = {
            'Authorization': 'Bearer ' + self._access_token['access_token']
        }

    def read_events_from_calendar(self):
        response = requests.get(
            self._GRAPH_API_ENDPOINT + '/me/calendar/events',
            headers=self._headers
        )

        events = response.json().get('value', [])

        return events

    def add_event_to_calendar(self, event):
        # request_body = {
        #                 "subject": "Benjamin's Birthday",
        #                 "start": {
        #                     "dateTime": "2023-12-30T17:00:00",
        #                     "timeZone": "UTC"
        #                     },
        #                 "end": {
        #                     "dateTime": "2023-12-30T19:00:00",
        #                     "timeZone": "UTC"
        #                     }
        #                 }

        response = requests.post(
            self._GRAPH_API_ENDPOINT + f'/me/events',
            headers=self._headers,
            json=event
        )

        return response

    def delete_event_from_calendar(self, event_id):
        if not event_id:
            print("Event ID is required to delete an event.")
            return

        response = requests.delete(
            self._GRAPH_API_ENDPOINT + f'/me/events/{event_id}',
            headers=self._headers
        )

        if response.status_code == 204:
            print(f"Event with ID {event_id} deleted successfully.")
        else:
            print(f"Error deleting event: {response.status_code}, {response.text}")

