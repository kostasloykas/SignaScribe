class Signature:
    def __init__(self) -> None:
        pass

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("Signature file saved")
        return

    pass
