
from function import *

print("----------------------------")
print(" BASIC PASSWORD CALCULATOR ")
print("----------------------------")

limit = int(input("Enter the max. number of charecters for password here: "))

choice = input("Do you want to use special charecters? [Y] or [N]: ").strip().upper()

if choice == "Y":
    print(generate_special(limit))

elif choice == "N":
    print(generate_no_special(limit))

else:
    print("Invalid Input!")
