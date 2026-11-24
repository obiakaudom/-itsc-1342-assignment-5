# [OBIAKA UDOM] - Assignment 5

def sanitize_ip_list(ip_list, blocked_ip):
    # TODO: Clean up the IP list according to the prompt instructions.
    # Note: Pay close attention to how items are iterated or removed!
    clean_list = []
    for ip in ip_list:
        if ip == blocked_ip:
            continue                      # skip it; never touch ip_list
        elif "invalid" in ip:
            clean_list.append("0.0.0.0")
        else:
            clean_list.append(ip)
    return clean_list