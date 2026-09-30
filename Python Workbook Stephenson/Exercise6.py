meal_cost=float(input("Enter the cost of the meal($): "))

#Tax calculation for the meal
percent_tax=5
tax_in_meal=(meal_cost*percent_tax)/100

#Tip calculation for the meal
percent_tip=18
tip_in_meal=(meal_cost*percent_tip)/100

#Total meal cost after adding both tax and tip in the meal cost.
total=meal_cost+tax_in_meal+tip_in_meal

#Output
print(f"Tax Amount: ${tax_in_meal:.2f}")
print(f"Tip Amount: ${tip_in_meal:.2f}")
print(f"Grand Total: ${total:.2f}")