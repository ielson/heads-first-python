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
        return (data.strip().split(','))
    except IOError as err:
        print("File Error: " + err)
        return None


james = get_data_from_file('james.txt')
mikey = get_data_from_file('mikey.txt')
sarah = get_data_from_file('sarah.txt')
julie = get_data_from_file('julie.txt')

james = sorted([sanitize(each_t) for each_t in james])
mikey = sorted([sanitize(each_t) for each_t in mikey])
julie = sorted([sanitize(each_t) for each_t in julie])
sarah = sorted([sanitize(each_t) for each_t in sarah])

print(sorted(set(james))[:3])
print(sorted(set(julie))[:3])
print(sorted(set(mikey))[:3])
print(sorted(set(james))[:3])