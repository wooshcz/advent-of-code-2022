
import string

def _sum_priorities(list_rucksacks):
    sum_priorities = 0
    for sack in list_rucksacks:
        sack = sack.strip()
        slice1 = sack[:int(len(sack)/2)]
        slice2 = sack[int(len(sack)/2):]
        #print("%s / %s" % (slice1, slice2))
        char = "".join(set(slice1).intersection(set(slice2)))
        #print(char)
        if char != '':
            #print(list_letters.index(char)+1)
            sum_priorities += (list_letters.index(char)+1)
    return sum_priorities

file = open('input.txt', 'r')
list_rucksacks = file.readlines()
list_letters = list(string.ascii_letters)

print("How many rucksacks are in the list? %d" % len(list_rucksacks))


print("What is the sum of the priorities of those item types? %d" % _sum_priorities(list_rucksacks))

i = 0
list_groups = []
list_group = []
for sack in list_rucksacks:
    list_group.append(sack)
    if (i+1)%3 == 0:
        list_groups.append(list_group)
        list_group = []
    i += 1

def _get_priority_v2(group_sacks):
    prio = 0
    char = "".join(
        set(group_sacks[0].strip())
            .intersection(set(group_sacks[1].strip()))
            .intersection(set(group_sacks[2].strip()))
        )
    #print(char)
    if char != '':
        #print(list_letters.index(char)+1)
        prio += (list_letters.index(char)+1)
    return prio

sum_priorities = 0
for group in list_groups:
    sum_priorities += _get_priority_v2(group)

print("What is the sum of the priorities of those item types (part2)? %d" % sum_priorities)