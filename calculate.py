rent = 1150.00
utilities = 65.00
phone = 60.00
car = 400.00

# add all subscriptions

subscriptions = 14.95


def billCalculations(allBills, months): 
  print(allBills * months)
  return


add_all_bills = rent + utilities + phone + car + subscriptions

print("Bill Total Each Month:", billCalculations(add_all_bills, 1))
print("Bill Total For The Entire Year", billCalculations(add_all_bills, 12))

