#!/usr/local/bin/python

print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill?'))
total_people = float(input('How many people to split the bill?'))
total_percent = float(input('What percentage tip would like to give? 10, 12, or 15?'))

tip = total_bill * (total_percent/100)
total_tip = (total_bill + tip)/total_people 

print(total_tip)