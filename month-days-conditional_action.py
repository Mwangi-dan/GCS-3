month = input ("Enter month: ").lower()

if month == 'september' or \
    month == 'april' or \
    month == 'june' or \
    month == 'november':
    print(f"The month of {month} has 30 days")
elif month == 'february':
    print(f"The month of {month} has 28 or 29 days")
else:
    print(f"The month of {month} has 31 days")
