def common_char(rucksackline):
    lineLen = len(rucksackline)
    firstCompartment = rucksackline[0:lineLen//2]
    secondCompartment = rucksackline[lineLen//2:]
    # print(rucksackline, firstCompartment, secondCompartment)
    return ''.join(set(firstCompartment).intersection(secondCompartment))

def char_prio(c):
    # print(c)
    if (c >= 'a' and c <= 'z'):
        return ord(c)-ord('a')+1
    elif (c >= 'A' and c <= 'Z'):
        return ord(c)-ord('A')+27
    else:
        return 0

def common_char_of_3_lines(line1, line2, line3):
    return ''.join(set(line1).intersection(line2).intersection(line3))

prio_sum = 0
# part one
# with open('input3.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         prio_sum += char_prio(common_char(line.strip()))
        #print(common_char(line.strip()))

# part two
with open('input3.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        prio_sum += char_prio(common_char_of_3_lines(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()))

print(prio_sum)
