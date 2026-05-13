import traceback
import sys
from .db import search
from .ai import GeminiSearch
def parser(filename):
    try:
        with open(filename, "r") as f:
            code = f.read()
        try:
            compiled_code = compile(code, filename, "exec")
            exec(compiled_code)
        except Exception:
            traceback.print_exc()
            formated = traceback.format_exc().split('\n')
            errorType = formated[-2].split(":")
            errorName = errorType[0]
            errorData = search(errorName)
            if not errorData:

    except Exception as e:
        print(e)
        sys.exit(1)

