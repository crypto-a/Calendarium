

class CalendarAccount:
    _username: str
    _password: str
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def read_events_from_calendar(self):
        raise NotImplementedError

    def add_event_to_calendar(self):
        raise NotImplementedError

    def delete_event_from_calendar(self):
        raise NotImplementedError

    def keep_track_of_calendar(self):
        raise NotImplementedError