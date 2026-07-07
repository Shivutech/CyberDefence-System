from scapy.all import sniff
from analysis.feature_extractor import save_packet
from analysis.detect_attack import detect
from analysis.alert_system import check_alert
from analysis.ip_blocker import block_ip

def process_packet(packet):

    if packet.haslayer("IP"):

        src = packet["IP"].src
        dst = packet["IP"].dst
        size = len(packet)
        protocol = packet["IP"].proto

        print("Source:", src)
        print("Destination:", dst)
        print("Size:", size)
        print("Protocol:", protocol)

        result = detect(size, protocol)
        status = detect(size, protocol)

        print("Traffic Status:", status)
        if "Suspicious" in status:
          block_ip(src)

        check_alert(src, status)

        print("Traffic Status:", result)
        print("----------------------")

        save_packet(src, dst, size, protocol)


def start_capture():

    print("Packet Capture Started")

    sniff(prn=process_packet, store=False ,iface="Wi-Fi")

