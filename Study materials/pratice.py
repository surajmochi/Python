log_data = """
192.168.1.10 - - [07/Nov/2025:10:15:32] "GET /index.html HTTP/1.1" 200 1024
192.168.1.11 - - [07/Nov/2025:10:16:01] "POST /login.php HTTP/1.1" 401 512
192.168.1.12 - - [07/Nov/2025:10:16:33] "GET /dashboard HTTP/1.1" 200 2048
"""

print("=== Raw log data ===")
print(log_data)

log = log_data.strip().split('\n')  # strip() removes leading/trailing spaces/newlines
print("\n Raw Log Data===")
print(log)

#loop through each log line and extract details
for log in logs:
    #use slicing & splitting to extract details
    ip = log[:log.find(' ')] # slice till first space -> IP Address