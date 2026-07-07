import os

blocked_ips = set()

def block_ip(ip):

    if ip not in blocked_ips:

        command = f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}'

        os.system(command)

        blocked_ips.add(ip)

        print("🔥 IP BLOCKED:", ip)