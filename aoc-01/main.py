
def _sum_calories(lines: str) -> int:
    sum = 0
    for cal in lines.split():
        sum += int(cal.replace('|', ''))
    return sum

file = open('input.txt', 'r')
text = '|'.join(file.readlines())

list_elves = text.split('|\n')
print("How many elves are in the list? %d" % len(list_elves))
list_calories = []

for elf in list_elves:
    list_calories.append(_sum_calories(elf))

print("How many total Calories is the top Elf carrying? %d" % sorted(list_calories)[-1])

print("How many Calories are top three Elves carrying in total?? %d" % sum(sorted(list_calories)[-3:]))