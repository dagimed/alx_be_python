# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Respond based on priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unrecognized priority level"

# Add time-bound urgency if applicable
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Note" not in message:
        message += " you should plan to complete it soon."
    else:
        message += ". Consider completing it when you have free time."

# Output the reminder
print("\n" + message)
