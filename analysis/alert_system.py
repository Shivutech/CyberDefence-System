suspicious_ips = set()
attack_count = 0

def check_alert(ip, status):

    global attack_count

    if "Suspicious" in status:

        suspicious_ips.add(ip)
        attack_count += 1

        print("🚨 ALERT: Possible Attack Detected!")
        print("Suspicious IP:", ip)
        print("Total Attacks:", attack_count)
        print("----------------------")