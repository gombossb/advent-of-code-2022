
pairs = []
with open('input4.txt') as f:
    lines = f.readlines()
    for line in lines:
        pair_arr = line.split(',')
        pair_arr[1] = pair_arr[1].strip() # \n
        first_range  = pair_arr[0].split('-')
        second_range  = pair_arr[1].split('-')
        pair = []
        pair.append(set(list(range(int(first_range[0]), int(first_range[1])+1))))
        pair.append(set(list(range(int(second_range[0]), int(second_range[1])+1))))
        pairs.append(pair)

count = 0
for pair in pairs:
    intsect = pair[0].intersection(pair[1])
    #part one
    # if intsect == pair[0] or intsect == pair[1]:
    #     count += 1 
    #part two
    if intsect != set([]):
        count += 1

print(count)
