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


james = get_data_from_file('james2.txt')
mikey = get_data_from_file('mikey2.txt')
sarah = get_data_from_file('sarah2.txt')
julie = get_data_from_file('julie2.txt')

sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['dob'] = sarah.pop(0)
sarah_data['times'] = sarah

print(sarah_data['name']+ "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['times']]))[:3]))
