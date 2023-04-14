#02:
'''
This script will craft a TCP SYN packet with some custom options and send it to the IP address 192.168.1.1 on port 80.

These are just a few examples of what you can do with Scapy. For more information and advanced usage, check out the official Scapy documentation.
'''

from scapy.all import *

ip = IP(src="192.168.1.2", dst="192.168.1.1")
tcp = TCP(sport=12345, dport=80, flags="S", options=[("MSS", 1460), ("NOP", None), ("WScale", 10)])

'''
We're creating a new packet that consists of an IP layer (ip) and a TCP layer (tcp).
The / operator is used to concatenate these layers together into a single packet.
'''
pkt = ip/tcp

# add payload
# data = "Hello, world!"
# pkt = ip/tcp/Raw(load=data)

send(pkt)