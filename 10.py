reg_x = 1
cycle = 1

#part one
# sig_strength_sum = 0

# with open('input10.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         if line[0:5] == 'addx ':
#             line_arr = line.split(' ')
#             if (cycle % 40) == 20:
#                 sig_strength_sum += cycle * reg_x
#             cycle += 1
#             if (cycle % 40) == 20:
#                 sig_strength_sum += cycle * reg_x
#             reg_x += int(line_arr[1])
#             cycle += 1
#         else:
#             if (cycle % 40) == 20:
#                 sig_strength_sum += cycle * reg_x
#             cycle += 1

# print(f"reg_x:{reg_x}, cycle:{cycle}, sig_str_sum:{sig_strength_sum}")

#part two
#40x6 px
cycle = 0
screen = ['']
def render_char():
    global screen, cycle, reg_x
    # new line
    if len(screen[len(screen)-1]) == 40:
        screen.append('')
    col = cycle % 40
    if abs(reg_x - col) <= 1:
        screen[len(screen)-1] += '#'
    else:
        screen[len(screen)-1] += '.'

def screen_display():
    global screen
    print('\n'.join(screen))

with open('input10.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line[0:5] == 'addx ':
            line_arr = line.split(' ')
            render_char()
            cycle += 1
            render_char()
            reg_x += int(line_arr[1])
            cycle += 1
        else:
            render_char()
            cycle += 1

screen_display()
