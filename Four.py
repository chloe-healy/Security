'''
The purpose of this script is to implement a system that will prevent fast
guessing of the PIN.

This is implemented by making the the hash function more computationally
expensive. 
- Recursive hash function.

As the previosu question, it has been tested on 3, 4, and 5-digit PINs.
Their results have been recorded and a graph plotted, to allow analysis
of the results and also comparison in time values from the previous question.
'''

import hashlib
import datetime


# Define the user the pin
s_user = "ch42"
# s_pin = "526377"
# p = hashlib.md5(s_pin.encode('utf-8')).hexdigest()
# print(p)
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
    # h = HMD5(HMD5(...HMD5(P IN)))
    h = hashlib.md5()
    h.update(s.encode('utf-8'))
    h = h.hexdigest()
    return h

def mulHash(s,m):
    '''This funtion will implement the recursion of the getHash function.
    It will call the getHash function multiple times and apply it to the 
    same PIN'''
    h = s
    for x in range(0,m):
        h = getHash(h)
    return h

# ask for username and password
# can remove the need to have the user input the username when brute 
# forcing the password 
user = input("user: ")
# pin = getpass.getpass("PIN : ") # No longer required when brute frorcing

# Rountinly try to insert all password combinations for up to 6 digit pins.
start = datetime.datetime.now()
for x1 in range(0,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                for x5 in range(0,10):
                    pin = str(x1) + str(x2) + str(x3) #+ str(x4) #+ str(x5)
                    # Change to the mulHash function.
                    # mulHash takes the pin and also the number of iterations
                    # as input.
                    # in this case we want to recursively call getHash 
                    # 1000 times.
                    hash = mulHash(pin, 1000)
                    # check if the user can log in successfully
                    if login(user, getHash(pin)):
                        stop = datetime.datetime.now()
                        print("Access Granted")
                        print("PIN match: " + pin)
                        time = millis_interval(start,stop)
                        print("Time to exec code: " +time)
                        quit()
                    

                print("Access Denied")

# Storing the results for plotting purposes 
digits = ["3", "4" "5"]
results = ["60978.004", "62611.312", "60996.569"]

# Refer to plot.py
# This is so we can see the comparison of the two graphs presented together.