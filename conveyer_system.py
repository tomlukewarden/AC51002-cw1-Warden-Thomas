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
        
# Working hours are 9-5, Need to use accumulator 
    for i in range(1,10):
        print(i)   
'''
1 = 9am
2 = 10am
3 = 11am
4 = 12pm
5 = 1pm
6 = 2pm
7 = 3pm
8 = 4pm
9 = 5pm
'''
daily_operations()
