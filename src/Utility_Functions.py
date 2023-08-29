def DEBUG(*args):
    message = "".join(map(str, args))
    print("DEBUG:", message)


#  print error and terminate
def ERROR(*error):
    print("ERROR:", error)
    exit(0)
