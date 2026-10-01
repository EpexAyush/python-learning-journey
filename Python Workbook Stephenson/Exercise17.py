mass_of_water=float(input("Enter the mass of the water(gm): "))


initial_temp=float(input("Enter the initial temprature(C): "))
final_temp=float(input("Enter the final temprature(C): "))

specific_heat_capacity_of_water=4.186 # J/g*C


#temprature change
delta_t=final_temp-initial_temp

#calculation of the amount of the energy that must be added or removed to acheive the desired temprature change
q=mass_of_water*specific_heat_capacity_of_water*delta_t

if q<0:
    print(f"Amount of energy released: {-q:.2f}")

elif q>0:
    print(f"Amount of energy gained: {q:.2f}")

else:
    print(f"Amount of energy required: {q:.2f}")

#computing the cost of heating of water
electricity_cost_per_kwh=8.9 #cents
q_kwh=q/3600000 #energy in KwH

total_electricity_bill=(q_kwh*electricity_cost_per_kwh)/100 # dollars

print(f"Total Electricity bill: ${total_electricity_bill:.2f}")