
file = open('input.txt', 'r')
grid = file.readlines()

print("Number of lines in the grid is %d" % len(grid))

matrix = []
for line in grid:
    ylist = []
    for char in line.strip():
        ylist.append(int(char))
    matrix.append(ylist)

ylen = len(matrix)
xlen = len(matrix[0])

visible_trees = ylen*2 + xlen*2 - 4
for y in range(1, ylen-1):
    for x in range(1, xlen-1):
        curr = matrix[y][x]
        print("We're at %d,%d: [%d]" % (x,y,curr))
        column = []
        for row in matrix:
            column.append(row[x])
        topl = (column[:y])
        leftl = (matrix[y][:x])
        rightl = (matrix[y][x+1:])
        bottoml = (column[y+1:])
        # print("Top: %s" % topl)
        # print("Left: %s" % leftl)
        # print("Right: %s" % rightl)
        # print("Bottom: %s" % bottoml)
        if max(topl) < curr or max(leftl) < curr or max(rightl) < curr or max(bottoml) < curr:
            visible_trees += 1
            print("Tree at %d,%d is visible!" % (x,y))

print("Number of visible trees: %d" % visible_trees)

def __calc_subscore(line, val):
    if line is None or len(line) == 0:
        return 0
    elif max(line) < val:
        return len(line)
    else:
        dst = 1
        for tree in line:
            if tree >= val:
                return dst
            dst += 1

scenic_score = 0
for y in range(0, ylen):
    for x in range(0, xlen):
        curr = matrix[y][x]
        print("We're at %d,%d: [%d]" % (x,y,curr))
        column = []
        for row in matrix:
            column.append(row[x])
        topl = column[:y]
        leftl = matrix[y][:x]
        rightl = (matrix[y][x+1:])
        bottoml = (column[y+1:])
        # print("Top: %s" % topl)
        # print("Left: %s" % leftl)
        # print("Right: %s" % rightl)
        # print("Bottom: %s" % bottoml)
        topl.reverse()
        leftl.reverse()
        topsco = __calc_subscore(topl, curr)
        leftsco = __calc_subscore(leftl, curr)
        rightsco = __calc_subscore(rightl, curr)
        bottomsco = __calc_subscore(bottoml, curr)
        multiple = topsco * leftsco * rightsco * bottomsco
        print(multiple)
        if multiple > scenic_score:
            scenic_score = multiple
            bestxy = (x,y)

print("Best scenic score: %d" % scenic_score)
print(bestxy)