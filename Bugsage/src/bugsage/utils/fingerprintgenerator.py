import hashlib
def generateErrorTypeFingerprint(errorType,model_version):
    data = f"{errorType}{model_version}"
    return hashlib.sha256(data.encode("utf-8")).hexdigest()
def generateErrorCaseFingerprint(errorCase,model_version,ErrorTypeId):
    data = f"{errorCase}{ErrorTypeId}{model_version}"
    return hashlib.sha256(data.encode("utf-8")).hexdigest()