import functools
from math import gcd

monkeys = []

def parseOperation(op, oldVal):
    if op == 'old * old':
        return oldVal * oldVal
    elif op[4] == '*':
        return oldVal * int(op[len('old * '):])
    elif op[4] == '+':
        return oldVal + int(op[len('old + '):])
    return 0

with open('input11.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        
        if line.startswith('Monkey'):
            monkeys.append({
                'items': [],
                'operation': '',
                'testDivisibleBy': 0,
                'testTrueTarget': -1,
                'testFalseTarget': -1
            })

        elif line.startswith('Starting items: '):
            items = line[len('Starting items: '):].split(', ')
            items = list(map(lambda x: int(x), items))
            monkeys[len(monkeys)-1]['items'] = items

        elif line.startswith('Operation:'):
            operation = line[len('Operation: new = '):]
            monkeys[len(monkeys)-1]['operation'] = operation

        elif line.startswith('Test: divisible'):
            testDivisibleBy = int(line[len('Test: divisible by '):])
            monkeys[len(monkeys)-1]['testDivisibleBy'] = testDivisibleBy
        
        elif line.startswith('If true'):
            testTrueTarget = int(line[len('If true: throw to monkey '):])
            monkeys[len(monkeys)-1]['testTrueTarget'] = testTrueTarget
        
        elif line.startswith('If false'):
            testFalseTarget = int(line[len('If false: throw to monkey '):])
            monkeys[len(monkeys)-1]['testFalseTarget'] = testFalseTarget

monkeyActivities = [0] * len(monkeys)

# for part two
def lcm(a,b):
    return a*b // gcd(a,b)

modulos = list(map(lambda x: x['testDivisibleBy'], monkeys))
modulo = functools.reduce(lambda x, y: lcm(x, y), modulos)
print(modulo)
#

for round in range(0, 10000):#20): part two / one
    for monkeyIdx in range(0, len(monkeys)):
        #print(round, monkeyIdx)
        for itemCount in range(0, len(monkeys[monkeyIdx]['items'])):
            #print(monkeys[monkeyIdx]['items'])
            monkeyActivities[monkeyIdx] = monkeyActivities[monkeyIdx] + 1
            # 1st elem always get popped
            newWorry = int( parseOperation(monkeys[monkeyIdx]['operation'], monkeys[monkeyIdx]['items'].pop(0)) ) % modulo #part two, // 3 in part one

            newMonkeyIdx = monkeys[monkeyIdx]['testTrueTarget'] \
                if (newWorry % monkeys[monkeyIdx]['testDivisibleBy'] == 0) \
                else monkeys[monkeyIdx]['testFalseTarget']
            
            monkeys[newMonkeyIdx]['items'].append(newWorry)

print(
    [{'monkey':i, 'activityCount':x} for i,x in enumerate(monkeyActivities)]
)
# part one: 348 * 347 = 120756
# part two: 195229 * 200326 = 38630064536
