import os
import random
import secrets
import string

user = input("what program would you like to use?\n type 1 for the password generator, type 2 for the passphrase generator: ")
def passwordgen():
    #Password generator
    #importing modules

    while True:
        print('\nWelcome to my password generator! \nStill in its testing phase!')#here we ask for the length of the password.
    #here we ask for the length of the password.
        segments = int(input("\nHow many segments would you like?  "))
        characters = int(input('\nhow many characters in each segment?  ')) 
    #we define the variables for ease of access
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        password = []
        for i in range(segments):
            password.append(''.join(random.choice(upper + num + lower)for _ in range(characters)))
        #temp = ''.join(secrets.choice(all)for i in range (characters))

        #password = ''.join(temp)

        print ("your password has been generated: " + '-'.join(password))
        ans = input("Would you like to generate another? key y/n: ")

        if ans not in ("y", "n"):
            print("invalid input")
            break

        elif ans == 'y':
            continue

        else:
            input("\nPress the enter key to exit")
            break  
    #we define the variables for ease of access
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        temp = ''.join(secrets.choice(all)for _ in range(length))

        password = ''.join(temp)

        print (password)

        ans = input("Would you like to generate another? key y/n: ")

        if ans == "y" or ans == "yes":
            continue
        elif ans == "n" or ans == "no":
            print("Goodbye!")
            break
        else:
            print("invalid input")
            break


def passphrasegen():

    while True:
        file = open("wordlist.txt", "r")
        content = file.read()
        wordlist = content.split()
        file.close()
        length = int(input("how many words would you like in your pass phrase?"))
        passphrase = ("-".join(random.choices(wordlist, k = length)))
        print("your passphrase has been generated. It is: " + passphrase)

        ans = input("would you like another passphrase? key Y/n ")

        if ans == 'y' or ans == 'yes':
            continue
   
        elif ans == 'n' or ans == 'no':
            print("goodbye!")
            break

        else:
            print("invalid input")
            break

if user == "1":
    passwordgen()

if user == "2":
    passphrasegen()

    input()