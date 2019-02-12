#!/usr/bin/env python
# coding: utf-8

# Importation du module scapy + rennommer en "scapy"

import scapy.all as scapy
import parser

# Utilisation de la fonction "scan" pour scanner le réseau

def scan(ip):
    requete_arp = scapy.ARP(pdst=ip)
    print(requete_arp.summary())

# Appelle de la fonction "scan" en analysant le réseau entier

scan("192.168.1.1/24")

print(input)
