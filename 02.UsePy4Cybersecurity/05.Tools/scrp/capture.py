# for crafting
from scapy.all import *

# Define a function to handle incoming packets
def handle_packet(packet):
    print(packet.summary())

# Create a sniffing filter to capture only TCP packets on port 80
filter = "tcp port 80"

# Start sniffing packets using the filter
sniff(filter=filter, prn=handle_packet)
