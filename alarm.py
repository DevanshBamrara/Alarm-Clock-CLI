from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    """
    Represents a single alarm.
    """

    id: int
    alarm_time: datetime
    label: str = ""
    active: bool = True

    def formatted_time(self, use_24_hour: bool = True) -> str:
        """
        Returns the alarm time as a formatted string.

        Args:
            use_24_hour: If True, returns time in 24-hour format.
                         If False, returns time in 12-hour AM/ PM format.

        Returns:
            Formatted time string.
        """

        if use_24_hour:
            return self.alarm_time.strftime("%H:%M")

        return self.alarm_time.strftime("%I:%M %p")