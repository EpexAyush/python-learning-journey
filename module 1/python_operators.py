print('''============================
        Section: A
============================''')

print("---------Que1: Precedence check-------")
print('''x = 5 + 3 * 2 ** 2
print(x)''') #we dont have to run this solve it in your mind.
print("Output: 17")

print("\n")
print("---------Que2: Associativity check-------")
print('''y=2**3**2
print(y)''')
print("Output: 512")

print("\n")
print("---------Que3: Associativity check-------")
print('''z = 20 - 5 - 3
print(z)''')
print("Output: 12")

print("\n")

print('''===========================
         Section: B
============================''')
print("----------Question: 1---------------")
print("print(10 > 5 and 5 != 5 or 4 == 4)")
print("Output: True")

print("\n")
print("-----------Question: 2---------------")
print('''If score=85, then which option will be return True?
a) score > 90 and score < 100
b) not (score == 85)
c) score >= 80 or score == 100
d) score < 80 and score > 70''')
print("Ans: option C will be the correct answer. ")

print("\n")
print("------------Question: 3---------------")
print('''Precedence order of the + operator is less than the precedence order of the * operator but if any question these operators are come together and we have to operate/solve the + operator first then which symbol will be taken in the consideration?
a) **
b) %
c) ()
d) //''')
print("Ans: option c will be the correct answer.")
print("\n")

print('''===========================
         Section: C
============================''')
print("------------Challenge 1: The E-Commerce Checkout Logic------------")
cart_total = 0

# Task 1: User ne 200 ki T-shirt aur 350 ki Jeans add ki (+= ka use karein)
cart_total+=200+350
# Task 2: User ne 50 ka discount code lagaya (-= ka use karein)
cart_total-=50
# Task 3: Comparison (>=) ka use karke check karein ki kya cart_total 500 ya usse zyada hai.
print(cart_total>=500)
# Result ko 'free_delivery' naam ke variable (Boolean) mein save karein aur print karein.

# Aapka code yahan likhein:
