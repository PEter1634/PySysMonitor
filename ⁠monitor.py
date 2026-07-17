import time
import os
import psutil

def monitor_system(interval=5):
    print("Starting PySysMonitor...")
    print("Press Ctrl+C to stop.\n")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            log_entry = (
                f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"CPU: {cpu_usage}% | "
                f"RAM: {memory.percent}% | "
                f"Disk: {disk.percent}%"
            )
            print(log_entry)

            # Save logs to a file
            with open("system_log.txt", "a") as f:
                f.write(log_entry + "\n")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_system()
