# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.



import calendar

month= int(input("Enter month in number: "))
year=int(input("Enter year in number: "))
print(f"{calendar.month(year,month)}")