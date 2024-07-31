from datetime import date

firstdate=date(2023,7,3)
lastdate=date(2023,11,4)

leftdays=lastdate-firstdate
print(f"{leftdays.days} days left")