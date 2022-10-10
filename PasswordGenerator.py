import random



'''

3 types of password:

weak - 5-7 chars, pure letters
medium - 8-12 chars, letters, numbers
strong - 12- 20 chars, letters, numbers, symbols

'''

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
numbers = "1234567890"
symbols = r"!@#$%^&*()[]{};'\:|,.?<>?"

#print(upper)
#print(lower)
#print(symbols)
#print(numbers)

def generateWeak():

    masterList:str= (upper+lower)
    generated_pass =""
    length = random.randint(5,7)
    print(length)

    for i in range(length):
        generated_pass += random.choice(masterList)
    return generated_pass

    return generateWeak()

def generateMedium():

    masterList = (upper+lower)
    generated_pass =""
    length = random.randint(8,12)
    print(length)

    for i in range(length):
        generated_pass += random.choice(masterList)
    return generated_pass

    for i in range(5):
        return(generateMedium())


def generateStrong():

    masterList = upper+lower+numbers+symbols
    generated_pass =""
    length = random.randint(15,20)
    print(length)

    for i in range(length):
        generated_pass += random.choice(masterList)
    return generated_pass
    for i in range(12):

        return(generateStrong())



'''
Welcome to Password Manager
What would you like to to do?:

1. Generate password
2. Show Generated Passwords - Database SQLite3
3. Delete Generated password
4.Exit

'''
'''
For what application will you use your password?
>>> Google Account
1. Weak
2. Medium
3. Strong
>>> 3

Save Password for Google Account
'''


'''2.
Saved Passwords:








'''
