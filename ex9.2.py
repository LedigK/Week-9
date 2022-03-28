#Ex 9.2
dict = dict()
fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dict:
            dict[words[2]] = 1
        else:
            dict[words[2]] += 1

print(dict)
