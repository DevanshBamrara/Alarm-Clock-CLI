from alarm_manager import AlarmManager
from clock_service import ClockService
from notification_service import NotificationService
from utils import parse_alarm_time


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("Python CLI Alarm Clock")
    print("=" * 40)
    print("1. Add Alarm")
    print("2. List Alarms")
    print("3. Delete Alarm")
    print("4. Start Alarm Monitor")
    print("5. Exit")


def add_alarm(alarm_manager: AlarmManager) -> None:
    """Handle adding a new alarm."""
    time_input = input(
        "\nEnter alarm time "
        "(07:30, 14:45, 7:30 AM, 2:45 PM): "
    ).strip()

    label = input("Enter alarm label (optional): ").strip()

    try:
        alarm_time = parse_alarm_time(time_input)

        alarm = alarm_manager.add_alarm(
            alarm_time=alarm_time,
            label=label,
        )

        print(
            f"Alarm #{alarm.id} set for "
            f"{alarm.formatted_time()}"
        )

    except ValueError as error:
        print(f"Error: {error}")


def list_alarms(alarm_manager: AlarmManager) -> None:
    """Display all alarms."""
    alarms = alarm_manager.list_alarms()

    if not alarms:
        print("\nNo alarms scheduled.")
        return

    print("\nScheduled Alarms:")
    print("-" * 40)

    for alarm in alarms:
        status = "Active" if alarm.active else "Inactive"

        print(
            f"ID: {alarm.id} | "
            f"Time: {alarm.formatted_time()} | "
            f"Label: {alarm.label or 'No Label'} | "
            f"{status}"
        )


def delete_alarm(alarm_manager: AlarmManager) -> None:
    """Handle deleting an alarm."""
    try:
        alarm_id = int(
            input("\nEnter alarm ID to delete: ").strip()
        )

        alarm_manager.delete_alarm(alarm_id)

        print("Alarm deleted successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    """Application entry point."""
    alarm_manager = AlarmManager()

    notification_service = NotificationService(
        alarm_manager
    )

    clock_service = ClockService(
        alarm_manager,
        notification_service,
    )

    while True:
        display_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_alarm(alarm_manager)

        elif choice == "2":
            list_alarms(alarm_manager)

        elif choice == "3":
            delete_alarm(alarm_manager)

        elif choice == "4":
            print(
                "\nStarting alarm monitor..."
            )
            print(
                "Press Ctrl+C to stop monitoring."
            )

            clock_service.run()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print(
                "Invalid option. Please choose "
                "a number between 1 and 5."
            )


if __name__ == "__main__":
    main()