#Criando e mapeando um volume no apache.

docker container run -dit --name test-apache2 -p 8080:80 -v $(pwd)/htdocs:/usr/local/apache2/htdocs/ httpd:2.4
