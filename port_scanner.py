%%writefile port_scanner.py

#Import libraries
import socket
import csv


# Function to scan ports
def scan_ports(target, start_port=1, end_port=1024, output_file="scan_results.csv"):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    
    results = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # half-second timeout
        result = sock.connect_ex((target, port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            status = "OPEN"
        else:
            service = "-"
            status = "CLOSED"
        
        results.append([port, status, service])
        sock.close()
    
    # Save results to CSV
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Port", "Status", "Service"])
        writer.writerows(results)
    
    print(f"Scan complete. Results saved to {output_file}")
    return results

# Example run
target_host = "scanme.nmap.org"   # Practice host provided by Nmap
scan_results = scan_ports(target_host, 1, 1024, "scan_results.csv")

# Preview first 10 results
for row in scan_results[:10]:
    print(row)

#Downloading the csv file created
from google.colab import files
files.download("scan_results.csv")
