# Q4. Create a program to print the multiplication table of a number.
# o	Take a number as input from the user.
# o	Use a for loop to iterate from 1 to 10.
# o	Calculate the product of the input number and the current iteration.
# o	Print the multiplication table.

number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")
