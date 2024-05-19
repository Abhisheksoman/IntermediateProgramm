def print_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("* " * i)

rows = 5  # You can adjust the number of rows as needed
print_pattern(rows)
