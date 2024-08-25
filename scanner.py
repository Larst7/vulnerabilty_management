import nmap

def run_nmap_scan(target, scan_type='-sS'):
    nm = nmap.PortScanner()
    nm.scan(target, arguments=scan_type)
    scan_results = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                scan_results.append({
                    'host': host,
                    'protocol': proto,
                    'port': port,
                    'state': nm[host][proto][port]['state'],
                    'service': nm[host][proto][port]['name'],
                    'reason': nm[host][proto][port]['reason']
                })
    
    return scan_results
