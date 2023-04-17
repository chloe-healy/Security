'''
Part Three of the Project
Find how long it takes to get all possible combinations of:
- 3 digit pin
- 4 digit pin
- 5 digit pin 
Plot the results and look at the difference between values
'''

import getpass
import hashlib

# Set the username and hash value of the password.
s_user = "ch42"
# First print the hash of the password so it can be stored as a variable.
#s_pin = "5263"
#p = hashlib.md5(s_pin.encode('utf-8')).hexdigest()
#print(p)
s_hash = "cc638784cf213986ec75983a4aa08cdb"


def login(user, hash):
    '''Function to check if the user and password match.'''
    if user == s_user and s_hash == hash:
        #print(hash)
        print("user/hash : " + user + "/" + hash)
        return True
    return False

def getHash(s):
    '''Function to create the hash of the provided PIN'''
    h = hashlib.md5()
    h.update(s.encode('utf-8'))
    h = h.hexdigest()
    return h

# Ask for the user name and PIN
user = input("user: ")
pin = getpass.getpass("PIN : ")

# Check if you can log in - check the hash matches the stored hash
if login(user, getHash(pin)):
    print("Access Granted")   
else:
    print("Access Denied")



