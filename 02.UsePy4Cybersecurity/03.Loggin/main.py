import re

log_file = "example.log"

with open(log_file, "r") as f:
    log_lines = f.readlines()

if len(log_lines) == 0:
    print("Log file is empty.")
else:
    # Count the number of requests by IP address
    ip_counts = {}
    for line in log_lines:
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ip = match.group(1)
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

    print("Request counts by IP address:")
    for ip, count in ip_counts.items():
        print(f"{ip}: {count}")

    # Find the most requested URL
    url_counts = {}
    for line in log_lines:
        match = re.search(r"\"(GET|POST) ([^\s]+)", line)
        if match:
            url = match.group(2)
            if url in url_counts:
                url_counts[url] += 1
            else:
                url_counts[url] = 1

    if len(url_counts) == 0:
        print("\nNo URLs found in log file.")
    else:
        most_requested_url = max(url_counts, key=url_counts.get)
        print(f"\nMost requested URL: {most_requested_url}")
