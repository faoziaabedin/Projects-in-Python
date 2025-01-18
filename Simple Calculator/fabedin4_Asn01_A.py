"""
CS1026a 2023
Assigmnet 01 Project 01 - Part A
Faozia Abedin
251383251
fabedin4
October 6th 2023

Code Description: This code computes and displays the Fibonacci sequence.
"""
print("Project One (01) - Part A : Fibonacci Sequence")
sequence_end = int(input("Sequence ends at: "))  # user input for range
a, b = 0, 1  # base numbers of the fibonacci sequence
for f in range(sequence_end + 1):  # include the last number in the range
    formatted = "{:,}".format(a)  # formatting
    print(f"{f}: {a} {formatted}")  # formatting so its position, unformatted, then formatted
    a, b = b, a + b  # formula for the next number

print("\nEND: Project One <01> - Part A")
print("Faozia Abedin fabedin4 251358251")