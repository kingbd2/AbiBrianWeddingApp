#!/usr/bin/env bash

npm run generate

echo "Removing previous distribution build..."
sudo rm -rd /var/www/html/Vue/dist/
echo "Removed previous distribution build!"

echo "Copying new distribution build..."
sudo cp -r dist/ /var/www/html/Vue
echo "Added new distribution build!"