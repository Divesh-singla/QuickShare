# message viewer
SUCCESS = "SUCCESS"
FAILURE = "FAILURE"
PROCESSING = "PROCESSING"
ALREADYEXIST = "ALREADY EXIST"

def get_message(type):
    if type == SUCCESS:
        return "File Saved"

    elif type == FAILURE:
        return "Process Failed due to Some Error !"

    elif type == PROCESSING:
        return "Processing"

    elif type==ALREADYEXIST:
        return "File Updated"


# print(get_message(FAILURE))