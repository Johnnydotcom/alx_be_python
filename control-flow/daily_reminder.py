task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

  
match priority:
    case "high":
        if time == "no" :
            print("Note: '" + task + "' is a high priority task. Consider completing it when you have free time.")
        else :
            print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
    case "medium":
        if time == "no" :
            print("Note: '" + task + "' is a medium priority task. Consider completing it when you have free time.")
        else :
            print("Reminder: '" + task + "' is a medium priority task that requires immediate attention today!")
    case "low":
        if time == "no" :
            print("Note: '" + task + "' is a low priority task. Consider completing it when you have free time.")
        else :
            print("Reminder: '" + task + "' is a low priority task that requires immediate attention today!")
        