
class Event(object):
    _user_id: int
    _event_id: int
    _calender_ids: list[str]

    def __init__(self, user_id: int):
        self._user_id = user_id

