def __getConvertedFileSize(filesize):
    # currenty acccepting the Byte

    if filesize < 1024:
        return f"{filesize} B"
    elif filesize < 1024**2:
        size_in_kb = filesize / 1024
        return f"{size_in_kb:.2f} KB"
    elif filesize < 1024**3:
        size_in_mb = filesize / 1024**2
        return f"{size_in_mb:.2f} MB"
    elif filesize < 1024**4:
        size_in_gb = filesize / 1024**3
        return f"{size_in_gb:.2f} GB"
    else:
        size_in_tb = filesize / 1024**4
        return f"{size_in_tb:.2f} TB"