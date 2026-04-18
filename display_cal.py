import calendar

def disply_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

year = int(input("Enter year (e.g., 2024): "))
month = int(input("Enter month (1-12): "))

disply_calendar(year, month)

