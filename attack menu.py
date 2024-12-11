from scapy.all import *

def simulate_attack(target_ip, mac_address, protocol, port, payload_size):
    try:
        pkt = None

        if protocol.upper() == "TCP":
            pkt = Ether(src=mac_address) / IP(dst=target_ip) / TCP(dport=port) / Raw(load="X" * payload_size)
        elif protocol.upper() == "UDP":
            pkt = Ether(src=mac_address) / IP(dst=target_ip) / UDP(dport=port) / Raw(load="X" * payload_size)
        elif protocol.upper() == "ICMP":
            pkt = Ether(src=mac_address) / IP(dst=target_ip) / ICMP() / Raw(load="X" * payload_size)
        elif protocol.upper() == "CUSTOM":
            # Custom protocol example
            pkt = Ether(src=mac_address) / IP(dst=target_ip) / Raw(load="CUSTOMPAYLOAD")
        else:
            raise ValueError("Unsupported protocol. Use TCP, UDP, ICMP, or CUSTOM.")

        sendp(pkt, verbose=False)
        print(f"Packet sent to {target_ip} with MAC {mac_address}, protocol {protocol}, port {port}, payload size {payload_size} bytes.")

    except Exception as e:
        print(f"Error: {e}")

# Menu interaktif seperti game lama
def main_menu():
    print("============================")
    print("  WELCOME TO ATTACK SIMULATOR")
    print("============================")
    print("  Select your options:")

    # Input target IP and MAC Address
    target_ip = input("Enter target IP address: ")
    mac_address = input("Enter target MAC address: ")

    # Protocol selection
    print("\nSelect Protocol:")
    print("1. TCP")
    print("2. UDP")
    print("3. ICMP")
    print("4. CUSTOM")

    protocol_choice = input("Enter the protocol number (1-4): ")
    protocol_map = {"1": "TCP", "2": "UDP", "3": "ICMP", "4": "CUSTOM"}
    protocol = protocol_map.get(protocol_choice, "TCP")

    # Port input (optional for ICMP or CUSTOM)
    if protocol in ["TCP", "UDP"]:
        port = int(input("Enter target port (0-65535): "))
    else:
        port = 0

    # Payload size input
    payload_size = int(input("Enter payload size (in bytes): "))

    # Simulate attack
    simulate_attack(target_ip, mac_address, protocol, port, payload_size)

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("\nDo you want to send another packet? (yes/no): ")
        if choice.lower() != "yes":
            print("Exiting Attack Simulator. Stay safe!")
            break
