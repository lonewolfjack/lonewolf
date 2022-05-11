from scapy.all import *
prind    （开始）
pkt=  IP  (dst="192.168.1.1")/ICMP()#发送数据包给IP(只发送)
send (pkt)