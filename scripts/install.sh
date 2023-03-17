#!/bin/bash
sudo apt-get -yq update
sudo apt install -y python3-picamera2 --no-install-recommends
sudo apt install -y git
cd ~
echo "Downloading Hexa 3.0"
git clone https://github.com/henrytriplette/hexa-3.0
cd hexa-3.0