
file = open('input.txt', 'r')
list_pairs = file.readlines()

print("How many pairs are in the list? %d" % len(list_pairs))

sum_pairs = 0
for pair in list_pairs:
    tpl = tuple(pair.strip().split(","))
    rng1 = set(range(int(tpl[0].split("-")[0]), int(tpl[0].split("-")[1])+1))
    rng2 = set(range(int(tpl[1].split("-")[0]), int(tpl[1].split("-")[1])+1))
    # print(rng1)
    # print(rng2)
    # print(rng1.union(rng2))
    if len(rng1.union(rng2)) == max(len(rng1), len(rng2)):
        sum_pairs += 1


print("In how many assignment pairs does one range fully contain the other? %d" % sum_pairs)


sum_pairs = 0
for pair in list_pairs:
    tpl = tuple(pair.strip().split(","))
    rng1 = set(range(int(tpl[0].split("-")[0]), int(tpl[0].split("-")[1])+1))
    rng2 = set(range(int(tpl[1].split("-")[0]), int(tpl[1].split("-")[1])+1))
    # print(rng1)
    # print(rng2)
    # print(rng1.union(rng2))
    if len(rng1.union(rng2)) != len(rng1) + len(rng2):
        sum_pairs += 1

print("In how many assignment pairs do the ranges overlap? %s" % sum_pairs)