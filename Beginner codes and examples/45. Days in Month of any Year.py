def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(Year, Month):
    if Month > 12 or Month < 1:
        return "Invalid Inputs"
    Month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(Year) == True and Month == 2:
        return print("29")
    else:
        return print(Month_days[Month - 1])


days_in_month(Year=int(input("Enter a Year ")), Month=int(
    input("Enter a Month (1 for January so on..) ")))
