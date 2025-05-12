import psutil
import platform
import socket

def get_ram():
    # Returns (total, available) RAM in MB
    vm = psutil.virtual_memory()
    return (vm.total // (1024 * 1024), vm.available // (1024 * 1024))

def get_process_count():
    return len(psutil.pids())

def get_up_stats():
    # Returns (uptime in minutes, dummy load average)
    uptime_seconds = psutil.boot_time()
    from datetime import datetime
    now = datetime.now().timestamp()
    uptime_minutes = int((now - uptime_seconds) // 60)
    return (f"{uptime_minutes} minutes", 0.0)

def get_connections():
    return len([c for c in psutil.net_connections() if c.status == psutil.CONN_ESTABLISHED])

def get_temperature():
    # Windows typically has no access to CPU temp
    try:
        import subprocess
        output = subprocess.check_output(['/usr/bin/vcgencmd','measure_temp']).decode()
        return float(output.split('=')[1][:-3])
    except:
        return 42.0  # dummy temp

def get_ipaddress():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "Unknown"

def get_cpu_speed():
    try:
        return psutil.cpu_freq().current
    except:
        return 0

# Test output (safe to comment out in production)
print('Free RAM: ' + str(get_ram()[1]) + ' MB (' + str(get_ram()[0]) + ' MB total)')
print('Number of processes: ' + str(get_process_count()))
print('Up time: ' + get_up_stats()[0])
print('Number of connections: ' + str(get_connections()))
print('Temperature in C: ' + str(get_temperature()))
print('IP-address: ' + get_ipaddress())
print('CPU speed in MHz: ' + str(get_cpu_speed()))
