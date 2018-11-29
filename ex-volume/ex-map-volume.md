#Example that demostrate a simple volume maping between host and container

docker container run -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx


#The flag -v is for reference the volume that we want to map 

#The $(pwd) parameter
