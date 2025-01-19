"""
CS1026a 2023
Assigmnet 01 Project 01 - Part B
Faozia Abedin
251383251
fabedin4
October 6th 2023

Code Description: The program computes and displays all the prime numbers that is within the range the user inputs.
"""
print("Part One - Project B: Prime Choice")  # title
starting_range = int(input("\nPrime Numbers starting with: "))  # user input for starting range
ending_range = int(input("and ending with: "))  # user input for ending range

if starting_range >= ending_range:  # invalid input, if starting is greater than ending
    print("\nIncorrect input:", starting_range, "is greater than", ending_range)
    print("The numbers have been automatically switched")
    starting_range, ending_range = ending_range, starting_range
    # switches the starting into ending and ending into starting
prime_numbers = []  # to hold numbers that are prime

for num in range(starting_range, ending_range + 1):  # goes through all the numbers in the range
    prime: bool = True
    for divisor in range(2, int(num ** 0.5) + 1):  # starting from 2, it checks the square root of the numbers
        if num % divisor == 0:  # checks if the number is divisible
            prime = False  # declares as a prime number
            break
    if prime:
        prime_numbers.append(num)  # stores the prime numbers into the variable
if prime_numbers:
    print("\nPrime numbers in the range from:", starting_range, "and", ending_range, "are:")
    for prime in prime_numbers:  # outputs all the prime numbers
        print(prime, "is prime")
else:
    print("There were no prime numbers found in the range")  # for when there is no prime number

print("\nEnd Part One <01> - Project B")
print("Faozia Abedin fabedin4 251358251")