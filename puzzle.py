import random

grid_puzzle = [[0 for _ in range(9)] for _ in range(9)]

# Build 9 blocks (3x3 subgrids)
blocks = []
k1, s1 = 3, 0
for _ in range(3):
    s2, k2 = 0, 3
    for y in range(3):
        b = [(a, e) for a in range(s1, k1) for e in range(s2, k2)]
        blocks.append(b)
        s2 += 3
        k2 += 3
    s1 += 3
    k1 += 3

def check_block(num, block, cell):
    for x in block:
        if x == cell:
            continue  # skip current cell
        if grid_puzzle[x[0]][x[1]] == num:
            return False
    return True

def check_row(num, row):
    for i in range(9):
        if grid_puzzle[row][i] == num:
            return False
    return True

def check_col(num, col):
    for i in range(9):
        if grid_puzzle[i][col] == num:
            return False
    return True



def solve():
    # find next empty cell
    for r in range(9):
        for c in range(9):
            if grid_puzzle[r][c] == 0:

                # find block for this cell
                for b in blocks:
                    if (r, c) in b:
                        block = b
                        break

                nums = list(range(1, 10))
                random.shuffle(nums)

                for num in nums:
                    if (check_block(num, block, (r, c)) and
                        check_row(num, r) and
                        check_col(num, c)):

                        grid_puzzle[r][c] = num  # place number

                        if solve():              # recursive continue
                            return True

                        grid_puzzle[r][c] = 0    # undo on failure

                return False  # no number works → backtrack

    return True  # solved

#create puzzle
cells_remove = []

def generate_puzzle(num):
    while len(cells_remove)< num:
        i = random.randint(0,8)
        j = random.randint(0,8)
        grid_puzzle[i][j]=0
        if solve():
            cells_remove.append((i,j))
            grid_puzzle[i][j]=0
    for cell in cells_remove:
        grid_puzzle[cell[0]][cell[1]] =0


# Run generator
def insert_num():
    solve()
    generate_puzzle(40)



