from Utility_Functions import *
from Arguments import Arguments
# FIXME: class Firmware


class Firmware:

    size = None
    type = None

    def __init__(self, arguments: Arguments) -> None:
        assert arguments.firmware and arguments.firmware_type

        self.size = len(arguments.firmware)
        self.type = arguments.firmware_type

        DEBUG(self.size, self.type)
        assert self.size and self.type

    pass
