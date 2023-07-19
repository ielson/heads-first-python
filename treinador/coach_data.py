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
        return {'name': temp.pop(0), 'dob': temp.pop(0), 'times': str(sorted(set(sanitize(t) for t in temp))[:3])}
    except IOError as err:
        print("File Error: " + err)
        return None


james = get_data_from_file('james2.txt')
mikey = get_data_from_file('mikey2.txt')
sarah = get_data_from_file('sarah2.txt')
julie = get_data_from_file('julie2.txt')

print(sarah['name'] + "'s fastest times are: " + sarah['times'])
