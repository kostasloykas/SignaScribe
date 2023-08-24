run:
	@python3 ./src/main.py -sd 2023-05-05


setup:

#github push 
push: .gitignore
	@git add . ;
	@git commit -m "update app";
	@git push;

#gitlab push 
gitlab_push: .gitignore
	@git push gitlab main;
