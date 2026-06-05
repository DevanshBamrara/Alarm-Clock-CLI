from datetime import datetime


def parse_alarm_time(time_str: str) -> datetime:
    """
    Parse a user-provided alarm time into a datetime object.

    Supported formats:
        07:30
        14:45
        7:30 AM
        2:45 PM

    Returns:
        datetime: Alarm time scheduled for today.

    Raises:
        ValueError: If the input format is invalid.
    """
    time_str = time_str.strip()

    supported_formats = [
        "%H:%M",      # 24-hour format
        "%I:%M %p",   # 12-hour format
    ]

    parsed_time = None

    for time_format in supported_formats:
        try:
            parsed_time = datetime.strptime(time_str, time_format)
            break
        except ValueError:
            continue

    if parsed_time is None:
        raise ValueError(
            "Invalid time format. Use '07:30', '14:45', '7:30 AM', or '2:45 PM'."
        )

    now = datetime.now()

    return datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=parsed_time.hour,
        minute=parsed_time.minute,
    )


def validate_alarm_time(time_str: str) -> bool:
    """
    Validate whether a time string is supported.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        parse_alarm_time(time_str)
        return True
    except ValueError:
        return False