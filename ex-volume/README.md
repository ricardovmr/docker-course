#In this file my main objective is to demonstrate my attempt to map a port in a container. 
#On this example we going to map the port 80(http) on a nginx server so the user can access from outside.

docker container run -p(port) 8080(exposes that port for the user access):80(internal port that nginx starts by default) nginx(image to be downloaded). 

#To access Nginx page go to any browser and type http://localhost:8080 or your ip.
