from scapy.all import *
pkt=IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
ls(pkt)