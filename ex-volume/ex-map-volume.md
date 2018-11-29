#Example that demostrate a simple volume maping between host and container

docker container run -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx

#The flag -v is to refer the volume that we want to map 

#The $(pwd) parameter is to say to the system look for a subfolder inside the current directory that call "html"

#After the ":" i know this folder points to the folder where nginx reads the default index file. I want nginx to stop pointing to its default folder and point it to my html folder that I just created.
