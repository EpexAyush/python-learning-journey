#==================================================
# Mega Challenge 1: The "Zomato Backend" Simulator
#==================================================

#we have a database
db={
    # Delivery Zones (Tuple Keys : String Values)
    (28.7041,77.1025):"Delhi_North",
    (28.4595, 77.0266): "Gurugram_Hub",
    #Dish Ingredients (String Keys : Set Values)
    "Pasta": {"Cheese", "Tomato", "Garlic", "Flour"},
    "Pizza": {"Cheese", "Tomato", "Basil", "Flour", "Olives"},
    "Vegan Salad": {"Tomato", "Lettuce", "Olives", "Cucumber"}
}

# Task:1 We are adding noida hub in the database.

db.update(
    {(28.5355,77.3910):"Noida_Hub"}
)

#Task:2 Unpacking the coordinates
guru_coords=(28.4595, 77.0266)
lat,long=guru_coords
print(f"Gurugram latitude is {lat} and longitude is {long} ")

# Task:3 We are doing intersection(finding common items)
common_ingredients= db.get("Pasta") & db.get("Pizza")

#Task:4 Performing Deletion between Pasta and Vegan salad
pasta_only_items=db.get("Pasta")-db.get("Vegan Salad")

#Task:5 We have to add mushroom in the pizza ingredients
new_ingre=db.get("Pizza")
new_ingre.add("Mushroom")
print("\n")
# =======================================
# Final Backend Report
# =======================================
print("------------------------Backend Report------------------------")
print(f"Total items in the database: {len(db)}")
print(f"Common ingredients in Pizza and Pasta are: {common_ingredients}")
print(f"Pasta specific items(vs Vegan Salad): {pasta_only_items}")
print(f"Updated Pizza ingredients are: {db["Pizza"]}")
print("-------------------------------------------------------------------")