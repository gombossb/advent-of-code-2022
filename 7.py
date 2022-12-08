root_dir = {'name': '/', 'files': [], 'dirs': []}
cwd = []

def cd(dest):
    global cwd
    if dest == '..':
        cwd.pop()
    elif dest == '/':
        cwd = []
    else:
        cwd.append(dest)

def mkfile(name, size):
    tmp_dir = root_dir
    for path in cwd:
        tmp_dir = tmp_dir.get('dirs')
        for d in tmp_dir:
            if d.get('name') == path:
                tmp_dir = d
                break
    tmp_dir.get('files').append({'name': name, 'size': size})

def mkdir(name):
    tmp_dir = root_dir
    for path in cwd:
        tmp_dir = tmp_dir.get('dirs')
        for d in tmp_dir:
            if d.get('name') == path:
                tmp_dir = d
                break
    tmp_dir.get('dirs').append({'name': name, 'files': [], 'dirs': []})

totalmax100k = 0
def dirsize_max100k(dir):
    global totalmax100k
    subdirs = 0
    for d in dir.get('dirs'):
        subdirs += dirsize_max100k(d)
    files = 0
    for f in dir.get('files'):
        files += f.get('size')
    if (subdirs + files) <= 100000:
        totalmax100k += files + subdirs
    return subdirs + files


with open('input7.txt') as f:
    lines = f.readlines()
    lsmode = False
    for line in lines:
        line = line.strip()
        #print(line)
        # line is a command
        if line[0] == '$':
            lsmode = False
            cmdline = line.split(' ')
            if cmdline[1] == 'cd':
                cd(cmdline[2])
            elif cmdline[1] == 'ls':
                lsmode = True
        elif lsmode:
            lsline = line.split(' ')
            if lsline[0] == 'dir':
                mkdir(lsline[1])
            else:
                mkfile(lsline[1], int(lsline[0])) # should only be in this format
#part one
#print(root_dir)
total_use = dirsize_max100k(root_dir)
print(total_use)
print(totalmax100k)
#part two
print('------------')
total = 70000000
required_unused = 30000000
must_be_freed = required_unused - (total - total_use)
print(must_be_freed)

min_found = total_use
def dir_to_delete(dir):
    global must_be_freed
    global min_found
    subdirs = 0
    for d in dir.get('dirs'):
        subdirs += dir_to_delete(d)
    files = 0
    for f in dir.get('files'):
        files += f.get('size')
    if (subdirs + files) >= must_be_freed and (subdirs + files) < min_found:
        min_found = subdirs + files
        print(dir.get('name'), min_found)
    #print(dir.get('name'), (subdirs+files))
    return subdirs + files

dir_to_delete(root_dir)
