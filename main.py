def pattern():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    print('inputs:', rows, columns)

    for i in range(rows):
        
        for j in range(columns):
            if(i == 0 and j % 2 == 0):
                 print(' ___ ', end=' ')
            else:
                print('  ',end='')

        print()

        for k in range(columns):
            if(k % 2 == 0):
                print('/   \\', end='')
            else:
                print("___", end="")

        print()

        for l in range(columns):
            if(l % 2 == 0):
                print('\___/', end='')
            else:
                print("   ", end="")
    print()

pattern()

print()

pattern()