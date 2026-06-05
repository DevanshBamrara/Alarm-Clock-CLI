# Python CLI Alarm Clock

## Problem Statement

Build a command-line alarm clock application in Python that allows users to create, manage, and monitor alarms without using a database or external storage.

The application should:

* Support both 12-hour and 24-hour time formats.
* Allow users to add, list, and delete alarms.
* Monitor alarms continuously.
* Notify users when alarms become due.
* Support snoozing alarms.
* Prevent duplicate alarm times.
* Keep all data in memory during execution.

The goal of the project is to demonstrate clean software design, input validation, object-oriented programming principles, and separation of concerns within a small CLI application.

---

# Requirements Discovery

The project requirements were intentionally open-ended and were refined through analysis and discussion.

The following decisions were made during requirements discovery:

### Core Requirements

* Add alarms
* List alarms
* Delete alarms
* Run alarm monitoring loop
* Trigger alarms
* Snooze alarms
* Support 12-hour and 24-hour input formats

### Clarifications

#### Time Format Support

Accepted formats:

```text
07:30
14:45
7:30 AM
2:45 PM
```

All times are converted internally into Python `datetime` objects.

#### Duplicate Alarm Handling

Only one alarm may exist for a specific trigger time.

Example:

```text
07:30
07:30
```

The second alarm is rejected.

#### Storage

No database.

No file storage.

Alarms exist only while the application is running.

---

# AI Usage

Artificial Intelligence was used during the development process for:

* Requirement clarification
* Product and architecture discussions
* Edge case identification
* Initial code drafting
* Design review

All AI-generated content was:

* Reviewed manually
* Validated before implementation
* Modified where necessary
* Integrated by the developer

The final design decisions and implementation remain the responsibility of the developer.

---

# Architecture

The application follows a simple layered architecture.

```text
User
 │
 ▼
CLI Interface
 │
 ▼
Alarm Manager
 │
 ├── Alarm Model
 │
 └── Clock Service
          │
          ▼
Notification Service
```

---

# Components

## Alarm Model

Represents an individual alarm.

Responsibilities:

* Store alarm information
* Store alarm state
* Format alarm time for display

---

## Alarm Manager

Responsible for alarm management.

Responsibilities:

* Add alarms
* Delete alarms
* List alarms
* Detect duplicates
* Find due alarms

---

## Clock Service

Responsible for alarm monitoring.

Responsibilities:

* Run monitoring loop
* Check alarms every second
* Trigger due alarms

---

## Notification Service

Responsible for alarm interaction.

Responsibilities:

* Display alarm information
* Snooze alarms
* Dismiss alarms
* Prevent snooze conflicts

---

## CLI Interface

Responsible for user interaction.

Responsibilities:

* Display menu
* Read commands
* Validate user input
* Call services

---

# Design Decisions

## In-Memory Storage

All alarms are stored in memory.

Reason:

* Simpler implementation
* Meets project requirements
* No persistence complexity

---

## Duplicate Prevention

Alarm times must be unique.

Reason:

* Simplifies alarm management
* Avoids confusing user experience
* Simplifies snooze handling

---

## Datetime-Based Storage

All alarm times are stored as Python `datetime` objects.

Reason:

* Simplifies time comparison
* Supports AM/PM conversion
* Handles date rollover naturally

---

## Separation of Concerns

Each file has a single responsibility.

Reason:

* Easier maintenance
* Easier testing
* Better readability

---

# Tradeoffs

## No Persistent Storage

### Pros

* Simpler implementation
* No database required

### Cons

* Alarms are lost when the application exits

---

## Duplicate Alarm Restriction

### Pros

* Predictable behavior
* Simpler logic

### Cons

* Users cannot create multiple alarms for the same time

---

## CLI-Only Interface

### Pros

* Lightweight
* Easy to implement

### Cons

* No graphical interface
* Limited user experience

---

# Features

### Supported Features

* Add alarm
* List alarms
* Delete alarm
* Alarm monitoring loop
* Alarm notifications
* Snooze alarm
* Dismiss alarm
* Duplicate prevention
* 12-hour time input
* 24-hour time input
* Input validation

---

# Folder Structure

```text
project/
│
├── alarm.py
├── alarm_manager.py
├── clock_service.py
├── notification_service.py
├── utils.py
├── main.py
└── README.md
```

---

# File Responsibilities

## alarm.py

Contains the `Alarm` dataclass.

---

## alarm_manager.py

Manages alarms stored in memory.

---

## clock_service.py

Runs the monitoring loop.

---

## notification_service.py

Handles alarm notifications and snoozing.

---

## utils.py

Contains time parsing and validation helpers.

---

## main.py

Application entry point and CLI menu.

---

# How To Run

## Prerequisites

Python 3.10 or later recommended.

Verify installation:

```bash
python --version
```

---

## Run Application

Navigate to the project directory:

```bash
cd project
```

Run:

```bash
python main.py
```

---

## Menu

```text
1. Add Alarm
2. List Alarms
3. Delete Alarm
4. Start Alarm Monitor
5. Exit
```

---

# Example Usage

## Add Alarm

```text
Enter alarm time: 7:30 AM
Enter label: Morning Alarm
```

---

## List Alarms

```text
ID: 1 | Time: 07:30 | Label: Morning Alarm
```

---

## Start Monitoring

```text
Starting alarm monitor...
Press Ctrl+C to stop monitoring.
```

---

## Alarm Trigger

```text
========================================
ALARM!
Label : Morning Alarm
Time  : 07:30
========================================

1. Snooze 5 minutes
2. Dismiss
```

---

# Testing

The following scenarios should be tested.

## Valid Time Formats

```text
07:30
14:45
7:30 AM
2:45 PM
```

Expected:

```text
Alarm created successfully
```

---

## Invalid Time Format

```text
25:61
hello
13:00 PM
```

Expected:

```text
Invalid time format
```

---

## Duplicate Alarm

Create:

```text
07:30
```

Attempt:

```text
07:30
```

Expected:

```text
Alarm already exists
```

---

## Delete Alarm

Delete an existing alarm.

Expected:

```text
Alarm deleted successfully
```

---

## Snooze Alarm

Trigger an alarm and select:

```text
1
```

Expected:

```text
Alarm snoozed until HH:MM
```

---

## Snooze Conflict

If snoozing creates a duplicate time.

Expected:

```text
Cannot snooze. Alarm already exists.
```

---

## Dismiss Alarm

Select:

```text
2
```

Expected:

```text
Alarm dismissed
```

---

# Future Improvements

Potential future enhancements include:

## Persistence

* Save alarms to JSON
* Restore alarms on startup

---

## Recurring Alarms

Support:

```text
Daily
Weekdays
Weekends
Custom schedules
```

---

## Multiple Snooze Options

Support:

```text
5 minutes
10 minutes
15 minutes
30 minutes
```

---

## Sound Notifications

* WAV file support
* MP3 support
* Custom alarm sounds

---

## Configuration System

Allow users to configure:

* Default snooze duration
* Time format preference
* Notification settings

---

## Automated Testing

Add:

* Unit tests
* Integration tests
* CI pipeline

---

## GUI Version

Possible future desktop application using:

* Tkinter
* PyQt
* CustomTkinter

---

# Conclusion

This project demonstrates the design and implementation of a simple but well-structured Python CLI alarm clock application. The solution focuses on clean architecture, input validation, separation of concerns, and maintainable code while remaining intentionally lightweight and easy to understand.
