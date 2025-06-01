# daily_reminder.py

# Get inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize message
message = ""

# Match case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unrecognized priority level"

# Add time-bound logic
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Note" in message:
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print
