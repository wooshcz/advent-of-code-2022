
file = open('input.txt', 'r')
commands = file.readlines()

print("Number of commands in the list is %s" % len(commands))

structure = {}
curr = None
sizes = []
i = 0
for line in commands:
    line = line.strip()
    print("Current folder: %s" % curr)
    if line[0] == "$":
        if len(sizes) > 0:
            structure[curr] = { 'sizes': sizes }
            sizes = []
        print("Input: %s" % line[2:])
        cmd = line.split(" ")
        if cmd[1] == "cd":
            if curr == None and cmd[2] == "/":
                structure[cmd[2]] = { 'sizes': [] }
                curr = cmd[2]
            elif cmd[2] == "..":
                curr = '/'.join(curr.split('/')[0:-1])
                if curr == "":
                    curr = "/"
            else:
                if curr != "/":
                    curr = curr + '/' + cmd[2]
                else:
                    curr = curr + cmd[2]
        if cmd[1] == "ls":
            pass
    else:
        print("Output: %s" % line)
        out = line.split(" ")
        if out[0] == "dir":
            if curr != "/":
                ind = curr + '/' + out[1]
            else:
                ind = curr + out[1]
            structure[ind] = { 'sizes': [] }
        else:
            sizes.append(int(out[0]))
    
    i += 1
    # if i > 30:
    #     break

# print(structure)
limit = 100000
keys_sorted = sorted(structure.keys())
sizes = {}

def __calculate_size(folder, level = 0):
    print("In folder: %s (%d)" % (folder, level))
    depth = len(folder.split("/"))
    if folder == '/':
        depth = 1
    if sizes.get(folder) != None:
        return sizes.get(folder)
    total = sum(structure[folder]["sizes"])
    matches = []
    for match in keys_sorted:
        if match == '/':
            continue
        if folder == '/':
            matches.append(folder + match.split("/")[depth])
        elif match.startswith(folder+'/'):
            matches.append(folder + '/' + match.split("/")[depth])
    # print(matches)
    for child in set(matches):
        print("recursing to %s" % child)
        total += __calculate_size(child, level+1)
    sizes[folder] = total
    return total

grand_total = __calculate_size('/')
print("What is the grand total? %d" % grand_total)
total_under_limit = 0
for size in sizes.values():
    if size < limit:
        total_under_limit += size

print("What is the sum of the total sizes of those directories? %d" % total_under_limit)

disk_space = 70000000
space_needed = 30000000
free_space = disk_space - grand_total
delete_target = space_needed - free_space

print("Free Space: %d, delete target: %d" % (free_space, delete_target))

best_dir = ""
best_size = space_needed
for size in sizes.keys():
    if sizes.get(size) < best_size and sizes.get(size) >= delete_target:
        best_dir = size
        best_size = sizes.get(size)
        print("Best dir so far: %s" % best_dir)

print("Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory? %d" % best_size)
