# This is the conversion of weight measurement
# weight of user
user_weight = int(input("Enter your weight: "))
# user unit in uppercase
unit = input("kilos(K)g or pounds(L)bs: ").upper()
# comparison of unit
if unit == "L":
    # To convert pounds to kilograms use times by 0.45
    converted = user_weight * 0.45
    print("your weight is", converted, "kilograms(kg)")
else:
    # To convert kilograms to pounds use divide by 0.45
    converted = user_weight / 0.45
    print("your weight is", converted, "pounds(lbs)")