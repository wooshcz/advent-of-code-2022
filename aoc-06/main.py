
file = open('input.txt', 'r')
stacks = []
line = file.readline().strip()

print("Length of the line is %s" % len(line))

signal_char = 0
for id in range(0, len(line)):
    print(id)
    #print(line[id])
    if id < 3:
        continue
    if len(set(line[id-3:id+1])) == 4:
        print(line[id-3:id+1])
        signal_char = id+1
        break

print("How many characters need to be processed before the first start-of-packet marker is detected? %d" % signal_char)

signal_char = 0
for id in range(0, len(line)):
    print(id)
    #print(line[id])
    if id < 13:
        continue
    if len(set(line[id-13:id+1])) == 14:
        print(line[id-13:id+1])
        signal_char = id+1
        break

print("How many characters need to be processed before the first start-of-packet marker is detected? %d" % signal_char)