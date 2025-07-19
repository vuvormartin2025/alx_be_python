# daily_reminder_.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")

        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")

    case "low":
        if time-bound == "yes":
            print(f"Reminder: '{task} is a low priority task, but still needs to be done today.")

        else:
            print(f"Note: '{task}' is a low priority task, but still needs to be done today.")

    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")
        