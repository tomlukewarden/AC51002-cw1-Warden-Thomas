import random
import time
from staff import StaffData


# Start daily production
def daily_operations():
    # Input the operator's name
    name = input("Enter your Name: ")

    # Define available operators with initial data
    operators = {
        "Obi": StaffData("Obi", 1000, 0, 0),
        "Arlo": StaffData("Arlo", 1001, 0, 0),
        "Lego": StaffData("Lego", 1002, 0, 0),
        "Emma": StaffData("Emma", 1003, 0, 0),
    }

    # Fetch the selected operator based on input name
    selected_operator = operators.get(name)
    if selected_operator:
        print("This is the correct Operator Name")
    else:
        print("Operator Name is not recognized, please try again")
        daily_operations()  # Restart the process if the name is not recognized
        return  # Exit the current function call to prevent further execution

    # Input the current day of the week
    day = input("What is the day today?: ")
    if day.lower() not in [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]:
        print("Please input the correct day of the week")
        daily_operations()  # Restart the process if the day is invalid
        return  # Exit the current function call to prevent further execution
    else:
        print("Day has been set")

    # Read and display yesterday's report
    try:
        with open("./files/end_of_day.txt", "r") as eod_file:
            prev_report = eod_file.read()
            print(f"Here's the previous report: {prev_report}")
    except FileNotFoundError:
        print("ERROR: No previous report found.")

    # Function to prompt the operator to start production
    def production_start():
        start = input(
            f"Welcome Back {name}! Would you like to start the production for today? (Yes/No): "
        ).lower()
        if start in ["yes", "y"]:
            print("Production has begun. \n")
            return True
        elif start in ["no", "n"]:
            print("Please begin production when you are ready.")
            return False
        else:
            print("ERROR:This is not the correct input. Please input Yes or No.")
            return production_start()

    # Start the production process if the operator confirms
    if production_start():
        # Define hours, items produced, and service item list
        working_hours = 0
        total_items_produced = 0
        service_item_list = []
        # These reset each day

        # Loop through each hour of the day
        for hour in range(9, 18):
            if hour < 17:
                # Simulate production for each hour
                working_hours += 1
                items_per_hour = random.randrange(75, 100)
                total_items_produced += items_per_hour
                service_item_list.append(items_per_hour)

                print(f"Hour {working_hours} produced {items_per_hour} items.")
                time.sleep(3)  # Simulate time between productions

                # Perform maintenance every 4 hours
                if working_hours % 4 == 0:
                    perform_maintenance(service_item_list)

        # Store the production data
        store_data(selected_operator, day, working_hours, total_items_produced)
        
        # End-of-day tasks
        end_of_day(name, day, selected_operator)

    else:
        production_start()


def perform_maintenance(service_item_list):
    print(
        "\n WARNING: Service Needed, maximum hours of operation has been reached :WARNING"
    )
    # Display the total number of items produced in the last 4 hours
    print("Here's your maintenance report:")
    print(f"Over the last 4 hours, we produced {sum(service_item_list[-4:])} items.\n")

    # Write this to the text file
    with open("./files/service_report.txt", "w") as service_file:
        service_file.write(
            f"Over 4 hours, we have produced {sum(service_item_list[-4:])} items.\n"
        )

    # Simulate maintenance
    print("Shutting down for maintenance in 10 seconds...")
    time.sleep(10)
    print("Maintenance has been completed.")
    print("Resuming production in 3 seconds...\n")
    time.sleep(1)
    print("Resuming production in 2 seconds...\n")
    time.sleep(1)
    print("Resuming production in 1 second...\n")
    time.sleep(1)
    print("Production has resumed.\n")


# Store the production data of each operator
def store_data(operator, day, hours_worked, items_produced):
    # Update the operator's accumulated values
    operator.hours_worked += hours_worked
    operator.items_produced += items_produced

    # Create the file path using the operator's name in lowercase
    file_path = f"./files/operators/{operator.name.lower()}_data.txt"

    # Append the current day's work to the file
    with open(file_path, "a") as operator_file:
        operator_file.write(
            f"{day}: Hours Worked: {hours_worked}, Items Produced: {items_produced}\n"
        )
        print("Data has been stored successfully!\n")

    # Re-read the file to calculate total hours worked and items produced
    total_hours = 0
    total_items = 0
    with open(file_path, "r") as operator_file:
        for line in operator_file:
            try:
                # Extract the hours and items data from each line
                hours = int(line.split("Hours Worked: ")[1].split(",")[0].strip())
                items = int(line.split("Items Produced: ")[1].strip())
                total_hours += hours
                total_items += items
            except (IndexError, ValueError):
                print("Skipping malformed line:", line.strip())
        if total_hours % 16 == 0:
            with open(file_path, "a") as operator_file:
                operator_file.write(f"Total Hours Worked: {total_hours}\n")
                operator_file.write(f"Total Items Produced: {total_items}\n")
        else:
            pass
# End-of-day 'tasks'
def end_of_day(name, day, operator):
    try:
        with open("./files/hours.txt", "r") as hours_file:
            # Read the last line of the file and create a list with the content
            lines = hours_file.readlines()
            # Find the final line of the file
            total_hours_items = lines[-1] if lines else "No data available."
    except FileNotFoundError:  # Error handling
        total_hours_items = "ERROR: No data available."

    # Write the end of day data to the text file
    with open("./files/end_of_day.txt", "w") as eod_file:
        eod_file.write(f"{name}\n")
        eod_file.write(f"{day}\n")
        eod_file.write(f"{total_hours_items}\n")

    end = input(
        f"Good afternoon {name}! Thank you for your work today. Would you like to perform end-of-day tasks? (Yes/No): "
    ).lower()
    if end in ["yes", "y"]:
        # Print the end of day report
        print("Great, here is your final Report:\n")
        print(f"Operator Name: {name}")
        print(f"Operator ID: {operator.staff_id}")
        print(f"Day: {day}")
        print(total_hours_items)
        print("Thanks for using our software!\n")
        next_day()
    elif end in ["no", "n"]:
        print("Software paused...")
        end_of_day(name, day, operator)
    else:
        print("ERROR: This is not the correct input. Please input Yes or No.")
        end_of_day(name, day, operator)


# Prompt for next day
def next_day():
    next_day_prod = input(
        "Are you happy to move on to the next daily operations? (Yes/No): "
    ).lower()
    if next_day_prod in ["yes", "y"]:
        daily_operations()
        return True
    elif next_day_prod in ["no", "n"]:
        print("Exiting software...")
        exit()
        return False
    else:
        print("ERROR: This is not the correct input. Please input Yes or No.")
        next_day()


# Start the operations
daily_operations()

while next_day():
    daily_operations()