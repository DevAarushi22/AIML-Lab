# Q1.  Create and access tuples.
# o	Create a tuple of colors.
# o	Access elements using indexing.
# o	Try to modify an element in the tuple (to demonstrate immutability).
# o	Find the number of occurrences of a specific element in the tuple.

colors = ("red", "blue", "green", "yellow", "blue")
print("First color:",colors[0])
print("Last color:", colors[-1])
blue_count=colors.count("blue")
print("Number of blue colors:", blue_count)