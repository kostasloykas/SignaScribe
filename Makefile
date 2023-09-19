help:
	@python3 ./src/main.py -h

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
