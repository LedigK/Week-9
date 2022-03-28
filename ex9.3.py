#Ex 9.3
dict = dict()
fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be found:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dict:
            dict[words[1]] = 1
        else:
            dict[words[1]] += 1

print(dict)   
