#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! [ -x "$(command -v nginx)" ]; then
  echo 'Installing Nginx...'
  apt-get update
  apt-get install -y nginx
fi

# - Create the folders, if they don't yet exist:
#   * '/data'
#   * '/data/web_static/'
#   * '/data/web_static/releases/'
#   * '/data/web_static/releases/test/'
#   * '/data/web_static/shared/'
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file '/data/web_static/releases/test/index.html',
# (with simple content, to test Nginx configuration)
printf '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tBest School\n\t</body>\n</html>\n' | tee /data/web_static/releases/test/index.html

# Create a symbolic link '/data/web_static/current' linked to the
# '/data/web_static/releases/test/' folder.
ln -sfT /data/web_static/releases/test/ /data/web_static/current

# Give recursive ownership of the '/data/' folder to the 'ubuntu' user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of '/data/web_static/current/'
# to 'hbnb_static' (ex: https://mydomainname.tech/hbnb_static).
sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
service nginx restart
