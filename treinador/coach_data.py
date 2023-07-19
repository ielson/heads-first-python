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

unique_james = []
for time in james:
    if not time in unique_james:
        unique_james.append(time)
print(unique_james)

unique_james = []
for time in james:
    if not time in unique_james:
        unique_james.append(time)
print(unique_james)

unique_james = []
for time in james:
    if not time in unique_james:
        unique_james.append(time)
print(unique_james)

unique_sarah = []
for time in sarah:
    if not time in unique_sarah:
        unique_sarah.append(time)
print(unique_sarah)