#!/usr/bin/env bash
# This script sets up webservers for the deployment of web static

# install nginx
sudo apt-get -y update
sudo apt-get install -y nginx

# create the folders
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/

# create html page
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# symbolic link to link two folders
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a \
	location /hbnb_static/ { \
		alias /data/web_static/current/; \
	}' /etc/nginx/sites-available/default

sudo service nginx restart
