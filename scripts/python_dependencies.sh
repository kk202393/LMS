#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install --upgrade setuptools wheel 
sudo apt install python3-dev default-libmysqlclient-dev build-essential
sudo apt-get install libmysqlclient-dev
pip install -r /home/ubuntu/LMS/requirements.txt