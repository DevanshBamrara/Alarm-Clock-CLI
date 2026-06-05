# Python CLI Alarm Clock

A simple, lightweight command-line alarm clock application in Python to manage and monitor alarms in-memory without using external storage or a database.

---

## Problem Statement
Build a command-line alarm clock application in Python that allows users to create, manage, and monitor alarms. The application must support 12-hour and 24-hour formats, allow snoozing and duplicate prevention, and run without a database or file-based persistence.

---

## Requirements Discovery
During analysis, the core requirements were defined as:
* **In-Memory Storage**: No external database or file dependency.
* **Flexible Time Formats**: Accept `07:30`, `14:45`, `7:30 AM`, and `2:45 PM`.
* **Alarm Monitoring**: Continuous time check loop (seconds precision).
* **Audio Alerts**: Simple audio notification on alarm trigger using `winsound`.
* **Conflict Resolution**: Prevent scheduling multiple alarms for the exact same time.

---

## AI Usage
Artificial Intelligence was used during development for:
* **Requirement clarification**
* **Architecture discussion**
* **Code drafting**

All AI-generated code and structure were manually reviewed, verified, and modified before integration.

---

## Architecture
The application uses a simple layered architecture to separate concerns:

```text
User ──> CLI Menu (main.py) ──> Alarm Manager (alarm_manager.py)
                                     │
                                     ├── Clock Service (clock_service.py)
                                     └── Notification Service (notification_service.py)
```

* **`main.py`**: Handles CLI user interactions, menu navigation, and validates input.
* **`alarm_manager.py`**: Manages the list of active alarms in memory.
* **`clock_service.py`**: Runs the monitoring loop to check for due alarms every second.
* **`notification_service.py`**: Triggers alarm notifications, handles audio beeps, and prompts for snooze/dismissal.
* **`utils.py`**: Helpers for validation and time parsing.
* **`alarm.py`**: The Alarm data model.

---

## Design Decisions
* **In-Memory List**: Selected for simplicity and meeting the constraint of zero external storage.
* **Winsound Audio Beeps**: Utilizes Python's native `winsound.Beep` for easy, cross-platform-free alert sounds.
* **Snooze-Time Re-validation**: Ensures snoozing an alarm by 5 minutes doesn't collide with another pre-existing alarm.

---

## Tradeoffs
* **Pros**: Simple codebase, zero configuration, lightweight, and dependency-free.
* **Cons**: Alarms are lost as soon as the terminal program exits.

---

## Features
* Add alarm with an optional label.
* Automatically schedules alarms for tomorrow if the input time has already passed today.
* List all scheduled alarms sorted by time.
* Delete alarm by ID.
* continuous monitor loop with `Ctrl+C` interrupt handling.
* Alarm notification triggering 5 beep sounds.
* Snooze (5 minutes) and Dismiss actions.

---

## Folder Structure
```text
Clock CLI/
├── alarm.py                # Alarm dataclass model
├── alarm_manager.py        # Logic to add, delete, and list alarms in memory
├── clock_service.py        # Alarm checking/monitoring loop
├── notification_service.py # Audio warnings and snooze/dismiss prompts
├── utils.py                # Helper functions for parsing and validating time inputs
├── main.py                 # Application entry point and CLI menu interface
└── README.md               # Project documentation
```

---

## How To Run

### Prerequisites
* Python 3.10 or later.

### Steps
1. Navigate to the project directory:
   ```bash
   cd "Clock CLI"
   ```
2. Run the application:
   ```bash
   python main.py
   ```

---

## Testing
Only **manual testing** has been performed on the application. The following manual test scenarios were executed:
1. Adding alarms with valid formats (`07:30`, `14:45`, `7:30 AM`, `2:45 PM`).
2. Verification of duplicate time warnings when attempting to add identical times.
3. Deleting alarms and ensuring they no longer display or trigger.
4. Simulating alarm trigger: confirming audio beep triggers and the menu prompts options correctly.
5. Verification of the snooze behavior (increments time by 5 minutes) and dismiss action (makes alarm inactive).

---

## Future Improvements
* **Persistence**: Save alarms to a local `alarms.json` file to restore them on app launch.
* **Custom Sounds**: Add support for playing MP3 or WAV files instead of system beeps.
* **Configurable Snooze**: Let users choose snooze durations (e.g., 5, 10, or 15 minutes).
* **Recurring Alarms**: Support repeat settings for weekdays, weekends, or custom days.
