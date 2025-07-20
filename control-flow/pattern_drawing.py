pattern_size = int(input("Enter the size of the pattern: "))
row_count = 1

while row_count <= pattern_size:
    column_count = 1
    while column_count <= pattern_size:
        print("*", end="")
        column_count += 1

    print()
    row_count += 1