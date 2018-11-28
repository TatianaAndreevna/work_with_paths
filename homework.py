import os


Migrations = 'Migrations'


def list_all_files():
    files = os.listdir(Migrations)
    files = [os.path.join(Migrations, file) for file in files if os.path.isfile(os.path.join(Migrations, file))]
    # for file in files:
    #     path = os.path.join(Migrations, file)
    #     if os.path.isfile(os.path.join(Migrations, file)):
    #         print(path)
    return files


def list_files_sql():
    list_files = list_all_files()
    files_sql = list()
    for file in list_files:
        if file.endswith('.sql'):
            files_sql.append(file)
    return files_sql


def find_by_content():
    list_file = list_files_sql()
    while True:
        search = input('Введите строку:')
        list_find_file = list()
        for files in list_file:
            with open(os.path.join(files)) as f:
                if search in f.read():
                    list_find_file.append(files)
                    print(files)
        print('Найдено файлов: {}'.format(len(list_find_file)))
        list_file = list_find_file


if __name__ == '__main__':
    find_by_content()