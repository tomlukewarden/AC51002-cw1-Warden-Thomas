# Start daily production
def daily_operations():
    def production_start(): 
        time = int(input('What time is it? '))
        
        if time >= 9 and time <= 17:
            # name = input('Enter your name to set up the productions ')
            start = input("Welcome Back! Would you like to start the production for today? ")
        else:
            print('It is not the correct time to start these productions, please come back between 9am and 5pm')
            exit()
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
        

'''
    

index 10 = 9am
index 11 = 10am
index 12 = 11am
index 13 = 12pm
index 14 = 1pm
index 15 = 2pm
index 16 = 3pm
index 17 = 4pm
index 18 = 5pm
'''
daily_operations()
