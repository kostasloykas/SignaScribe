run:
	@python3 ./src/main.py -mi 0 -sa eddsa -pi 0x2389 -vi 0x2344 -ht sha256 -f ./src/files/file.txt -c ./src/files/dummy.pem


setup:
	@pip install argparse cryptography


#github push 
push: .gitignore
	@git add . ;
	@git commit -m "update app";
	@git push;

#gitlab push 
gitlab_push: .gitignore
	@git push gitlab main;
