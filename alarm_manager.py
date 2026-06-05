from datetime import datetime
from typing import List

from models.alarm import Alarm


class AlarmManager:
    """
    Manages alarms in memory.
    """

    def __init__(self) -> None:
        self.alarms: List[Alarm] = []
        self._next_id: int = 1

    def add_alarm(self, alarm_time: datetime, label: str = "") -> Alarm:
        """
        Add a new alarm.

        Raises:
            ValueError: If an alarm already exists for the given time.
        """
        if self.alarm_exists(alarm_time):
            raise ValueError(
                f"An alarm already exists for {alarm_time.strftime('%H:%M')}"
            )

        alarm = Alarm(
            id=self._next_id,
            alarm_time=alarm_time,
            label=label,
            active=True,
        )

        self.alarms.append(alarm)
        self._next_id += 1

        return alarm

    def delete_alarm(self, alarm_id: int) -> None:
        """
        Delete an alarm by its ID.

        Raises:
            ValueError: If the alarm is not found.
        """
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                self.alarms.remove(alarm)
                return

        raise ValueError(f"Alarm with ID {alarm_id} not found")

    def list_alarms(self) -> List[Alarm]:
        """
        Return all alarms sorted by time.
        """
        return sorted(self.alarms, key=lambda alarm: alarm.alarm_time)

    def alarm_exists(self, alarm_time: datetime) -> bool:
        """
        Check whether an alarm already exists for the given time.
        """
        return any(
            alarm.alarm_time == alarm_time
            for alarm in self.alarms
        )

    def get_due_alarms(self, current_time: datetime | None = None) -> List[Alarm]:
        """
        Return alarms that should trigger now.

        Matching is done at minute precision to avoid
        triggering multiple times within the same minute.
        """
        if current_time is None:
            current_time = datetime.now()

        due_alarms: List[Alarm] = []

        for alarm in self.alarms:
            if not alarm.active:
                continue

            if (
                alarm.alarm_time.year == current_time.year
                and alarm.alarm_time.month == current_time.month
                and alarm.alarm_time.day == current_time.day
                and alarm.alarm_time.hour == current_time.hour
                and alarm.alarm_time.minute == current_time.minute
            ):
                due_alarms.append(alarm)

        return due_alarms