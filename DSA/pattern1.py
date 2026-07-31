row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

for outer in range(row):
    for inner in range(column):
        print("*", end=" ")
    
    print()
