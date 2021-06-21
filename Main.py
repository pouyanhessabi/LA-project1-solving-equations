augmented_matrix = []
constant_matrix = []


def print_matrix():
    make_zero()
    for i in range(len(augmented_matrix)):
        print("| ", end="")
        for j in range(len(augmented_matrix[i])):
            print("%.2f" % augmented_matrix[i][j], end="     ")
        print("|")
    print()


def has_zero(row_index):
    a = 0
    for i in range(len(augmented_matrix[0])):
        if augmented_matrix[row_index][i] != 0 and i != len(augmented_matrix[0]) - 1:
            return False
    return True


def check_inconsistent():
    for j in range(len(augmented_matrix)):
        if has_zero(j):
            print("***  Inconsistent    ***")
            exit()


def make_zero():
    for i in range(len(augmented_matrix)):
        for j in range(len(augmented_matrix[0])):
            if augmented_matrix[i][j] == 0:
                augmented_matrix[i][j] = 0.00


def solution_print(column):
    print("X" + str(column + 1), end=" ")
    print("| " + str("%.2f" % augmented_matrix[0][column]) + " |")
    for row in range(len(augmented_matrix) - 1):
        row += 1
        print("   | " + str("%.2f" % augmented_matrix[row][column]) + " |")


print("***      Hello , it's only for n * n matrix      ***\n***      Be careful about your input             ***")
tmp = int(input("Please enter number of rows:\n"))
print("Enter coefficient matrix by each row")
for i in range(tmp):
    augmented_matrix.append(list(map(float, input().split())))
    if i == tmp - 1:
        break
    print("Enter next row")
print("Enter constant matrix by each row")
temporary = 0
for i in range(tmp):
    temporary = float(input())
    constant_matrix.append(temporary)
    augmented_matrix[i].append(temporary)
tmp = len(augmented_matrix[0])
for i in range(len(augmented_matrix)):
    for j in range(len(augmented_matrix)):
        if len(augmented_matrix[j]) != len(augmented_matrix[i]):
            print("Wrong input")
print("Augmented Matrix :")
print_matrix()
check_inconsistent()

print("Each step:")
k = 0
while k < (len(augmented_matrix[0]) - 1):
    try:
        tmp = augmented_matrix[k][k]
    except:
        pass
    if tmp == 0:
        break
    for i in range(len(augmented_matrix[0])):
        try:
            augmented_matrix[k][i] /= tmp
        except:
            pass
    try:
        if k == len(augmented_matrix[0]) - 2:
            break
    except:
        pass
    for j in range(len(augmented_matrix)):
        try:
            temporary = augmented_matrix[k + 1 + j][k]
        except:
            pass
        for i in range(len(augmented_matrix[0])):
            try:
                augmented_matrix[k + 1 + j][k + i] += -temporary * augmented_matrix[k][k + i]
            except:
                pass
    k += 1
    print_matrix()
    print()

check_inconsistent()
print("***  Echelon form   ***")
print_matrix()

j = 0
i = len(augmented_matrix) - 1
while i > 0:
    last_column = len(augmented_matrix[0]) - 1 - j
    last_row = len(augmented_matrix) - 1 - j
    tmp = augmented_matrix[last_row - 1][last_column - 1]
    while last_row > 0:
        last_column = len(augmented_matrix[0]) - 1
        tmp = augmented_matrix[last_row - 1][last_column - 1 - j]
        while last_column + 1 > last_row:
            augmented_matrix[last_row - 1][last_column] += -augmented_matrix[i][last_column] * tmp
            last_column -= 1
        last_row -= 1
    i -= 1
    j += 1

check_inconsistent()
print("***   Reduced echelon form   *** ")
print_matrix()

print("***   The solution is   ***")
for i in range(len(augmented_matrix[0]) - 2):
    solution_print(i)
    print("      +")
solution_print(len(augmented_matrix[0]) - 2)
print("      =")
column = len(augmented_matrix[0]) - 1
print("   | " + str("%.2f" % augmented_matrix[0][column]) + " |")
for row in range(len(augmented_matrix) - 1):
    row += 1
    print("   | " + str("%.2f" % augmented_matrix[row][column]) + " |")
