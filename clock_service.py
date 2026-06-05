import time
from datetime import datetime

from alarm_manager import AlarmManager
from notification_service import NotificationService


class ClockService:
    """
    Continuously monitors alarms and triggers them when due.
    """

    def __init__(
        self,
        alarm_manager: AlarmManager,
        notification_service: NotificationService,
    ) -> None:
        self.alarm_manager = alarm_manager
        self.notification_service = notification_service

    def run(self) -> None:
        """
        Start the alarm monitoring loop.
        """
        if not self.alarm_manager.list_alarms():
            print("No alarms configured.")

        print("Alarm clock running...")

        try:
            while True:
                self.check_alarms()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nAlarm clock stopped.")

    def check_alarms(self) -> None:
        """
        Check whether any alarms are due and trigger them.
        """
        current_time = datetime.now()

        due_alarms = self.alarm_manager.get_due_alarms(current_time)

        for alarm in due_alarms:
            self.notification_service.trigger_alarm(alarm)