"""
Author= Sahil
"""

def username():
    studentID = input("Enter the student ID: ")
    First_name = input("Enter the First name: ")
    Last_name = input("Enter the last name: ")
    University = input("What is the name of your university: ")

    if "Whitecliffe" in University and "COLLEGE" in University:
        generated_username = studentID[0:2] + Last_name[0:3]
        print(f"Welcome to Whitecliffe College. Your username is {generated_username}.")
    else:
        print("Please enter a valid university to generate your username.")

def main():
    username()

main()
