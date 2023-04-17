#%%
'''
This script implement a brute force situation.
All possible combinations of the PIN are tested until a match os found.
Digits contained in the pin can be from [0-9]
Once a match is found Access is Granted and the program exists, providing the
user with their username and their PIN match value.

This has been tested on 3, 4 and 5 digit PINs, their results were recorded 
and presented as a plot in which it could be seen the relationship between the 
number of digits and the time taken to execute. 

'''

import hashlib
import datetime


# Define the user the pin
s_user = "ch42"
#s_pin = "5263"
#p = hashlib.md5(s_pin.encode('utf-8')).hexdigest()
#print(p)
s_hash3 = "85422afb467e9456013a2a51d4dff702"
s_hash4 = "cc638784cf213986ec75983a4aa08cdb"
s_hash5 = "c9b49ca561a1f728f02c136e2f987c0b"
s_hash6 = "3eac0f0fc2bc5910ed66baf0b05ed5dd"
# s_hash represents the hashed pin


def millis_interval(start,end):
    '''Function which calculates the time it takes to check combinations'''
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return str(millis)



def login(user, hash):
    '''Function to check if the user and password match.'''
    if user == s_user and s_hash3 == hash:
        print("user/hash : " + user + "/" + hash)
        return True
    elif user == s_user and s_hash4 == hash:
        print("user/hash : " + user + "/" + hash)
        return True
    elif user == s_user and s_hash5 == hash:
        print("user/hash : " + user + "/" + hash)
        return True
    elif user == s_user and s_hash6 == hash:
        print("user/hash : " + user + "/" + hash)
        return True
    else:
        return False


def getHash(s):
    h = hashlib.md5()
    h.update(s.encode('utf-8'))
    h = h.hexdigest()
    return h

# ask for username and password
# can remove the need to have the user input the username when brute 
# forcing the password 
user = "ch42"
# pin = getpass.getpass("PIN : ") # No longer required when brute frorcing

# Rountinly try to insert all password combinations for up to 4 digit pins.
start = datetime.datetime.now()
for x1 in range(0,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                for x5 in range(0,10):
                    for x6 in range(0,10):
                        pin = str(x1) + str(x2) + str(x3) + str(x4) + str(x5) + str(x6)
                        hash = getHash(pin)
                        # check if the user can log in successfully
                        if login(user, getHash(pin)):
                            stop = datetime.datetime.now()
                            print("Access Granted")
                            print("PIN match: " + pin)
                            time = millis_interval(start,stop)
                            print("Time to exec code: " +time)
                            quit()
                    

                    print("Access Denied")
                
# Refer to plot.py for plotting results.
digits = ["3", "4", "5", "6"]
results = ["9577.917","10922.75" ,"9906.144", "9954.801"]




# %%
