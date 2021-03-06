#!/bin/bash
BLACK='\e[0;30m'
BLUE='\e[0;34m'
GREEN='\e[0;32m'
CYAN='\e[0;36m'
RED='\e[0;31m'
PURPLE='\e[0;35m'
BROWN='\e[0;33m'
LIGHTGRAY='\e[0;37m'
DARKGRAY='\e[1;30m'
LIGHTBLUE='\e[1;34m'
LIGHTGREEN='\e[1;32m'
LIGHTCYAN='\e[1;36m'
LIGHTRED='\e[1;31m'
LIGHTPURPLE='\e[1;35m'
YELLOW='\e[1;33m'
WHITE='\e[1;37m'
NC='\e[0m'              
NC='\e[0m'              

clear
	
    echo -e "${GREEN}  +------------------------------------------------------------------+ " 
    echo -e "${LIGHTBLUE}  # ${RED}Version${GREEN} 1.2${LIGHTBLUE} |${CYAN}           Theseus Menu    ${LIGHTBLUE}                         # "
	echo -e "${LIGHTBLUE}  # ------------          --------------------                       # "
    echo -e "${LIGHTBLUE}  #${CYAN}                          Auto installer${LIGHTBLUE}                          # "
	echo -e "${LIGHTBLUE}  #                          --------------                          # "
	echo -e "${LIGHTBLUE}  #${CYAN}                              Enjoy${LIGHTBLUE}                               # "
	echo -e "${LIGHTBLUE}  #                              -----                               # "
	echo -e "${LIGHTBLUE}  #${CYAN}                      Press Enter For Launch${LIGHTBLUE}                      # "
    echo -e "${GREEN}  +------------------------------------------------------------------+ "
    	
echo -e "${LIGHTBLUE}Press Enter To Start Installing Perl On YourServer!"
read enter
yum install perl -y

clear

echo -e "${LIGHTBLUE}Press Enter To Start The Update Of Your Server!"
read enter
yum update -y

clear

echo -e "${LIGHTBLUE}Press Enter To Start DSTAT Installer !"
read enter
yum install dstat -y

clear

echo -e "${LIGHTBLUE}Press Enter To Start CPAN Installer !"
read enter
yum install cpan -y

clear

echo -e "${LIGHTBLUE}Press Enter To Start GCC Installer !"
read enter
yum install gcc -y

clear

echo -e "${LIGHTBLUE}Press Enter To Start Time::HiRes Installer !"
read enter
cpan force install Time::HiRes

clear


echo -e "${LIGHTBLUE}Press Enter To Start Net::RawIP Installer !"
read enter
cpan force install Net::RawIP

clear

echo -e "${LIGHTBLUE}Finish ! You Can Exit (Press Enter)"
read enter
chmod 777 *
./beta
