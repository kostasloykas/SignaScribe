from Arguments import Arguments
from Firmware import Firmware
import json
from OpenSSL import crypto
from Utility_Functions import *
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PublicKey
from cryptography.hazmat.primitives import serialization
from typing import Union

SUPPORTED_PUBLIC_KEYS = Union[Ed25519PublicKey, Ed448PublicKey]


class JSON:
    arguments = None
    firmware = None
    owner_certificate = None
    public_key = None

    def __init__(self, arguments: Arguments, firmware: Firmware, owner_certificate: crypto.X509, public_key: SUPPORTED_PUBLIC_KEYS) -> None:
        self.arguments = arguments
        self.firmware = firmware
        self.owner_certificate = owner_certificate
        self.public_key = public_key.public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode("utf-8")

        assert self.arguments and self.firmware and self.owner_certificate and self.public_key

    def __str__(self) -> str:
        return json.dumps(
            {"manifest_version": self.arguments.manifest_version, "common_name": self.owner_certificate.get_subject().CN,
             "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_algorithm": self.arguments.hash_algorithm, "sign_algorithm": {"type": self.arguments.sign_algorithm,
                                                                                 "public_key": self.public_key},
             "firmware_size": self.firmware.size, "firmware_type": self.firmware.type}, indent=5)

    pass
