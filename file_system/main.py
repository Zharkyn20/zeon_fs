from commands import *

_, command, *args = sys.argv
check_commands(sys.argv)
commands_dict[command](*args)
