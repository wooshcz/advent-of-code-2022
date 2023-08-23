
import math


file = open('input.txt', 'r')
instructions = file.readlines()
init = 1

print("Number of lines is %d" % len(instructions))

class Monkey:
    def __init__(self, name: str, items: list, operator: str, const: any, divisible: int) -> None:
        self._name = name
        self._items = items
        self._operator = operator
        self._divisible_by = divisible
        self._iftrue = None
        self._iffalse = None
        self._insp_counter = 0
        if const == "old":
            self._type = "var"
        else:
            self._type = "const"
            self._const = int(const)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self._iffalse == None:
            print_iffalse = "none"
        else:
            print_iffalse = self._iffalse._name
        if self._iftrue == None:
            print_iftrue = "none"
        else:
            print_iftrue = self._iftrue._name
        return '<' + self._name + '/' + str(len(self._items)) + '/' + self._operator + '/' + str(self._divisible_by) + '/' + str(self._type) + '/' + print_iftrue + '/' + print_iffalse + '/' + str(self._insp_counter) + '>'

    def _oper(self, old) -> int:
        if self._operator == "+" and self._type == "const":
            return old + self._const
        if self._operator == "*" and self._type == "const":
            return old * self._const
        if self._operator == "*" and self._type == "var":
            return old * old

    def _set_iftrue(self, iftrue: 'Monkey'):
        self._iftrue = iftrue

    def _set_iffalse(self, iffalse: 'Monkey'):
        self._iffalse = iffalse

    def _addto(self, item: int) -> None:
        self._items.append(item)

    def _inspect(self):
        val = self._items.pop(0)
        # print("%s is inspecting item %d" % (self._name, val))
        self._insp_counter += 1
        val = self._oper(val)
        val = math.floor(val/3)
        if (val % self._divisible_by == 0):
            # print("Item %d gets thrown to %s" % (val, self._iftrue._name))
            self._iftrue._addto(val)
        else:
            # print("Item %d gets thrown to %s" % (val, self._iffalse._name))
            self._iffalse._addto(val)

monkeys = {}
iftrues = {}
iffalses = {}

for line in instructions:
    line = line.strip("\n")
    if len(line) == 0:
        continue
    if line[0] != " ":
        name = line.split(":")[0]
        continue
    if line[2] != " ":
        key = line.split(":")[0]
        vals = line.split(":")[1]
        if key.strip() == "Starting items":
            items = vals.split(",")
            items = list(map(lambda el: int(el.strip()), items))
            continue
        if key.strip() == "Operation":
            oper = vals.split(" ")[-2]
            const = vals.split(" ")[-1]
            continue
        if key.strip() == "Test":
            divisible = int(vals.split(" ")[-1])
            continue
    if line[4] != " ":
        key = line.split(":")[0]
        vals = line.split(":")[1]
        if key.strip() == "If true":
            iftrue = vals[-1]
            iftrues[name] = iftrue
            continue
        if key.strip() == "If false":
            iffalse = vals[-1]
            iffalses[name] = iffalse
            monkeys[name] = Monkey(name, items, oper, const, divisible)

# print(monkeys)
for kys in iftrues.keys():
    monkeys[kys]._set_iftrue(monkeys['Monkey ' + iftrues[kys]])
    monkeys[kys]._set_iffalse(monkeys['Monkey ' + iffalses[kys]])

for rnd in range(20):
    # print(monkeys)
    print("Round %d" % rnd)
    for key in monkeys.keys():
        while len(monkeys[key]._items) > 0:
            monkeys[key]._inspect()

for key in monkeys.keys():
    print(monkeys[key]._insp_counter)