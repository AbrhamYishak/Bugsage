import traceback
import sys
from ..database.db import search
from ..ai.ai import GeminiSearch
from ..cli.bugsagecommunity import BugsageCommunity
# from ..templates.format import format
# from ..templates.format import save
# from .inspector import codetree
def parser(filename,ai=False, statusCallBack=None):
    try:
        with open(filename, "r") as f:
            code = f.read()
            # codetree(code)
        try:
            compiled_code = compile(code, filename, "exec")
            exec(compiled_code)
        except Exception:
            # traceback.print_exc()
            error = traceback.format_exc()
            if ai:
                status,message,model_version = GeminiSearch(error,code)
                
                return (True,status,message,model_version)
            else:
                formated = error.split('\n')
                errorType = formated[-2].split(":")
                errorName = errorType[0]
                errorCase = errorType[1].strip()
                errorData = search(errorName,errorCase)
                if not errorData:
                    found,response = BugsageCommunity(errorCase,errorName)
                    if not found:
                        if statusCallBack:
                            statusCallBack("🤖 Asking AI ... ","dots")
                        status,message,model_version = GeminiSearch(error,code)
                        return (True,status,message,model_version)
                    return (False,True,response,None)
    except Exception as e:
        print(e)
        sys.exit(1)

