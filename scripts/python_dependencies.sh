#!/usr/bin/env bash

virtualenv /home/ubuntu/LMS/env
source /home/ubuntu/env/bin/activate
pip install --upgrade setuptools wheel 
sudo apt-get install libmysqlclient-dev
sudo apt install libmysqlclient-dev
pip install mysqlclient==2.0.3
pip install -r /home/ubuntu/LMS/requirements.txt