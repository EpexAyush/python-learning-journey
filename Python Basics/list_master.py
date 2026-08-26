#=================================================
# Lists In Python (Advanced Practical Scenarios)
#=================================================

print("\n")

#-------------------------------------------------------
#Task 1: Cinema Ticket Queue (Slicing & Modification)
#-------------------------------------------------------

#Creating a list ticket_queue
ticket_queue=["Rohan","Priya","Amit","Sana","Karan"]
#Extracting the first 3 peoples from the list using slicing and storing it into a variable.
vip_queue=ticket_queue[0:3]
#Removing Amit from the original list 
ticket_queue.remove("Amit")
#adding new person vikram into the original list at index no=2
ticket_queue.insert(2,"Vikram")
#printing the final output of the ticket_queue
print(ticket_queue)

print("\n")

#-------------------------------------------------
#Task 2: Movie Watchlist (Operations & Reversing)
#-------------------------------------------------

#creating an empty list.
upcoming_movies=[]
#adding 2 movies in the list using append() function.
upcoming_movies.append("Dune 2")
upcoming_movies.append("Deadpool 3")
#creating another list
classic_movies=["Godfather","Matrix"]
#merging classical movies into upcoming movies
upcoming_movies.extend(classic_movies)
#Reversing the entire upcoming movies list 
upcoming_movies.reverse()
#print upcoming movies.
print(upcoming_movies)

print("\n")

#-------------------------------------------------------
#Task 3: Box Office Analysis (Math, Counting & Sorting)
#-------------------------------------------------------

#creating a list of ticket sales for the day.
ticket_sales=[250,150,500,150,300,150,800]
#Total revenue of that day.
print(f"Total Revenue:{sum(ticket_sales)}")
#the highest ticket price which was sold.
print(f"The Highest Ticket Price: {max(ticket_sales)}")
#lowest ticket price which was sold.
print(f"The Lowest Ticket Price: {min(ticket_sales)}")
#checking how many tickets were sold of Rs 150.
print(F"150 Rs. Tickets Sold: {ticket_sales.count(150)}")
#sorting the ticket sales list into the ascending order and printing it.
ticket_sales.sort()
print(f"Ticket sales in Increasing Order: {ticket_sales}")