elves = []
i = 0
with open('input1.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line in ('\n', '\r\n'):
            i += 1
            continue
            # break

        elf = ""
        # empty at index
        if i >= len(elves):
            elf = {'total_calories': 0, 'calories': []}
        else:
            elf = elves[i]
            
        elf['calories'].append(int(line))
        elf['total_calories'] = sum(elf['calories'])

        if i >= len(elves):
            elves.append(elf)
        else:
            elves[i] = elf

        # print(i, elf)

max_calorie = 0  
for elf in elves:
    if elf['total_calories'] > max_calorie:
        max_calorie = elf['total_calories']
#print(max_calorie)

calories = []
for elf in elves:
    calories.append(elf['total_calories'])
calories.sort(reverse=True)
print(calories)
