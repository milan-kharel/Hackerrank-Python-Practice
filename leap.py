def is_leap(year):
    # Initialize leap as False by default
    leap = False
    
    # Check if the year is divisible by 4 and not divisible by 100, or if it's divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # If any of the conditions are true, set leap to True
        leap = True
    
    # Return the value of leap (True if it's a leap year, False otherwise)
    return leap

# Take user input for a year and convert it to an integer
year = int(input("Enter a year: "))

# Call the is_leap function and print the result
print(is_leap(year))
