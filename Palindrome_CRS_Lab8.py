#Christopher Robles Serrano
#Module 8 Lab 8
#11/24/2024
#This program check if the user submitted string is a palidrome. It ignores special characters and case sensitivity.


def is_palindrome():
    #Getting user's string.
    userString = input("Enter a word to check if its a palidrome: ")
    
    #Converting valid characters from user input into a list of strings.
    userString2 = [e for e in userString if e.isalnum()]

    #Converting the list of strings into 1 string and into lowercase.
    userString2 = ''.join(userString2).lower()

    #Checking our formatted user string is the same if it was reversed. If true return true.
    if userString2 == userString2[::-1]:
        print(f'Your string "{userString}" is a palindrome.')
        return True
    
    #If false return false.
    else:
        print(f'Your string "{userString}" is not a palindrome.')
        return False
    
#Calling our method via a print statement.    
print(is_palindrome())    
