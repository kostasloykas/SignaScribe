run:
	@python3 ./src/main.py -mi 0 -oi kostas.com -sa eddsa -pi 0x2389 -vi 0x2344 -ht sha256 \
	-f ./src/files/firmware.hex -c ./src/files/dummy.pem -p ./src/files/public_key.pem


setup:
	@pip install argparse cryptography certifi


#github push 
push: .gitignore
	@git add . ;
	@git commit -m "update app";
	@git push;

#gitlab push 
gitlab_push: .gitignore
	@git push gitlab main;
