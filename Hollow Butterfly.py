n = int(input("Enter the size of the pattern: "))

# Upper part of the pattern
for i in range(1, n + 1):
    if i == 1:
        # First row: asterisks at the corners with a long gap between
        print("* " + "  " * (n * 2 - 2) + "* ")
    else:
        # Calculate spaces for subsequent rows
        left_right_space = 2 * (i - 2)  # Spaces between the side stars and the edges
        middle_space = 4 * (n - i)      # Spaces between the two middle stars
        # Construct the row
        row = "* " + " " * left_right_space + "* " + " " * middle_space + "* " + " " * left_right_space + "* "
        print(row)

# Lower part of the pattern
hollow_space = 0
for i in range(1, n + 1):
    if i == n:
        # Last row: asterisks at the corners like the first row
        print("* " + "  " * (n * 2 - 2) + "* ")
    else:
        # Calculate spaces for subsequent rows
        left_right_space = (n - i - 1) * 2  # Spaces between the side stars and the edges
        # Construct the row
        row = "* " + " " * left_right_space + "* " + " " * hollow_space + "* " + " " * left_right_space + "* "
        hollow_space += 4  # Increase the hollow space in the middle for each subsequent row
        print(row)
