
import os

from commands import *


def helper_remove_added_dir(dir_name):
    os.rmdir(dir_name)


def helper_remove_added_file(file_name):
    os.remove(file_name)


def helper_add_removed_file(file_name):
    os.system(f'touch {file_name}')


def test_check_commands():
    arguments = ['main.py', 'add',
                 'test_resources/test1.txt']
    expected = 'Satisfied amount of commands!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'any command']
    expected = 'Not allowed command!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'add']
    expected = 'You forgot to add more arguments!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'ls']
    expected = 'Satisfied amount of commands!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'get', 'file_name']
    expected = 'You forgot to add more arguments!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'get', 'text.txt',
                 'test_resources/test2.txt']
    expected = 'Satisfied amount of commands!'
    actual = check_commands(arguments)
    assert expected == actual

    arguments = ['main.py', 'add',
                 'test_resources/test1.txt', 'extra_useless']
    expected = 'Extra useless arguments!'
    actual = check_commands(arguments)
    assert expected == actual


def test_init():
    arguments = 'test_assets/zeon_fs'
    assert os.path.isdir(arguments) is True
    expected = 'Already exists!'
    actual = init(arguments)
    assert expected == actual

    arguments = 'test_assets/zeon'
    assert os.path.isdir(arguments) is False
    expected = 'Created!'
    actual = init(arguments)
    assert expected == actual

    helper_remove_added_dir(arguments)


def test_list_files():
    arguments = 'test_assets'
    expected = ['zeon_fs']
    actual = list_files(arguments)
    assert expected == actual


def test_add_file():
    arguments = 'test_resources/test1.txt'
    expected = 'Successfully added!'
    actual = add_file(arguments)
    assert expected == actual

    helper_remove_added_file('test_assets/zeon_fs/test1.txt')

    arguments = 'test_resources/non_existing_file.txt'
    expected = 'Incorrect path!'
    actual = add_file(arguments)
    assert expected == actual

    arguments = 'test_resources/test_existing_file.txt'
    expected = 'Already exists!'
    actual = add_file(arguments)
    assert expected == actual


def test_delete_file():
    arguments = 'test_assets/zeon_fs/test_existing_file2.txt'
    expected = 'Successfully deleted!'
    actual = delete_file(arguments)
    assert expected == actual
    helper_add_removed_file(f'{arguments}')

    arguments = 'zeon_fs/non_existing_file.txt'
    expected = 'Not Found!'
    actual = delete_file(arguments)
    assert expected == actual


def test_get_file():
    arg1, arg2 = 'test_assets/zeon_fs/new_file_name.txt',\
                 'test_resources/test5.txt'
    expected = 'Content successfully copied!'
    actual = get_file(arg1, arg2)
    assert expected == actual

    arg1, arg2 = 'test_assets/zeon_fs/new_file_name.txt',\
                 'test_resources/test5.txt'
    expected = 'This file already exists!'
    actual = get_file(arg1, arg2)
    assert expected == actual
    helper_remove_added_file(f'{arg1}')
