#!/bin/bash
sudo apt -yq update
sudo apt -yq upgrade
sudo apt install -y python3-picamera2 --no-install-recommends
sudo apt install -y git
sudo apt install -y python3-pip
# Install Node
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt update
sudo apt install -y nodejs
# Install Yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn -y
# Clone repo
cd ~
echo "Downloading Hexa 3.0"
git clone https://github.com/henrytriplette/hexa-3.0
cd hexa-3.0