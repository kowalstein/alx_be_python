# This script provides a customized reminder for task based on user input

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
# user input

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: {task} is a high priority task that does not require immediate attention today")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task.")
        elif time_bound == "no":
            print(f"Reminder: {task} is a medium priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task.")
        elif time_bound == "no":
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case other:
        print("Invalid selection")