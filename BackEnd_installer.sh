#!/bin/bash

RED='\033[38;5;196m'
GREEN='\033[38;5;82m'
YELLOW='\033[38;5;226m'
BLUE='\033[38;5;81m'
NC='\033[0m' # No Color (Defualt colour)

##################################################################
install_status_vel=1

total_progress=4

print_AEYE_WEB() {
  clear
  figlet Welcome To
  figlet AEYE WEB 
}

initialize_system() {
  clear
  echo "Updating system package list..."
  sudo apt update
  sudo apt install -y
  
  if [ $? -eq 0 ]; then
    install_status_vel=0
    echo "System package list updated successfully."
    echo -e "${BLUE}[0/$total_progress] ${NC}Install figlet..."
    sudo apt install figlet -y
    
    if [ $? -eq 0 ]; then
      clear
      print_AEYE_WEB
    else
      install_status_vel=1
      echo -e "${RED}[0/$total_progress] Failed to install." ${NC}
    fi
    
  else
    echo ${RED}"Failed to update system package list."${NC}
  fi
}

initialize_system

########################################################################

uninstall_docker() {
  sudo systemctl stop docker.socket
  sudo systemctl disable docker.socket
  sudo systemctl stop docker.service

  dpkg -l | grep -i docker 
  sudo apt-get purge -y docker-*
  sudo apt-get purge -y python3-docker*
  
  dpkg -l | grep -i docker 

  sudo rm -rf /var/lib/docker* /etc/docker*
  sudo rm -rf /var/run/docker.sock /var/run/dockershim.sock /var/run/docker.pid
  sudo rm -rf /var/lib/dockershim /var/run/docker /var/run/dockershim.sock
  sudo apt purge -y docker-ce docker-ce-cli containerd.io

}

install_docker () {
  
  sudo apt-get update
  sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt-get update
    
  if [ $? -eq 0 ]; then
    
    sudo apt-get -y install docker-ce docker-ce-cli containerd.io
  else
    install_status_vel=1
    echo -e "${RED}[2/$total_progress] ${NC}Failed to install docker"
  fi
  
}

install() {

  if [ $install_status_vel -eq 0 ]; then
    echo -e "${BLUE}[1/$total_progress] ${NC}Uninstall Docker..."
    figlet Uninstall Docker
    uninstall_docker
  else
    echo -e "${RED}[1/$total_progress] ${NC}Failed to uninstall Docker due to install_status_vel = 1"
  fi

  if [ $install_status_vel -eq 0 ]; then
    echo -e "${BLUE}[2/$total_progress] ${NC}Install Docker..."
    figlet Install Docker
    install_docker 
  else
    echo -e "${RED}[2/$total_progress] ${NC}Failed to install Docker due to install_status_vel = 1"
  fi
    
  if [ $install_status_vel -eq 0 ]; then
    echo -e "${BLUE}[3/$total_progress] ${NC}Install Docker Compose...."
    figlet Install 
    figlet Docker Compose
    sudo apt install docker-compose -y
  else
    echo -e "${RED}[3/$total_progress] ${NC}Failed to install Docker Compose due to install_status_vel = 1"
  fi
}

install

run_server() {
  if [ $install_status_vel -eq 0 ]; then
    echo -e "${BLUE}[4/$total_progress] ${NC}Run AEYE Web Server"
    cd Docker && sudo docker-compose up
  else
    echo -e "${RED}[4/$total_progress] ${NC}Failed to Run AEYE Web Server due to install_status_vel = 1"
  fi
  
}

run_server
