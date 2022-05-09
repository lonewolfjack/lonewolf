from scapy.all import *
pkt=IP(dst="192.168.0.1")/ICMP()
ans,uans=sr(pkt)
ans.summary()

#发送一个数据返回一个应答数据包
#sr（）sr1（） 以ip方式发送数据包
#srp（）发送时要使用MAC地址