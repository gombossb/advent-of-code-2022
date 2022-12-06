def marker_end(s):
    if len(s)>5:
        for i in range(0, len(s)-3):
            window = s[i:i+4]
            print(window)
            if len(set(list(window))) == 4:
                return i+4

def start_of_msg(s):
    for i in range(0, len(s)-14):
        window = s[i:i+14]
        print(window)
        if len(set(list(window))) == 14:
            return i+14

#part one
#print(marker_end('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))
#print(marker_end(open('input6.txt').readlines()[0].strip()))
#part two
#print(start_of_msg('bvwbjplbgvbhsrlpgdmjqwftvncz'))
print(start_of_msg(open('input6.txt').readlines()[0].strip()))
