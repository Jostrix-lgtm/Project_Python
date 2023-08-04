# Question 3
# Presented by Joseph

# For list of integers
list1 = []

# For list of squares of list1
list2 = []

# This is an instruction Title
print("This program is designed to accept 6 Inputs into a list. Please follow the instructions given.")

# This is a recursive program to ensure users input a number between 1-100
n=0
def integer_check():
    integer=int(input("Enter the number : "))
    if 0<integer<101:
        global n
        n+=1
        list1.append(integer)
        if n<3:
            integer_check()
    else:
        print("Invalid Input. Number should be between 1-100...")
        integer_check()

# Running integer check and printing the list inputs
integer_check()
print(list1)

# Input for power of the three numbers in list
a=input("Enter the power of the First number in List : ")
b=input("Enter the power of the Second number in List : ")
c=input("Enter the power of the Third number in List : ")

# Checking for blanked inputs
next_step=0
if len(a) == 0 or len(b) == 0 or len(c) == 0:
    print("Invalid Input, Blanked inputs are not accepted.")
    next_step+=1
else:
    list2.append(int(a))
    list2.append(int(b))
    list2.append(int(c))

# Display final list output
print("List Found : ",list1+list2)

# Function to check for incorrect input for power of three number in list
def check(n):
    if int(list1[n])!=int(list2[n])**(0.5):
        return False
    elif int(list1[n])==int(list2[n])**(0.5):
        return True

# Function to either print invalid or rotate list according to the check above
if next_step==0:
    x = 0
    for i in range(0, 3):
        check(i)
        if check(i) == True:
            x += 1
        elif check(i) == False:
            x = 0
            print("Invalid Input, One or more Inputs have been identified Incorrect.")
            break
    if x > 0:
        list1.extend(list2)
        list1 = list1[2:] + list1[:2]
        print("After Rotating the list: ",list1)













