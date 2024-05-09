print("Welcome to the Tip Calculator")
billAmt = float(input("What was the Total bill ? : "))
tipPerc = float(input("How much Percentage of tip you would like to give ? : "))
noPeople = int(input("How many people to Split the Bill ? : "))

total = billAmt + ((tipPerc * billAmt)/100)
perPerson = total / noPeople

perPerson = round(perPerson,2)
print(f"Each Person Should Pay {perPerson}")
