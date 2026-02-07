# from scapy.arch.windows import get_windows_if_list
# from scapy.all import sniff

# packet = sniff(count = 10)

# for iface in get_windows_if_list():
#     print(iface["name"], "=>", iface["description"])

# print('=====================================')
# print(packet)

from scapy.all import sniff,wrpcap,rdpcap

# packet = sniff(count = 20)

# wrpcap("capture.pcap", packet)

packet = rdpcap("capture.pcap")
print(len(packet))
packet[0].show()
