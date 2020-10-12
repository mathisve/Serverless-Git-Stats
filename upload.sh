#!/usr/bin/env bash
# Mathis Van Eetvelde
# Script to automatically install dependencies, zip files and upload them to AWS

python3 -V
pip3 -V

echo "Installing Python3 Dependencies from requirements.txt"
rm -rf package
mkdir package
pip3 install --quiet --target ./package -r requirements.txt --upgrade

echo "Adding /modules to archive.zip"
zip --quiet -r9 archive.zip modules

echo "Adding /package to archive.zip"
cd package
zip --quiet -r9 ../archive.zip .
cd ..

echo "Adding main.py to archive.zip"
zip -g --quiet archive.zip main.py

echo "Uploading archive.zip to AWS"
aws lambda update-function-code --function-name git-stats --zip-file fileb://archive.zip
