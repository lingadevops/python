import calendar

year = int(input("Enter year (e.g., 2024): "))
month = int(input("Enter month (1-12): "))

cal = calendar.month(year, month)
print(cal)