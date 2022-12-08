mx = []
with open('input8.txt') as f:
    for line in f:
        line = line.strip()
        row = []
        for c in line:
            row.append(int(c))
        mx.append(row)
mx_size = len(mx) # should be an kxk mx which is true (99x99)

def is_visible(row, col):
    # if on the edge
    if row == 0 or col == 0 or row == mx_size-1 or col == mx_size-1:
        return True
    # left to right
    left_to_right = True
    for i in range(0, col):
        if mx[row][i] >= mx[row][col]:
            left_to_right = False
            break
    # top to bottom
    top_to_bottom = True
    for i in range(0, row):
        if mx[i][col] >= mx[row][col]:
            top_to_bottom = False
            break
    # right to left
    right_to_left = True
    for i in range(mx_size-1, col, -1):
        if mx[row][i] >= mx[row][col]:
            right_to_left = False
            break
    # bottom to top
    bottom_to_top = True
    for i in range(mx_size-1, row, -1):
        if mx[i][col] >= mx[row][col]:
            bottom_to_top = False
            break
    return left_to_right or top_to_bottom or right_to_left or bottom_to_top

#part one
total_visible = 0
for row in range(0, mx_size):
    for col in range(0, mx_size):
        if is_visible(row, col):
            total_visible += 1
print(total_visible)
print('-----------')

#part two
def scenic_score(row, col):
    # if on the edge
    if row == 0 or col == 0 or row == mx_size-1 or col == mx_size-1:
        return 0
    
    to_left = 0
    for i in range(col-1, -1, -1):
        to_left += 1
        if mx[row][i] >= mx[row][col]:
            break
    
    to_top = 0
    for i in range(row-1, -1, -1):
        to_top += 1
        if mx[i][col] >= mx[row][col]:
            break
    
    to_right = 0
    for i in range(col+1, mx_size):
        to_right += 1
        if mx[row][i] >= mx[row][col]:
            break
    
    to_bottom = 0
    for i in range(row+1, mx_size):
        to_bottom += 1
        if mx[i][col] >= mx[row][col]:
            break
    
    return to_left * to_top * to_right * to_bottom

max_scenic_score = 0
for row in range(0, mx_size):
    for col in range(0, mx_size):
        if scenic_score(row, col) > max_scenic_score:
            max_scenic_score = scenic_score(row, col)

print(max_scenic_score)
