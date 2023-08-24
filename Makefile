run:
	@python3 ./src/main.py 


setup:

#github push 
push: .gitignore
	@git add . ;
	@git commit -m "update app";
	@git push;

#gitlab push 
gitlab_push: .gitignore
	@git push gitlab main;
