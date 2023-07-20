class AthleteList(list):
    def __init__(self, name, dob=None, times=[]) -> None:
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[:3])


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_data_from_file(file):
    try:
        with open(file) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print("File Error: " + err)
        return None


james = get_data_from_file('james2.txt')
mikey = get_data_from_file('mikey2.txt')
sarah = get_data_from_file('sarah2.txt')
julie = get_data_from_file('julie2.txt')

print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(james.name + "'s fastest times are: " + str(james.top3()))
