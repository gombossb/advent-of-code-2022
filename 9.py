visited_locations = set()
def add_loc(tail):
    global visited_locations
    visited_locations.add(str(tail))

head = [0, 0]
tail = [50, 50]
add_loc(tail)

def head_tail_touching(head, tail):
    return (head[0]==tail[0] and head[1]==tail[1]) or (
        [0,1].count(abs(head[0]-tail[0])) > 0 and [0,1].count(abs(head[1]-tail[1])) > 0
    )

def move_head(dir, length):
    global head, tail
    for i in range(0, length):
        if dir == 'L':
            head = [head[0], head[1]-1]
            if not head_tail_touching(head, tail):
                tail = [head[0], tail[1]-1]
                add_loc(tail)
        elif dir == 'U':
            head = [head[0]-1, head[1]]
            if not head_tail_touching(head, tail):
                tail = [tail[0]-1, head[1]]
                add_loc(tail)
        elif dir == 'R':
            head = [head[0], head[1]+1]
            if not head_tail_touching(head, tail):
                tail = [head[0], tail[1]+1]
                add_loc(tail)
        elif dir == 'D':
            head = [head[0]+1, head[1]]
            if not head_tail_touching(head, tail):
                tail = [tail[0]+1, head[1]]
                add_loc(tail)

with open('input9.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line_arr = line.split(' ')
        move_head(line_arr[0], int(line_arr[1]))

print(head, tail)
print(len(visited_locations))
