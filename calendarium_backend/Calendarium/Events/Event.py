from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event(object):
    event_ids: dict[str, str]
    event_summary: str
    event_start_time: datetime
    event_end_time: datetime

