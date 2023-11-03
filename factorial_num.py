# Author: Dyuthi Ramesh (B.Tech Sem 2 Section C)
# Finding factorial of a given number

num = 5  # taking input from the user
factorial = 1  # initailising factorial as 1 as 1! is equal to 1
for i in range(2, num + 1):  # for loop to iterate over the range
    factorial *= i  # computing the factorial

# Displaying the output
print("Factorial of", num, '=', factorial)