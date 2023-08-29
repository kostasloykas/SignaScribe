def DEBUG(*args):
    message = "".join(map(str, args))
    print("DEBUG:", message)


#  print error and terminate
def ERROR(*error):
    error_message = "".join(map(str, error))
    print("ERROR:", error_message)
    exit(0)
