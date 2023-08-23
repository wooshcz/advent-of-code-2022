
def _initialize():
    header = stacks[-1]
    stck = {}
    for i in range(len(header.replace(" ", ""))):
        # print(i)
        idx = header.index(str(i+1))
        # print(idx)
        lst = []
        for column in reversed(stacks[:-1]):
            # print(column[idx], end="")
            if column[idx] == " ":
                break
            lst.append(column[idx])
        stck[str(i+1)] = lst
    return stck

file = open('input.txt', 'r')
stacks = []
while True:
    line = file.readline()
    if line == "\n":
        break
    stacks.append(line.strip("\n"))

procedure = []
while True:
    line = file.readline()
    if line == "":
        break
    procedure.append(line.strip())

print("How many lines are in the stacks? %d" % len(stacks))
print("How many lines are in the procedure? %d" % len(procedure))

stck = _initialize()

for step in procedure:
    step_lst = list(step.split(" "))
    rep = step_lst[1]
    src = step_lst[3]
    dst = step_lst[5]
    for j in range(int(rep)):
        srclst = stck[src]
        # print(stck[src])
        it = srclst.pop()
        stck[src] = srclst
        # print(stck[src])

        # print(stck[dst])
        stck[dst].append(it)
        # print(stck[dst])

print("After the rearrangement procedure completes, what crate ends up on top of each stack?")

for stack in stck.keys():
    print(stck[stack][-1], end="")

print()

stck = _initialize()

for step in procedure:
    step_lst = list(step.split(" "))
    rep = step_lst[1]
    src = step_lst[3]
    dst = step_lst[5]
    srclst = stck[src]
    crates = srclst[-1*int(rep):]
    # print(stck[src])
    for j in range(int(rep)):
        srclst.pop()
    stck[src] = srclst
    # print(stck[src])
    stck[src] = srclst
    # print(stck[dst])
    stck[dst].extend(crates)
    # print(stck[dst])

print("After the rearrangement procedure completes, what crate ends up on top of each stack? (part2)")

for stack in stck.keys():
    print(stck[stack][-1], end="")

print()