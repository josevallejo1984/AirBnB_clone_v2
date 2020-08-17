#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must:
file_path="/data/web_static/releases/test/index.html"
if [ ! -e "$(type nginx)" ]
then
	sudo apt install -y nginx
fi

if [ ! -d "/data/web_static/releases/test" ]
then
	mkdir -p /data/web_static/releases/test
fi

if [ ! -d "/data/web_static/shared" ]
then
	mkdir -p /data/web_static/shared
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
	ln -s /data/web_static/releases/test /data/web_static/current
else
	rm -f /data/web_static/current
	ln -s /data/web_static/releases/test /data/web_static/current
fi
sudo chown "$USER":"$USER" /data -R

TEXT="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name localhost;/a $TEXT" /etc/nginx/sites-available/default

sudo service nginx restart
