# SignaScribe

This app takes as input a firmware file for IoT devices (e.g., Contiki OS), a x509 certificate chain, vendor ID, product ID, hash algorithm, and a signature algorithm.
It can be used by anyone who wants to produce their own firmwares and securely flash them in Tilergatis. After validating the certificate chain, we create a signature 
using either the eddsa25519 or ed448 signature algorithm and import these files into a zip archive for flashing with the Tilergatis flash application.
  

How to run script:
    python3 ./src/main.py -sa eddsa25519 -pi 0x2389 -vi 0x2344 -ha sha256 -f ./src/files/firmware.hex -c ./src/files/certificate_chain.pem 

For help:
    python3 ./src/main.py -h
