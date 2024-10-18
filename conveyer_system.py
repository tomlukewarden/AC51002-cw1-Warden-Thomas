# Start daily production
def daily_operations():
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
            for hour in range(9, 18):

                if hour < 17:
                    working_hours += 1
                hours_file.write(f"Total Operating Hours: {working_hours}\n")
    else:
        print("Daily productions have not started yet")

    def end_of_day():
        with open('./files/hours.txt', 'r') as hours_file:
            lines = hours_file.readlines()
            total_hours = lines[-1]  # Access the last line (final hour)
        # Want to collect all data from the day and store it in a text file with the date and be able to retrieve this at the start of the next day
            end = input("Are you ready to perform the end of day tasks? ")
            if end.lower() in ["yes", "y"]:
                print("Great, here is your final Report: ")
                print('The Date')
                print(total_hours)
                print('Number of Items produced')
                print('Your name')
                exit()
            else:
                print("Okay, please come back when you are ready ")
    end_of_day()


daily_operations()
