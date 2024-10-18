# Start daily production
def daily_operations():
    def production_start(): 
            start = input("Welcome Back! Would you like to start the production for today? ")
            
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
    
    if production_start():
        print('Executing daily productions')
    else:
        print('Daily productions have not started yet')
        
        working_hours = 0
        for hour in range(9, 18):
            print(f"{hour}am, Total working hours so far: {working_hours}")
        if hour < 17: 
            working_hours += 1
        print(f"Total working hours: {working_hours}")
        
    def end_of_day():
        # Want to collect all data from the day and store it in a text file with the date and be able to retrieve this at the start of the next day
        end = input('Are you ready to perform the end of day tasks? ')
        if end.lower() in ["yes", "y"]:
            print('Great, here is your final Report! See you tomorrow!')
            exit()
        else:
            print("Okay, please come back when you are ready ")
    end_of_day()
daily_operations()
