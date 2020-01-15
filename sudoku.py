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

print_board(board)

def print_index(bord):

    for i in range(len(bord)):
        if i % 3 == 0 and i !=0:
            print(i, bord[i])

#print_index(board)

def getempty(bd):
    for i in range(len(bd)):
        for j in range(len(bd)):
            if bd[i][j] == 0:
                print(i, j)
                return i, j
    return -1, -1

getempty(board)


def isPossible(bd, i, j, num):
    for x in range(9):
        if bd[i][x] != num:
            rowvalid = True
            if rowvalid:
                for y in range(9):
                    if bd[y][j] != num:
                        columnvalid = True
                        if columnvalid:
                            PortionX, PortionY = 3*(i/3), 3*(j/3)
                            for x in range(PortionX, PortionX+3):
                                for y in range(PortionY, PortionY+3):
                                    if bd[x][y] == num:
                                        return False
                            return True
        return False


def solve(bd, i = 0, j = 0):
    i, j = getempty(bd)
    if i == -1:
        return True



    #check if the num added does not violate any rules in columns
