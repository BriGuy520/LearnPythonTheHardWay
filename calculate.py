# Rent payments for the year

rent = 1150.00

utilities = 65.00

# Calculate phone bill for year

phone = 60.00

# Car payments 

car = 400.00

# add all subscriptions

subscriptions = 14.95


def billCalculations(allBills, months): 
  print(allBills * months)
  return


addAllBills = rent + utilities + phone + car + subscriptions

print("Bill Total Each Month:", billCalculations(addAllBills, 1))
print("Bill Total For The Entire Year", billCalculations(addAllBills, 12))

