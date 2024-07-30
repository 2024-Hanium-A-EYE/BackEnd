#!/bin/bash

RED='\033[38;5;196m'
GREEN='\033[38;5;82m'
YELLOW='\033[38;5;226m'
BLUE='\033[38;5;81m'
NC='\033[0m' # No Color (Defualt colour)

##################################################################
install_status_VAR=1

total_progress=2

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
    install_status_VAR=0
    echo "System package list updated successfully."
    echo -e "${BLUE}[0/$total_progress] ${NC}Install figlet..."
    sudo apt install figlet -y
    
    if [ $? -eq 0 ]; then
      clear
      print_AEYE_WEB
    else
      install_status_VAR=1
      echo -e "${RED}[0/$total_progress] Failed to install." ${NC}
    fi
    
  else
    echo ${RED}"Failed to update system package list."${NC}
  fi
}

initialize_system

########################################################################

intialize_docker_install () {
  sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
  
  curl -fsSL https://get.docker.com -o docker-install.sh

  if [ $? -eq 0 ]; then
    echo -e "${BLUE}[1/$total_progress] ${NC}Docker install initialization Succeed."
  else
    install_status_VAR=1
    echo -e "${RED}[1/$total_progress] ${NC}Dokcer install initialization Failed."
  fi
}

install_docker () {
  intialize_docker_install
  
  sudo apt update
  if [ $? -eq 0 ]; then
    sh ./docker-install.sh --dry-run    

    # Create the docker group.
    sudo groupadd docker
  else
    install_status_VAR=1
    echo -e "${RED}[1/$total_progress] ${NC}Failed to install docker"
  fi
  
}

install() {

  if [ $install_status_VAR -eq 0 ]; then
    echo -e "${BLUE}[1/$total_progress] ${NC}Install Docker..."
    figlet Install Docker
    install_docker 
  else
    echo -e "${RED}[1/$total_progress] ${NC}Failed to install Docker due to install_status_VAR = 1"
  fi
    
}

install

########################################################################

run_server() {

  if [ $install_status_VAR -eq 0]; then
    echo -e "${BLUE}[2/$total_progress] ${NC} running server..."
    figlet AEYE Server
    cd Docker && docker-compose up -d
  else
    echo -e "${RED}[2/$total_progress] ${NC}Failed to run server"
  fi

}

run_server
