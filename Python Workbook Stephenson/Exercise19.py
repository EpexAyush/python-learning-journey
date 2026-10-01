import math

#given
initial_velocity=0 #m/s
acc_due_to_gravity=9.8 #m/s^2
height=float(input("Enter the height(m): "))


#computation of the final velocity
final_velocity=math.sqrt((initial_velocity**2)+(2*acc_due_to_gravity*height))

print(f"Final Velocity: {final_velocity}")
