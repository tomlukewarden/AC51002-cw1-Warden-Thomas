# Start daily productions

production_start = input("Would you like to start the productions for today? ")

if (
    production_start == "yes"
    or production_start == "Yes"
    or production_start == "y"
    or production_start == "Y"
):
    print("Production has begun.")
else:
    print("Production will not start.")
