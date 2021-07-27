import os
import requests
import shutil
import time


key = 'https://raw.githubusercontent.com/ilyhalight/AkiRAR-Activator/master/rarreg.key'
default_dir = 'C:\Program Files\WinRAR'

def download(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def activate(dir):
    file_path = dir + '/rarreg.key'
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
        except PermissionError:
            print('Перезапустите программу с правами администратора')
    else:
        pass

    try:
        download(key)
    except:
        print('Проверьте соединение с интернетом')
    try:
        shutil.copy2('rarreg.key', dir)
    except PermissionError:
        print('Перезапустите программу с правами администратора')
    download_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'rarreg.key')
    try:
        os.remove(download_file)
    except:
        pass

    print('WinRAR был успешно активирован')


def check_activate():
    if os.path.isdir(default_dir):
        activate(default_dir)
    else:
        print('Папка WinRAR находится не в стандартном месте')

if __name__ == '__main__':
    if os.name == 'nt':
        check_activate()
        print('Выход...')
        time.sleep(3)
    else:
        print('Данная OS не поддерживается')
        time.sleep(3)