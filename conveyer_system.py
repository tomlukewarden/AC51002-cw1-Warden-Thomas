import random
import time


# Start daily production
def daily_operations():
    # Will be adding a better/more secure way to this

    # Global Variables
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
            service_item_list = []
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
                    service_item_list.append(items_per_hour)
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
                def maintenance():
                    max_hours = 4
                    service_total = 0
                    # Max hours it can handle is 4
                    if working_hours == 4:
                        service_total = sum(service_item_list)
                        print(
                            "Service Needed, maximum hours of operation has been reached"
                        )
                        print("Heres your maintenance report:")
                        print(
                            f"Over {max_hours} hours, we have produced {service_total} items."
                        )
                        # Printing service report - Will change this so it prints the sum of everything in the 4 hours instead of the total hours
                        time.sleep(3)  # Pause program for 3 seconds then return
                        service_total = 0
                    elif working_hours == 8:
                        service_total = sum(service_item_list[-4:])
                        print(
                            "Service Needed, maximum hours of operation has been reached"
                        )
                        print("Heres your maintenance report:")
                        print(
                            f"Over {max_hours} hours, we have produced {service_total} items."
                        )
                        # Printing service report - Will change this so it prints the sum of everything in the 4 hours instead of the total hours
                        time.sleep(3)  # Pause program for 3 seconds then return
                    else:
                        pass
                    with open("./files/service_report.txt", "w") as service_file:
                        service_file.write(
                            f"Over {max_hours} hours, we have produced {service_item_list[-4:]} items.\n"
                        )

                maintenance()
    else:
        print("Daily productions have not started yet")

    def end_of_day():
        # Opening text file to collect final report
        with open("./files/hours.txt", "r") as hours_file:
            lines = (
                hours_file.readlines()
            )  # Using readlines() method to produce a list of all items in txt file
            total_hours_items = lines[-1]  # Access the last line (final hour and item)
        with open("./files/end_of_day.txt", "w") as eod_file:
            eod_file.write(f"{name}\n")
            eod_file.write(f"{date}\n")
            eod_file.write(f"{total_hours_items}\n")
            # Want to collect all data from the day and store it in a text file with the date and be able to retrieve this at the start of the next day
            end = input("Are you ready to perform the end of day tasks? ")
            if end.lower() in ["yes", "y"]:
                print("Great, here is your final Report: ")
                print(f"Operator Name: {name}")
                print(f"Date: {date}")
                print(total_hours_items)
    end_of_day()
    def next_day():
                    user_confirmation = input('Would you like to continue to the next day?')
                    if user_confirmation.lower() in ["yes", "y"]:
                        print("Okay! Please input your details to start production")
                        return daily_operations()
                    elif user_confirmation.lower() in ["no", "n"]:
                        print("Okay! Our Operational System will now close.")
                    else:  
                        print("This is not the correct input.")
                        print("Please input Yes or No.")
                        return next_day()
daily_operations()
