$!/bin/bash

echo 'start'
sudo apt-get update
sudo apt-get install default-jdk
sudo apt-get install -y --no-install-recommends libreoffice libfontconfig1 libfreetype6 libx11-6 libxrender1 libxrender1 libxrender1 libxext6 libxcb1 libxcb1 libuuid1
sudo rm -rf /var/lib/apt/lists/*