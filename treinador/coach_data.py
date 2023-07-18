import pathlib

current_directory = pathlib.Path(__file__)


def get_txt_files(folder=current_directory):
    parent_directory = folder.parent
    print("current: " + str(parent_directory)) 
    txt_list = list(pathlib.Path(parent_directory).glob('*.txt'))
    print("files: " + str(txt_list))
    return txt_list


for file in get_txt_files():
    with open(file) as athlete_file:
        athlete_data = athlete_file.readline()
    athlete_data = athlete_data.strip().split(',')
    athlete_name = file.name.split('.')[0]
    exec(f"{athlete_name} = athlete_data")