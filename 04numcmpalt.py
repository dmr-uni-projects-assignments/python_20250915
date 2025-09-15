# Question 4: Number Comparison (True/False)
# Write a Python program that asks the user for two numbers.
# Store them in variables.
# Print whether the first number is greater than the second (True or False).
# Print whether the two numbers are equal (True or False).

n1 = eval(input("Input num1: "))
n2 = eval(input("Input num2: "))

# add a second one with ifs...
print("n1 > n2 = ", end="")
if (n1 > n2):
    print("True")
else:
    print("False")

print("n1 == n2 = ", end="")
if (n1 == n2):
    print("True")
else:
    print("False")