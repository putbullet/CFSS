import nmap

def scan_ports(target_ip):
    """
    Scan for open ports on the specified IP address using Nmap.

    Args:
        target_ip (str): The IP address to scan for open ports.

    Returns:
        None
    """
    """ Create an instance of the Nmap PortScanner """
    nm = nmap.PortScanner()

    """ Perform the scan on the specified IP address """
    nm.scan(hosts=target_ip, arguments='-p 1-65535 -T4')

    """ Iterate through the scanned hosts and print open ports """
    for host in nm.all_hosts():
        print(f"Open ports for {host}:")
        for PTCL in nm[host].all_protocols():
            ports = nm[host][PTCL].keys()
            for port in ports:
                print(f"Port {port}/{PTCL} is open")

""" Take input from the user """
target_ip = input("Enter the target IP address to scan: ")
scan_ports(target_ip)

