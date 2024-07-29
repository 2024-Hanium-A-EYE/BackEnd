#!/bin/bash

# update system
sudo apt update && sudo apt install figlet -y

figlet Welcome To
figlet AEYE Back

# install dependencies
sudo pip install -r dependencies.txt

# run server
figlet Start Server
cd AEYE_Back_3_2
python manage.py runserver



