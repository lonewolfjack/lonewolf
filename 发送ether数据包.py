from scapy.all import *
pkt=IP(dst="192.168.1.1")/ICMP()
sendp(Ether(dst="ff:ff:ff:ff:ff:ff"))#发送数据包给ether（只发送）