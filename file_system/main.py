from commands import *

_, command, *args = sys.argv

if command in commands_dict.keys():
    check_commands(sys.argv)
    commands_dict[command](*args)
else:
    help_me()