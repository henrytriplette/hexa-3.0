#!/bin/bash
sudo apt-get -yq update
cd ~
echo "Updating Hexa 3.0"
cd hexa-3.0
git pull https://github.com/henrytriplette/hexa-3.0
# sudo cp config.ini.sample config.ini
# sudo systemctl restart hexa-3.0