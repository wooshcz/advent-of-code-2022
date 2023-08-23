
file = open('input copy.txt', 'r')
movements = file.readlines()

print("Number of movements in the grid is %d" % len(movements))

# hx = hy = 0
# tx = ty = 0

# visited = set()
# for movement in movements:
#     line = movement.strip().split(" ")
#     print("[%d,%d]" % (hx, hy))
#     visited.add((tx,ty))
#     dst = int(line[1])
#     dir = line[0]
#     # print(dir)
#     # print(dst)
#     transform = ()
#     if dir == 'U':
#         transform = (0,1)
#     if dir == 'D':
#         transform = (0,-1)
#     if dir == 'L':
#         transform = (-1,0)
#     if dir == 'R':
#         transform = (1,0)
#     for i in range(dst):
#         oldx = hx
#         oldy = hy
#         hx += transform[0]
#         hy += transform[1]
#         if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
#             continue
#         else:
#             tx = oldx
#             ty = oldy
#             print("Tail moved to [%d,%d]" % (tx, ty))
#             visited.add((tx,ty))

# print(len(visited))



hx = hy = 0
tx = list(0 for j in range(9))
ty = list(0 for j in range(9))

visited2 = set()
for movement in movements:
    line = movement.strip().split(" ")
    print("[%d,%d]" % (hx, hy))
    visited2.add((tx[8],ty[8]))
    dst = int(line[1])
    dir = line[0]
    # print(dir)
    # print(dst)
    transform = ()
    if dir == 'U':
        transform = (0,1)
    if dir == 'D':
        transform = (0,-1)
    if dir == 'L':
        transform = (-1,0)
    if dir == 'R':
        transform = (1,0)
    for i in range(dst):
        oldx = hx
        oldy = hy
        hx += transform[0]
        hy += transform[1]
        print("[%d,%d]" % (hx, hy))
        if abs(hx-tx[0]) > 1 or abs(hy-ty[0]) > 1:
            print("moving knot 1 to [%d,%d]" % (oldx,oldy))
            prevx = tx.copy()
            prevy = ty.copy()
            tx[0] = oldx
            ty[0] = oldy
            for n in range(1,9):
                if abs(tx[n]-tx[n-1]) > 1 or abs(ty[n]-ty[n-1]) > 1:
                    print("moving knot {} to [{},{}]".format((n+1), prevx[n-1], prevy[n-1]))
                    tx[n] = prevx[n-1]
                    ty[n] = prevy[n-1]
                    if n == 8:
                        print("Tail moved to [%d,%d]" % (tx[8], ty[8]))
                        visited2.add((tx[8],ty[8]))

print(len(visited2))