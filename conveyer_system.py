import random
import time


# Start daily production
def daily_operations():
    # Will be adding a better/more secure way to this
    name = input("Enter your Name ")
    date = input("Enter the Date ")
    # Showing yesterdays end of day report
    with open("./files/end_of_day.txt", "r") as eod_file:
        prev_report = eod_file.read()
        # Printing report
        print(f"Here's yesterdays report: {prev_report}")
    # Function of the start of productions
    def production_start():
        start = input(
            "Welcome Back! Would you like to start the production for today? "
        )
        # Check for valid start responses
        if start.lower() in ["yes", "y"]:
            print("Production has begun.")
            return True
        elif start.lower() in ["no", "n"]:
            print("Production will not start.")
            return False
        else:  # Error handling
            print("This is not the correct input.")
            print("Please input Yes or No.")
            return production_start()

    # If statement to show that the productions are working
    if production_start():
        # Working hours logic to add to text file
        with open("./files/hours.txt", "w") as hours_file:
            working_hours = 0
            items_per_hour = 0
            total_items_produced = 0
            for hour in range(9, 18):
                # Maximum number of items produced an hour will be 100 items
                if hour < 17:
                    # Working hours increase by 1 each loop round
                    working_hours += 1
                    items_per_hour = random.randrange(
                        75, 100
                    )  # Items increase by a random number between 75 and 100
                    total_items_produced += (
                        items_per_hour  # Total of Items updates every hour
                    )
                    print(f"Hour {working_hours} produced {items_per_hour} items \n")
                    time.sleep(3)
                # Adding these to the text file
                hours_file.write(f"Total Operating Hours: {working_hours}\n")
                hours_file.write(
                    f"Hour {working_hours} produced {items_per_hour} items \n"
                )
                hours_file.write(
                    f"In {working_hours} hours of Operation, DundeeZest Conveyer Belt produced {total_items_produced} items"
                )
                # Using function so it can be recalled if needed
                def maintenance(working_hours):
                    # Max hours it can handle is 4
                    if working_hours == 4 or working_hours == 8:
                        print('Service Needed, maximum hours of operation has been reached')
                        print('Heres your maintenance report:')
                        print(f"Total Operating Hours: {working_hours} & Total Items produced: {total_items_produced} \n")
                        time.sleep(3) # Pause program for 3 seconds then return
                    with open('./files/service_report.txt', 'w') as service_file:
                            service_file.write(f"Total Operating Hours: {working_hours} & Total Items produced: {total_items_produced} \n")
                maintenance(working_hours)
    else:
        print("Daily productions have not started yet")

    def end_of_day():
        # Opening text file to collect final report
        with open("./files/hours.txt", "r") as hours_file:
            lines = hours_file.readlines()
            total_hours_items = lines[-1]  # Access the last line (final hour and item)
        with open("./files/end_of_day.txt", "w") as eod_file:
            eod_file.write(f"{name}\n")
            eod_file.write(f"{date}\n")
            eod_file.write(f"{total_hours_items}\n")
            # Want to collect all data from the day and store it in a text file with the date and be able to retrieve this at the start of the next day
            end = input("Are you ready to perform the end of day tasks? ")
            if end.lower() in ["yes", "y"]:
                print("Great, here is your final Report: ")
                print(f'Operator Name: {name}')
                print(f'Date: {date}')
                print(total_hours_items)
            else:
                print("Okay, please come back when you are ready ")

    end_of_day()


daily_operations()
