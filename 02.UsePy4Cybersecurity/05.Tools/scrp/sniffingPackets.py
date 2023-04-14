#01:
'''
This script will capture 10 packets from the network that match the filter "ip" and
print the source and destination IP addresses of each packet.
'''
from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")

sniff(prn=packet_handler, filter="ip", count=10)
