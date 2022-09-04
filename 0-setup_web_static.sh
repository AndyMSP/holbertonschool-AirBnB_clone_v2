#!/usr/bin/env bash
# Sets up web server for deployment of web_static

# 1) Install nginx if not already
# 2) Create directory structure
# 3) Create test HTML files
# 4) Create symbolic link, replace if already existing
# 5) Change owner and group of /data/ recursively to ubuntu
# 6) Configure nginx and alias hbnb_static to /data/web_static/current/
# 7) Reload nginx server

#1
apt -y update
apt -y install nginx

#2
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

#3
echo "Holberton School" > /data/web_static/releases/test/index.html
echo "Holberton School root index page" > /data/web_static/index.html

#4
ln -sf /data/web_static/releases/test/ /data/web_static/current

#5
chown -R ubuntu:ubuntu /data/

#6
rm -f /etc/nginx/conf.d/tacobell.conf
rm -f /etc/nginx/sites-enabled/default
echo \
"server{
	listen 80;
	root /data/web_static/;
	index index.html;

	add_header X-Served-By $HOSTNAME;

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}" \
> /etc/nginx/conf.d/tacobell.conf

#7
service nginx restart
