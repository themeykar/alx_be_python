task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        if time_bound == "yes" and priority == "high":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today! ")

    case "medium":
        if time_bound == "yes" and priority == "medium":
            print(f"Reminder: '{task}' is a {priority} priority task that requires attention when less busy! ")

    case "low":
        if time_bound == "no" and priority == "low":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")


