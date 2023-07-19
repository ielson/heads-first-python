def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


with open('james.txt') as jaf: data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf: data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif: data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf: data = saf.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(each_t) for each_t in james])
mikey = sorted([sanitize(each_t) for each_t in mikey])
julie = sorted([sanitize(each_t) for each_t in julie])
sarah = sorted([sanitize(each_t) for each_t in sarah])

print(sorted(set(james))[:3])
print(sorted(set(julie))[:3])
print(sorted(set(mikey))[:3])
print(sorted(set(james))[:3])