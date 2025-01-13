#Q6. Create a list, access elements, modify elements, and perform list operations.
# Create a list of fruits.
fruits=["Apple","Banana","Cherry","Date", "Orange"]
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# Access clemcnts using indexing.
fruits[1]="Kiwies"
print(f"modified list is: {fruits}")

#Modify clcmcnts in the list.
fruits.append("watermelon")
print(f"modified list is: {fruits}")

# Add and remove elements from the list.
fruits.remove("watermelon")
print(f"modified list is: {fruits}")

# Find the length of the list.
length=len(fruits)
print(length)

# Sort the list in ascending and descending order.
fruits.sort()
print(f"sorted fruits list are/is: {fruits}")