from datetime import timedelta

from alarm import Alarm
from alarm_manager import AlarmManager

import winsound


class NotificationService:
    """
    Handles alarm notifications, snoozing, and dismissal.
    """

    def __init__(self, alarm_manager: AlarmManager) -> None:
        self.alarm_manager = alarm_manager

    def trigger_alarm(self, alarm: Alarm) -> None:
        """
        Display alarm information and ask the user
        whether to snooze or dismiss.
        """
        print("\n" + "=" * 40)
        print("ALARM!")
        import winsound
        for _ in range(5):
            winsound.Beep(1000, 500)
        print(f"Label : {alarm.label or 'No Label'}")
        print(f"Time  : {alarm.formatted_time()}")
        print("=" * 40)

        while True:
            print("\n1. Snooze 5 minutes")
            print("2. Dismiss")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.snooze_alarm(alarm)
                break

            if choice == "2":
                self.dismiss_alarm(alarm)
                break

            print("Invalid choice. Please enter 1 or 2.")

    def snooze_alarm(self, alarm: Alarm) -> None:
        """
        Snooze an alarm for 5 minutes.

        Prevents snoozing if another alarm already
        exists at the new time.
        """
        snooze_time = alarm.alarm_time + timedelta(minutes=5)

        if self.alarm_manager.alarm_exists(snooze_time):
            print(
                f"Cannot snooze. An alarm already exists at "
                f"{snooze_time.strftime('%H:%M')}."
            )
            return

        alarm.alarm_time = snooze_time

        print(
            f"Alarm snoozed until "
            f"{alarm.alarm_time.strftime('%H:%M')}."
        )

    def dismiss_alarm(self, alarm: Alarm) -> None:
        """
        Dismiss an alarm so it does not trigger again.
        """
        alarm.active = False
        print("Alarm dismissed.")