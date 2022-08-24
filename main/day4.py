weight = 4.8
cost_ground_premium = 125.00

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:  
  cost_ground = weight * 4.75 + 20

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:  
  cost_drone = weight * 14.25

print(cost_ground)
print(cost_drone)
print("Ground Shipping Premium $", cost_ground_premium)