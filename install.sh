
#!/bin/bash
echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Starting services..."
docker-compose up -d

echo "Done! Visit https://mafd.duckdns.org"
