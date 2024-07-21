import json
from types import SimpleNamespace

def __getParsedJson(dataList):
    parsedData = json.loads(dataList, object_hook=lambda d: SimpleNamespace(**d))
    return parsedData