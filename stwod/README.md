# STWOD

## Get started
Clone and make sure docker and docker-compose are installed.
	
	docker-compose up
	docker build -t dapc11/stwod . && clear && docker run --rm --network host -it dapc11/stwod:latest stwod.py -s 5
