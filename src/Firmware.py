from Utility_Functions import *
from Arguments import Arguments


class Firmware:
    data = None
    size = None
    type = None

    SUPPORTED_EXTENTIONS = ["hex", "bin", "zip"]

    def __init__(self, arguments: Arguments) -> None:
        assert arguments.firmware

        self.data = arguments.firmware.read()
        self.size = len(self.data)
        # firmware type
        self.type = self.__TakeFirmwareExtention(
            arguments.firmware.name)

        assert self.data and self.size and self.type

    def __TakeFirmwareExtention(self, firmware_name: str) -> str:
        extention = firmware_name.split(".").pop()

        if not extention in self.SUPPORTED_EXTENTIONS:
            ERROR("Not supported extention of firmware file",
                  "SUPPORTED EXTENTIONS --->", self.SUPPORTED_EXTENTIONS)
        return extention

    pass
