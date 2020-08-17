#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must:
file_path="/data/web_static/releases/test/index.html"
if ! which nginx > /dev/null
then
	sudo apt-get -y update
	sudo apt-get -y install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > "$file_path"

sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -Rh ubuntu:ubuntu /data

udo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
