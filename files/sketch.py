man = []
other = []
try:
    data = open('./files/sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('file not found')

try:
    man_file = open("man_data.txt", mode="w+")
    other_file = open("other_data.txt", mode="w+")
    print(man, file=man_file)
    print(other, file=other_file)
    man_file.close()
    other_file.close()

except IOError:
    print("error opening file")
