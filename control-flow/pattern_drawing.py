while True:
    try:

        size = int(input("Enter the size of pattern:"))
        if size > 0:
            break
        else:
            print("please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer .")

row = 0

# Outer loop - while loop for rows

while row < size:

    for col in range(size):
        print("*", end="")

    print()
    row += 1
