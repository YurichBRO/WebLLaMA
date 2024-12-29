def truncate(string, length):
    if len(string) > length:
        return string[:length-1] + '…'
    return string