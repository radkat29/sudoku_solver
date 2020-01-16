backtracks = 0
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def noviolations(bd, i, j, num):
    #check row
    for x in range(9):
        if bd[i][x] == num:
            return False
    #check column
    for y in range(9):
        if bd[y][j] == num:
            return False
    #check boxes
    PortionX, PortionY = 3 * (i // 3), 3 * (j // 3)
    for xx in range(PortionX, PortionX + 3):
        for yy in range(PortionY, PortionY + 3):
            if bd[xx][yy] == num:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j !=0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#print_board(board)

#def print_index(bord):
#
 #   for i in range(len(bord)):
  #      if i % 3 == 0 and i !=0:
   #         print(i, bord[i])

#print_index(board)

def getempty(bd):
    for i in range(len(bd)):
        for j in range(len(bd)):
            if bd[i][j] == 0:
                #print(i, j)
                return i, j
    return -1, -1

def solve(bd):
    global backtracks
    i, j = getempty(bd)
    print("call to get empty", i, j)
    if i == -1:
        return True
    for trynum in range(1, 10):
        if noviolations(bd, i, j, trynum):
            print("values of i, j, num are", i, j, bd[i][j])
            bd[i][j] = trynum
            print("after insertion values of i, j, num are", i, j, bd[i][j])
            if solve(bd):
                return True
            #reaches here when we looped through all nums and there was no valid number
            print("before backtracking index and val is", i, j, bd[i][j])
            backtracks += 1
            bd[i][j] = 0
            print("after backtracking index and val is", i, j, bd[i][j])
    print("false when", i, j, bd[i][j])
    return False
#for first cell where no values are valid(no value was actually set so it will remain zero)
#return false
#method popped out of stack, the next method on top of stack is called again
#if no valid values then the value is reset to 0 (or a diff valid number is set)

print_board(board)
solve(board)
print("          ")
print("solution")
print_board(board)
print("num backtracks is", backtracks)