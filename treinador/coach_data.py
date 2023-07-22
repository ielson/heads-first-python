import pickle

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


def put_to_store(files_list):
    all_ath = {}
    for each_file in files_list:
        ath = get_data_from_file(each_file)
        all_ath[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as ath_pickle:
            pickle.dump(all_ath, ath_pickle)
    except IOError as err:
        print('File error: ' + err)
    return (all_ath)


def get_from_store():
    all_ath = {}
    try:
        with open('athletes.pickle', 'rb') as ath_file:
            all_ath = pickle.load(ath_file)
    except IOError as err:
        print('File error: ' + err)
    return all_ath
