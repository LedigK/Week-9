#Ex 9.5
dict = dict()

fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in dict:
            dict[domain] = 1
        else:
            dict[domain] += 1

print(dict)
