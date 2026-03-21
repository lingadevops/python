high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# Using 'or' operator
high_income = True
good_credit = False
if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Using 'not' operator
high_income = False
good_credit = False
student = True
if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")



if (high_income and good_credit) or student:
    print("Eligible for loan")
else:
         print("Not eligible for loan")


if high_income and good_credit and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")