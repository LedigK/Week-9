#Ex 9.4
dict = dict()
maximum = 0
max_address = ''

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dict:
        dict[words[1]] = 1
    else:
        dict[words[1]] += 1

for address in dict:
    if dict[address] > maximum:
        maximum = dict[address]
        max_address = address

print(max_address, maximum)
