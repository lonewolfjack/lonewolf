from scapy.all import  IP,ls
pkt=IP(dst="192.168.0.100")
ls(pkt)