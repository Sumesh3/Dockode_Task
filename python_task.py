def main():
    row = int(input("Enter the row number: "))
    column = int(input("Enter the column number: "))

    row1 = (row*2)+1
    if column % 2 == 0:
      column1 = column+1
    else:
      column1 = column
    
    for i in range(row1):
        for j in range(column1):
            if i == 0:
                if j % 2 == 0:
                    print(' ___', end='')
                else:
                    print('    ', end='')
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        print('\___/', end='')
                    else:
                        print('   ', end='')
                else:
                    if j % 2 == 0:
                        print('/   \\', end='')
                    else:
                        print('___', end='')
        print()

if __name__ == "__main__":
    main()