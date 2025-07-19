# Pattern drawings

size = int(input("Enter the size of pattern:"))

row = 0

# Outer loop - while loop for rows

while row < size:

    for col in range(size):
        print("*", end="")

    print()
    row += 1