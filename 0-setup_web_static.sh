#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must:
file_path="/data/web_static/releases/test/index.html"
if [ ! -e "$(type nginx)" ]
then
	sudo apt install -y nginx
fi

if [ ! -d "/data/web_static/releases/test" ]
then
	sudo mkdir -p /data/web_static/releases/test
fi

if [ ! -d "/data/web_static/shared" ]
then
	sudo mkdir -p /data/web_static/shared
fi

echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > "$file_path"

if [ ! -L "/data/web_static/current" ]
then
	sudo ln -s /data/web_static/releases/test /data/web_static/current
else
	sudo rm -f /data/web_static/current
	sudo ln -s /data/web_static/releases/test /data/web_static/current
fi
sudo chown -Rf "$USER":"$USER" /data

TEXT="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name localhost;/a $TEXT" /etc/nginx/sites-available/default

sudo service nginx start
