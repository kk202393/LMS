#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install --upgrade setuptools wheel 
sudo apt-get install mysql-server
pip install -r /home/ubuntu/LMS/requirements.txt