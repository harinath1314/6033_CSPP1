import sys

# no of rows are equal to the number of columns.
n = int(input("Enter the number of rows in a matrix"))
a = [[0 for x in range (n)] for y in range(n)]
for i in range (n):
    for j in range(n):
        a[i][j]=int(input())
        print (a[i][j])
    print("\n")