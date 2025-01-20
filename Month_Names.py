months =  ["January","February","March","April","May","June","July","August","September","October","November","december"]

Month_id = int(input("Enter the month number (1-12):"))
# QUESTION1
if 1 <= Month_id <= 12:
    print(f"Month number {Month_id} is {months[Month_id - 1]}")
else:
    print("Invalid input!Please enter a number between 1 and 12")


# Question 2
age = int(input("Enter your age: "))

if age < 16:
    print("Your ticket costs  3.00")
elif age < 60:
    print("Your ticket costs  6.00")
else:
    print("Your ticket costs  2.00")

# Question 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("The greatest number amongst the entered values is the first number", a)
elif b > a and b > c:
    print("The greatest number amongst the entered values is the second number", b)
elif c > a and c > b:
    print("The greatest number amongst the entered values is the third number", c)

   # Question 5

num1 = int(input("Enter the number to calculate factorial: "))

factorial = 1

if num1 < 0:
    print("Factorials do not exist for negative numbers")
elif num1 == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num1+1):
        factorial *= i
    print(f"The factorial for {num1} is {factorial}.")

   # Question6

num4 = int(input("Enter the number: "))
r = 0

while num4 > 0:
   d = num4 % 10
   r = r * 10 + d
num4 = num4 // 10
print(f"The reverse of the entered number is {r}")

    # Question7

num2 = int(input("Enter the number: "))
num3 = int(input("Enter number of multiples you need: "))

print(f"The first {num3} multiples of {num2} are: ")
for i in range(1,num3+1):
    print(num2 * i, end=" ")

      # Question 8

while True:
    word = input("Enter a word (type 'done' to end): ")
    print(f"The word you entered is {word}")
    if word == 'done' or word == 'Done' or word == 'DONE':
        break

# Question 9

for i in range (1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

        # question 10

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()





