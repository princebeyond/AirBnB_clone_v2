static_dir="/data/web_static"
release_dir="$static_dir/releases/test"
current_dir="$static_dir/current"
nginx_config="/etc/nginx/sites-enabled/default"

# Create directory structure
mkdir -p "$release_dir"
mkdir -p "$static_dir/shared"

# Create index.html with test content
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | tee "$release_dir/index.html" > /dev/null

# Create symbolic link
ln -sf "$release_dir" "$current_dir"

# Set ownership
chown -R ubuntu:ubuntu "$static_dir"

# Add location block to Nginx configuration
sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' "$nginx_config"

# Restart Nginx
service nginx restart
