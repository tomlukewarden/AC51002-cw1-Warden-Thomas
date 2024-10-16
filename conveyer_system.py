# Start daily productions


def production_start():  # function to recall the production start
    print("Good Morning")
    start = input("Would you like to start the productions for today? ")
    if (
    start == "yes" # Thinking of all valid options
    or start == "Yes"
    or start == "y"
    or start == "Y"
):
        print("Production has begun.")
    elif(
        start == 'no'
        or start == 'No'
        or start == 'n'
        or start == 'N'
    ):
        print("Production will not start.")
    else: # Error handling
        print('This is not the correct input')
        print('Please input Yes or No')

production_start()