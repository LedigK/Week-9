#Ex 9.1
count = 0
dict = dict()
fhand = open('words.txt')

for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dict:
            continue
        dict[word] = count

if 'programs' in dict:
    print('True')
else:
    print('False')
