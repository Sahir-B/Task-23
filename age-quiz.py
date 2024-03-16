# This program takes the user's age as input and provides different messages
# based on certain age ranges:

# Prompt the user to input their age and convert it to an integer
age = int(input("Enter your age: "))

# Check if the age is less than 13, print message
if age < 13:
    print("You qualify for the kiddie discount.")

# Check if the age is exactly 21, print message
elif age == 21:
    print ("Congrats on your 21st!"), 

# Check if the age is between 40 and 65 (exclusive),print message
elif 40 <= age < 65:
    print("You're over the hill")

# Check if the age is between 65 and 100 (inclusive), print message
elif 65 <= age <= 100:
    print ("Enjoy your retirement!")

# Check if the age is greater than 100, print message
elif age > 100:
     print ("Sorry, you're dead!")

# If none of the above conditions are met, print a message
else:
    print("Age is but a number")