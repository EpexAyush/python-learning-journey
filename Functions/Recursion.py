print("-------Question:1-----------")
#defining a function
def sum_n(n):
    '''ye function n tak ke numbers ko add krke final output deta hai.'''
    if n<=1:
        return n
    return n+sum_n(n-1)
result=sum_n(5)
print(f"Total sum: {sum_n(990)}")

print("--------------------------------\n")

print("---------Question:2-----------")
# Question 2 Solution: Print 1 to N Recursively
def print_1_to_n(n):
    if n == 0:
        return 
    print_1_to_n(n - 1)
    print(n)


# Function call
print_1_to_n(4)
print("--------------------------------\n")
