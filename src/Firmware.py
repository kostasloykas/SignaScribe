from Utility_Functions import *
from Arguments import Arguments


class Firmware:
    data = None
    size = None
    type = None
    path = None

    def __init__(self, arguments: Arguments) -> None:
        assert arguments.firmware and arguments.firmware_type

        self.data = arguments.firmware.read()
        self.size = len(self.data)
        self.type = arguments.firmware_type
        self.path = arguments.firmware.name

        assert self.data and self.size and self.type and self.path

    pass
