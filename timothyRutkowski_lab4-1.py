# Timothy Rutkowski 02/21/2024 timothyRutkowski_lab4-1.py

# This program will start at a penny and double it's value every day
# using a loop function. Each value will be double that of the day before. 
# The amount of days the values are to double will be input by the user.

#Define variables
daysInput = int(input('\nPlease enter the amount of days you would like to calculate: '))
startPay = float(0.01) # Starting pay for the first day
totalPay = 0 # Intialize total pay to 0
pay = startPay # Initialize pay to starting amount of a penny

#Sets the header
print('\nDay\tPennies')
print('-----------------')

#Loop function to calculate pay for each day
for day in range(1, daysInput + 1):
    totalPay += pay
    print(f'{day}\t${pay:.2f}')
    pay *= 2 # Double the pay for each day

#Output the total pay
print(f'\nThe total pay for {daysInput} days is: ${totalPay:.2f}')