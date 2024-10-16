# Start daily production
def daily_operations():
    def production_start(): 
        start = input("Good Morning! Would you like to start the production for today? ")

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
daily_operations()
