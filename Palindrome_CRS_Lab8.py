#Receiving inputs from user
myPalindrome = input("What would you like to check for a palindrome?")

#Removing all alphanumberic values and converting to lowercase.
myPalindrome2 = ''.join(e for e in myPalindrome if e.isalnum()).lower()

def is_palindrome(myP):
    #Checking if our original string is equal to our reversed string. If true return true.      
    if myP == myP[::-1]:
        return True
    
    #If not true return false.
    else:
        return False

#Printing our results passing in the user input as our parameter.
print(is_palindrome(myPalindrome2))