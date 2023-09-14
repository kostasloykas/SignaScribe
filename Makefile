run:
	@python3 ./src/main.py -m 0 -sa eddsa25519 -pi 0x2389 -vi 0x2344 -ha sha256 \
	-f ./src/files/firmware.hex -c ./src/files/www.example.org.chained+root.crt 


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
