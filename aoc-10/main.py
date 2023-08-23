
file = open('input.txt', 'r')
instructions = file.readlines()
init = 1

print("Number of instructions is %d" % len(instructions))
signal = []
carry = None
for inst in instructions:
    inst = inst.strip().split(" ")
    print(inst)
    if len(signal) == 0:
        setval = init
    else:
        setval = signal[-1]
        if carry is not None:
            setval = carry
    if inst[0] == 'noop':
        signal.append(setval)
    if inst[0] == 'addx':
        val = int(inst[1])
        signal.append(setval)
        signal.append(setval)
        carry = setval + val
    print(signal[-1])

print(signal)
print(len(signal))
# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
cycles = [20, 60, 100, 140, 180, 220]
sums = 0
for cycle in cycles:
    sums += cycle * signal[cycle-1]
    print(signal[cycle-1])
    print(cycle*signal[cycle-1])

print("[Part 1] - What is the sum of these six signal strengths? %d" % sums)

crth = 6
crtw = 40
cyc = 0
output = []
for row in range(crth):
    line = []
    for pos in range(crtw):
        sprite = list('.' for j in range(crtw))
        for pixel in range(-1, 2):
            xpos = signal[cyc] + pixel
            if xpos >= 0 and xpos < crtw:
                sprite[signal[cyc] + pixel] = 'X'
        # print(sprite)
        print(sprite[(cyc) % crtw], end="")
        cyc += 1
    print("")

