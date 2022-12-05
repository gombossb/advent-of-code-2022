stacks = []
for i in range(0, 10):
    stacks.append([])
# use stack number for index, such that 0 remains empty and unused
# too lazy to write parser for initial stacks
stacks[1] = ['N', 'S', 'D', 'C', 'V', 'Q', 'T']
stacks[2] = ['M', 'F', 'V']
stacks[3] = ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M']
stacks[4] = ['D', 'Q', 'R', 'T', 'F']
stacks[5] = ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B']
stacks[6] = ['C', 'F', 'G', 'N', 'P', 'W', 'Q']
stacks[7] = ['W', 'F', 'R', 'L', 'C', 'T']
stacks[8] = ['T', 'Z', 'N', 'S']
stacks[9] = ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']
#print(stacks)

def crane(qty, source, target):
    for i in range(0, qty):
        tmp = stacks[source].pop()
        stacks[target].append(tmp)

def cranev2(qty, source, target):
    tmpstack = []
    for i in range(0, qty):
        tmpstack.append(stacks[source].pop())
    for i in range(0, qty):
        stacks[target].append(tmpstack[len(tmpstack)-1-i])

def print_top():
    for i in range(1, 10):
        print(stacks[i][len(stacks[i])-1], end='')
    print()

with open('input5.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue
        line_arr = line.split(' ')
        #crane(int(line_arr[1]), int(line_arr[3]), int(line_arr[5]))
        cranev2(int(line_arr[1]), int(line_arr[3]), int(line_arr[5]))

print(stacks)
print_top()