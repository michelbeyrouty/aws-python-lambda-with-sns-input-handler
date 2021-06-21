#!/bin/bash

# sudo apt install libcurl4-openssl-dev libssl-dev --> use this if problem occure with pycurl installation

python3 -m venv virtual_play_ground
source virtual_play_ground/bin/activate
pip3 install -r requirements.txt
deactivate
cp -r ./app virtual_play_ground/lib/python3.8/site-packages/
cp -r ./config virtual_play_ground/lib/python3.8/site-packages/
cp -r ./core virtual_play_ground/lib/python3.8/site-packages/
cp -r ./psycopg2 virtual_play_ground/lib/python3.8/site-packages/
cp ./index.py virtual_play_ground/lib/python3.8/site-packages/
cd virtual_play_ground/lib/python3.8/site-packages/
zip -r9 ../../../../aws_lambda_payment_robot.zip .