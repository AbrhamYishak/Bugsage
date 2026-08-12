import traceback
import sys
from bugsage.database.db import search
from bugsage.ai.ai import aiSearch
from bugsage.cli.bugsagecommunity import BugsageCommunity
from bugsage.exceptions import NoInternetError, APIKeyError
# from ..templates.format import format
# from ..templates.format import save
# from .inspector import codetree
def parser(filename,ai=False, statusCallBack=None):
    try:
        with open(filename, "r") as f:
            code = f.read()
        try:
            compiled_code = compile(code, filename, "exec")
            exec(compiled_code)
        except Exception:
            error = traceback.format_exc()
            if ai:
                try:
                    status,message,model_version = aiSearch(error,code)
                    return (True,status,message,model_version)
                except APIKeyError as e:
                    raise APIKeyError(e)
            else:
                formated = error.split('\n')
                errorType = formated[-2].split(":")
                errorName = errorType[0]
                errorCase = errorType[1].strip()
                errorData = search(errorName,errorCase)
                if not errorData:
                    try:
                        found,response = BugsageCommunity(errorCase,errorName)
                        if not found:
                            if statusCallBack:
                                statusCallBack("🤖 Asking AI ... ","dots")
                            try:
                                status,message,model_version = aiSearch(error,code)
                                return (True,status,message,model_version)
                            except APIKeyError as e:
                                raise APIKeyError(e)
                        return (False,True,response,None)
                    except NoInternetError as e:
                        raise NoInternetError("No Internet Connection")
    except Exception as e:
        print(e)
        sys.exit(1)

