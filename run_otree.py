import re
import sys

from otree_startup import execute_from_command_line

if __name__ == '__main__':
    print("Andrew likes fish.")
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(execute_from_command_line())
