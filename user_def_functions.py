#square function
def calculate_square(number):
    result=number**2
    print(result)

calculate_square(2342)

#calculate Area
def calculate_area(length,width):
    result=length*width
    print(f"{result} meter square.")

calculate_area(23,54)

#calculate cube:
def calculate_cube(number):
    result=number**3
    print(result)
calculate_cube(76)

# Even or not?
def is_even(num):
    if num%2!=0:
        print(f"{num} is an Odd Number.")

    elif num==0:
        print("You have entered a Zero.")

    else:
        print(f"{num} is an Even Number.")

is_even(1)

#find largest number
def largest_num(num1,num2):
    result=max(num1,num2)
    print(f"{result} is the largest number.")
#calling the function 
largest_num(7868,546)

#calculation a simple interest:
# suppose a person is invested 20 lakh Rs for 5 years and bank is giving him 12% interst per year then how much amount he will get from interest.
def sim_int(p,r,t):
    result=(p*r*t)/100
    print(result)

sim_int(2000000,23,5)

# calculating the student result
# eg: Ayush scored total marks 523 and got 87.1666% and we are calculating marks for 6 subjects
def stu_marks(name,mark1,mark2,mark3,mark4,mark5,mark6):
    total_marks= mark1+mark2+mark3+mark4+mark5+mark6
    percent= total_marks/6
    print(f"{name} score {total_marks} and got {percent}%")

stu_marks("Ayush",88,87,83,84,99,82)