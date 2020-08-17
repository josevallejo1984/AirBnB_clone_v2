#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must:
file_path="/data/web_static/releases/test/index.html"
if ! which nginx > /dev/null
then
	sudo apt-get -y update
	sudo apt-get -y install -y nginx
fi
# create folder recursive if not exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# create a fake file html
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > "$file_path"
# create simbolic link
sudo ln -s /data/web_static/releases/test /data/web_static/current
# change ownership to folder /data and all you content
sudo chown -Rh ubuntu:ubuntu /data/
# config default file nginx for server to aliases
udo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# start nginx service
sudo service nginx start
