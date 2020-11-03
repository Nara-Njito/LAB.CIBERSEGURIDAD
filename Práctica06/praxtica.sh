#!/bin/bash

rpri=$(hostname -I)

nmap $rpri | base64 >result.txt

rpu=$(curl ifconfig.me)

nmap $rpu | base64 >>result.txt

nmap scanme.nmap.org | base64 >>result.txt

