#python 3.8.2
import sys

# charges varibles that can chanage with rate increases later
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00
over_charge = 0.25 # Over Milage charges 

#Mile limits
daily_limit = 100 # Daily Milage Limit
weekly_Limit = 900 # weekly Milage limit

mile_charge = 0 # intiial varible as 0 to remove extra else statments
extra_miles = 0  #intiial varible as 0 to remove extra else statments

# get information from user ,rental type, odometer intial and final reading
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input('Ending Odometer Reading:\n'))

totalMiles = odoEnd - odoStart# get total miles driven

# if Daily or budget  or  weekly is rental code rental period is days
# base charge of rental is rental period * type of charge
if rentalCode == 'B':
    rentalPeriod = int(input("Number of Days Rented:\n"))
    baseCharge = rentalPeriod * budget_charge
    mile_charge = totalMiles * over_charge     # budget rental  mileage charge:for each mile driven

elif rentalCode == 'D':  # daily rental code
    rentalPeriod = int(input("Number of Days Rented:\n"))
    baseharge = rentalPeriod * daily_charge
    averageDayMiles = totalMiles / rentalPeriod
    # daily rental if under 100 daily miles charge daily rate if above add on  extra mileage charge per mile
    if averageDayMiles >= daily_limit:
        extra_miles = averageDayMiles - daily_limit
        mile_charge = extra_miles * over_charge

elif rentalCode == 'W':
    # if Weekly is rental code rental period is number of weeks
    rentalPeriod = int(input("Number of Weeks Rented:\n"))
    baseCharge = rentalPeriod * weekly_charge
    averageWeekMiles = totalMiles / rentalPeriod
    # daily rental if under 900 weekly miles charge weekly rate if above add on 25cents per mile
    if averageWeekMiles >= weekly_Limit:
        extra_miles = averageWeekMiles - weekly_Limit
        mile_charge = over_charge * rentalPeriod


# add base charge and mileage charge to get total rental amount
ammount = baseCharge + mile_charge

print(f"""
Rental Summary

Rental Code:        {rentalCode}
Rental Period:      {rentalPeriod}
Starting Odometer:  {odoStart}
Ending Odometer:    {odoEnd}
Miles Driven:       {totalMiles}
Amount Due:         {format(ammount, '.2f')}
""")

# other option to print out as in the example

# # print off the rental summary.
# print('Rental Summary')
# # Rental Code:        The rental code
# print('Rental Code:        {}'.format(rentalCode))
# # Rental Period:      The number of days the vehicle was rented
# print('Rental Period:        {}'.format(rentalPeriod))
# # Starting Odometer:  The vehicle's odometer reading at the start of the rental period
# print('Starting Odometer:  {}'.format(odoStart))
# # Ending Odometer:    The vehicle's odometer reading at the end of the rental period
# print('Ending Odometer:    {}'.format(odoEnd))
# # Miles Driven:       The number of miles driven during the rental period
# print('Miles Driven:      {}'.format(totalMiles))
# # Amount Due:         The amount of money billed displayed with a dollar sign cents
# print('Amount Due:        ${}'.format(format(ammount, '.2f')))
