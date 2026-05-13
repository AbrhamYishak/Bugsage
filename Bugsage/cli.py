# myrunner
#!/usr/bin/env python3

import sys
from .parser import parser
if len(sys.argv) < 2:
    print("Usage: Bugsage <python_file>")
    sys.exit(1)

file_name = sys.argv[1]
parser(file_name)

