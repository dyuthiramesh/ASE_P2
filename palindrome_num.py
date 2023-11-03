# Author: Dyuthi Ramesh (B.Tech Sem 2 Section C)
# Checking whether a given number is a palindrome or not

number = 12321 
reverse_number = int(str(number)[::-1])  # converting the number to a string, reversing it and then type converting back to integer

if number == reverse_number:  # palindrome check
    print(number, "is a palindrome!")
else:
    print(number, "is not a palindrome!")
