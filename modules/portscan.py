import nmap

def port_scan(target):

    nm = nmap.PortScanner()

    nm.scan(target,"1-1000")

    ports = []

    for host in nm.all_hosts():

        for proto in nm[host].all_protocols():

            for port in nm[host][proto]:

                state = nm[host][proto][port]["state"]

                if state == "open":

                    print("open:",port)

                    ports.append(port)

    return ports
