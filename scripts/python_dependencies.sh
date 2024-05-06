#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install --upgrade setuptools wheel 
pip install setuptools==58.2.0
sudo apt-get install libmysqlclient-dev
pip install -r /home/ubuntu/LMS/requirements.txt