def age_program():
    seconds_or_years = input("Give me seconds (s) or years (y)? ")
    if seconds_or_years == "s":
        #convert seconds to years
        user_value = input("Enter the number of seconds you have lived for: ")
        print("'you have lived for {} years'".format(int(user_value) /60 /60/ 24/ 365))
    elif seconds_or_years == 'y':
        user_value = input("Enter the number of years you have lived for: ")
        print(" You have lived for {} seconds".format(int(user_value) * 365 * 24 * 60 * 60))
