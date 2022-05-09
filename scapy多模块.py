from scapy.all import *
pkt=Ether()/IP()/TCP()
ls(pkt)
