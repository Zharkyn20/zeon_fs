import os.path
import shutil
import sys


ALLOWED_COMMANDS = {'init': [0, 1], 'add': [1], 'ls': [0, 1], 'delete': [1],
                   'get': [2]}


def check_commands(commands=sys.argv):

    _, command, *args = commands

    if command not in ALLOWED_COMMANDS.keys():
        return 'Not allowed command!'

    command_len = ALLOWED_COMMANDS[command]
    if len(args) > max(command_len):
        return 'Extra useless arguments!'
    if len(args) < min(command_len):
        return 'You forgot to add more arguments!'

    return 'Satisfied amount of commands!'


def init(directory):
    if os.path.isdir(directory):
        return 'Already exists!'
    os.mkdir(directory)
    return 'Created!'


def list_files(path):
    files_list = os.listdir(f'{path}')
    return files_list


def add_file(from_path):
    os.system('cd test_assets/zeon_fs')
    file_name = os.path.basename(from_path)

    if not os.path.isfile(from_path):
        return 'Incorrect path!'
    if os.path.isfile(f'test_assets/zeon_fs/{file_name}'):
        return 'Already exists!'

    source = f'{from_path}'
    destination = 'test_assets/zeon_fs'
    shutil.copy(source, destination)
    return 'Successfully added!'


def delete_file(file_name):
    if not os.path.isfile(file_name):
        return 'Not Found!'

    os.remove(f'./{file_name}')
    return 'Successfully deleted!'


def get_file(file_name, from_path):
    if os.path.isfile(file_name):
        return 'This file already exists!'

    content = open(from_path, 'r')
    zeon_fs_file = open(f'{file_name}', 'x')
    zeon_fs_file.write(content.read())
    zeon_fs_file.close()
    content.close()
    return 'Content successfully copied!'


def help_me():
    help_text = " Available commands: \
    'init': , \
    'add': arguments -path, \
    'delete': arguments -file_name, \
    'list': , \
    'get': arguments -file_name, -path \
    "
    print(help_text)


commands_dict = {
    'init': init,
    'add': add_file,
    'delete': delete_file,
    'list': list_files,
    'get': get_file,
}

