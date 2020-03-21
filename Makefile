IMAGE_NAME=nybscrapper

dbuild:
	docker build -t ${IMAGE_NAME} .

dup:
	docker run -it -v ${shell pwd}/src/:/code -w /code ${IMAGE_NAME} /bin/bash