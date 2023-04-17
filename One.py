'''
Part One of the project.
- The initial system consists of a single user and pin.
- Check to see if you can run the code and log in successfully
'''

import getpass

# Define the user the pin
s_user = "ch42"
s_pin = "5263"

def login(user, pin):
    '''Function to check if the user and password match.'''
    if user == s_user and s_pin == pin:
        print("user/PIN : " + user + "/" + pin)
        return True
    return False

# Ask for the user name and PIN
user = input("user: ")
pin = getpass.getpass("PIN : ")

# Check if you can log in
if login(user,pin):
    print("Access Granted")
else:
    print("Access Denied")