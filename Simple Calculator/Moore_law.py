"""
CS1026a 2023
Assigmnet 01 Project 01 - Part C
Faozia Abedin
251383251
fabedin4
October 6th 2023

Code Description: This code computes and displays an estimate of the Moore's law (the observation that the number of transistors in an
integrated circuit will double every two years) and the resulting computing power it represents.
"""
print("Project One (01) - Part C: The Moore the Merrier")  # header
starting_transistors = int(input("Starting Number of transistors: "))  # user input for how many transistors to start
starting_years = int(input("Starting Year: "))  # user input for starting year
total_years = int(input("Total Number of Years: "))  # user input for how many year to calculate up too
# Calculating the number of two-year cycles in the output
years = int((total_years + 2)/2)
# header
print("YEAR : TRANSISTORS : FLOPS :")

# for loop that goes through the years
for i in range(years):
    # calculates FLOPS based on the number of transistors
    flops = starting_transistors * 50
    # if else statement to determine the correct units for FLOPS
    if flops < 1e3:
        units = "FLOPS"
    elif 1e3 <= flops < 1e6:
        units = "kiloFLOPS"
        flops /= 1e3
    elif 1e6 <= flops < 1e9:
        units = "megaFLOPS"
        flops /= 1e6
    elif 1e9 <= flops < 1e12:
        units = "gigaFLOPS"
        flops /= 1e9
    elif 1e12 <= flops < 1e15:
        units = "teraFLOPS"
        flops /= 1e12
    elif 1e15 <= flops < 1e18:
        units = "petaFLOPS"
        flops /= 1e15
    elif 1e18 <= flops < 1e21:
        units = "exaFLOPS"
        flops /= 1e18
    elif 1e21 <= flops < 1e24:
        units = "zettaFLOPS"
        flops /= 1e21
    else:
        units = "yottaFLOPS"
        flops /= 1e24
    # Printing and formatting the values
    print(f"{starting_years} {starting_transistors: ,} {flops:.2f} {units} {int(starting_transistors * 50):,}")
    # Doubling the number of transistors and adding 2 years to the years
    starting_transistors *= 2
    starting_years += 2

print("\nEND: Project One (01) - Part C")
print("Faozia Abedin fabedin4 251358251")