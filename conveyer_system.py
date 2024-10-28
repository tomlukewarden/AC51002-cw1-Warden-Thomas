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
        # Restart the process if the name is not recognized
        daily_operations()
    
    # Input the current day of the week
    day = input("What is the day today?: ")
    if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        print("Please input the correct day of the week")
        # Restart the process if the day is invalid
        daily_operations()
    else:
        print("Day has been set")

    # Read and display yesterday's report
    with open("./files/end_of_day.txt", "r") as eod_file:
        prev_report = eod_file.read()
        print(f"Here's yesterday's report: {prev_report}")
    def production_start():
# Function to prompt the operator to start production.
        start = input(f"Welcome Back {name}! Would you like to start the production for today? (Yes/No) \n ")
        if start.lower() in ["yes", "y"]:
            print("Production has begun.")
            return True
        elif start.lower() in ["no", "n"]:
            print("Production will not start.")
            return False
        else:
            print("This is not the correct input. Please input Yes or No.")
            return production_start()

    if production_start():
        working_hours = 0
        total_items_produced = 0
        service_item_list = []
        for hour in range(9, 18):

        # Simulate production for each hour
            if hour < 17:
                working_hours += 1
                items_per_hour = random.randrange(75, 100)
                total_items_produced += items_per_hour
                service_item_list.append(items_per_hour)
                print(f"Hour {working_hours} produced {items_per_hour} items \n")
                time.sleep(3)
                
            # Perform maintenance if necessary
            def maintenance():
                if working_hours % 4 == 0:
                    print("Service Needed, maximum hours of operation has been reached")
                    print("Here's your maintenance report:")
                    
                    # Calculate items produced in the last 4 hours
                    print(f"Over the last 4 hours, we produced {sum(service_item_list[-4:])} items.")
                    
                    
                    # Write the maintenance report to a file
                    with open("./files/service_report.txt", "w") as service_file:
                        service_file.write(f"Over 4 hours, we have produced {sum(service_item_list[-4:])} items.\n")
                    
                    # Simulate maintenance time
                    print("Shutting down for maintenance...")
                    time.sleep(10)
                    print("Maintenance has been completed")
                    print("Resuming production...")
            maintenance_performed = True
            # Reset the maintenance flag after 4-hour block has completed
            if working_hours % 4 == 0 and maintenance_performed:
                maintenance_performed = False
            maintenance()
    
    else:
        print("Daily productions have not started yet")

    def storeData():
        selected_operator.hours_worked += working_hours
        selected_operator.items_produced += total_items_produced

        file_path = f"./files/operators/{selected_operator.name.lower()}_data.txt"
        with open(file_path, "a") as operator_file:
            operator_file.write(f'{day}: Hours Worked: {selected_operator.hours_worked}, Items Produced: {selected_operator.items_produced},\n')
        print("Data has been stored successfully!")
            
    def end_of_day():
        # Read the total operating hours and items produced from the hours file
        with open("./files/hours.txt", "r") as hours_file:
            lines = hours_file.readlines()
            total_hours_items = lines[-1]  # Access the last line (final hour and item)

        # Write the end-of-day summary to a file
        with open("./files/end_of_day.txt", "w") as eod_file:
            eod_file.write(f"{name}\n")
            eod_file.write(f"{day}\n")
            eod_file.write(f"{total_hours_items}\n")

        # Prompt the operator to perform end-of-day tasks
        end = input(f"Good afternoon {name}! Are you ready to perform the end of day tasks? ")
        if end.lower() in ["yes", "y"]:
            print("Great, here is your final Report: ")
            print(f"Operator Name: {name}")
            print(f"Date: {day}")
            print(total_hours_items)
            storeData()  # Store the operator's data
            print("Thanks for using our software!") 
        else:
            print("Okay, please come back when you are ready")
    end_of_day()

daily_operations()


next_day = input("Are you happy to move on to the next daily operations? ")
if next_day.lower() in ["yes", "y"]:
    daily_operations()
else:
    exit()

