import pickle

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
    # with open(X) as Y, open(W) as Z:
    with open("man_data.txt", mode="wb") as man_file:
        pickle.dump(man, man_file)
    with open("other_data.txt", mode="wb") as other_file:
        pickle.dump(other, other_file)

except pickle.PickleError as err:
    print("File error: " + err)
