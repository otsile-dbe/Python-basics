#How to print a 2D list (list inside a list)
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]      ]  #This is a list inside a list, or a 2D list, it has 4 rows and 3 columns
print(number_grid[0][0]) # prints 1, first index is row, second index is column
print(number_grid[1][2]) # prints 6, first index is row, second

#Using nested loops in a 2D list
for row in number_grid: #Outer loop that iterates through each row in the 2
    print(row) #Printing the entire row

for row in number_grid: #Outer loop that iterates through each row in the 2D list
    for col in row: #Inner loop that iterates through each column in the current row
        print(col) #Printing each individual element in the 2D list, one by one