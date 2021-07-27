import os
import requests
import shutil



key = 'https://raw.githubusercontent.com/ilyhalight/AkiRAR-Activator/master/rarreg.key'
default_dir = 'C:\Program Files\WinRAR'

def download(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def activate(dir):
    file_path = dir + '/rarreg.key'
    vote = ''
    if os.path.isfile(file_path):
        while True:
            print('Вероятно WinRAR уже активирован с помощью rarreg.key. Вы хотите перезаписать файл? [y/n]')
            vote = input('>>> ')
            if vote == 'y':
                try:
                    os.remove(file_path)
                except PermissionError:
                    print('Перезапустите программу с правами администратора')
                break
            elif vote == 'n':
                print('Вы отказались от перезаписи файла rarreg.key')
                break
            else:
                pass
    else:
        pass

    if vote == 'n':
        print(file_path, 'уже существует')
    else:
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

def deactivate(dir):
    file_path = dir + '/rarreg.key'
    vote = ''
    if os.path.isfile(file_path):
        while True:
            print('Вы уверены, что хотите деактивировать WinRAR? [y/n]')
            vote = input('>>> ')
            if vote == 'y':
                try:
                    os.remove(file_path)
                    print('WinRAR был успешно деактивирован')
                except PermissionError:
                    print('Перезапустите программу с правами администратора')
                break
            elif vote == 'n':
                print('Вы отказались от деактивации WinRAR')
                break
            else:
                pass
    else:
        print('Указан несуществующий путь.')

def check_deactivate():
    if os.path.isdir(default_dir):
        deactivate(default_dir)
    else:
        while True:
            print('Введите путь до папки WinRAR')
            dir = input('>>> ')
            if os.path.isdir(dir):
                break
            else:
                pass

        deactivate(dir)

def status():
    if os.path.isdir(default_dir):
        file_path = f'{default_dir}/rarreg.key'
        if os.path.isfile(file_path):
            print('Статус: Активирован')
        else:
            print('Статус: Не активирован')
    else:
        print('WinRAR установлен не в стандартную папку')

def check_activate():
    if os.path.isdir(default_dir):
        activate(default_dir)
    else:
        while True:
            print('Введите путь до папки WinRAR')
            dir = input('>>> ')
            if os.path.isdir(dir):
                break
            else:
                pass

        activate(dir)

def main():
    while True:
        os.system('cls||clear')
        print(f'Добро пожаловать в AkiRAR Activator.\nПрограмма была протестирована на версии WinRAR 6.02 (64-разрядная)\n\nВыберите действие:\n1) Проверить активацию (Работает, если WinRAR у вас установлен в {default_dir})\n2) Активировать WinRAR\n3) Деактивировать WinRAR\n4) Выйти')
        vote = input('>>> ')
        if vote == '1':
            status()
            break
        elif vote == '2':
            check_activate()
            break
        elif vote == '3':
            check_deactivate()
            break
        elif vote == '4':
            break
        else:
            pass

    input('Нажмите Enter для закрытия программы... ')

if __name__ == '__main__':
    if os.name == 'nt':
        main()
    else:
        print('Данная OS не поддерживается')