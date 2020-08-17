#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must:
if ! which nginx > /dev/null
then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
# create folder recursive if not exist
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
# create a fake file html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# create simbolic link and re-create if exit (option f forced)
ln -sf /data/web_static/releases/test /data/web_static/current
# change ownership to folder /data and all you content
sudo chown -Rh ubuntu:ubuntu /data/
# config default file nginx for server to aliases
udo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# start nginx service
sudo service nginx start
