# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to control rows
while row < size:
    # Use for loop to print a row of asterisks
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after row is complete
    row += 1
