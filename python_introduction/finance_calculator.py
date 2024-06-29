Income = int(input("Enter your monthly income: "))
monthlyExp = int(input("Enter your monthly expenses: "))

Monthly_Savings = int(Income - monthlyExp)
Projected_Savings = int(Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05))

print("Your monthly savings are $", Monthly_Savings)

print("Projected savings after one year, with interest, is: ", Projected_Savings)


