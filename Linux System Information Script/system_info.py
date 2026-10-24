
import getpass
import platform
import shutil
import socket
import os


def get_hostname():
    return socket.gethostname()


def get_current_user():
    return getpass.getuser()


def get_os_info():
    return f"{platform.system()} {platform.release()}"


def get_ip_address():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Determine the local network interface address.
        # No application data is sent.
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        try:
            return socket.gethostbyname(socket.gethostname())
        except OSError:
            return "Unable to determine IP address"
    finally:
        sock.close()


def get_disk_info():
    usage = shutil.disk_usage(os.path.abspath(os.sep))

    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)

    return (
        f"Total: {total_gb:.2f} GB | "
        f"Used: {used_gb:.2f} GB | "
        f"Free: {free_gb:.2f} GB"
    )


def get_memory_info():
    # Linux and WSL
    if platform.system() == "Linux":
        try:
            memory = {}

            with open("/proc/meminfo", "r", encoding="utf-8") as file:
                for line in file:
                    key, value = line.split(":", 1)
                    memory[key] = int(value.strip().split()[0])

            total = memory["MemTotal"]
            available = memory["MemAvailable"]
            used = total - available

            return (
                f"Total: {total / 1024:.2f} MB | "
                f"Used: {used / 1024:.2f} MB | "
                f"Available: {available / 1024:.2f} MB"
            )
        except (OSError, KeyError, ValueError):
            return "Unable to read memory information"

    # Windows
    if platform.system() == "Windows":
        try:
            import ctypes

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]

            status = MEMORYSTATUSEX()
            status.dwLength = ctypes.sizeof(status)

            if ctypes.windll.kernel32.GlobalMemoryStatusEx(
                ctypes.byref(status)
            ):
                total = status.ullTotalPhys / (1024 ** 2)
                available = status.ullAvailPhys / (1024 ** 2)
                used = total - available

                return (
                    f"Total: {total:.2f} MB | "
                    f"Used: {used:.2f} MB | "
                    f"Available: {available:.2f} MB"
                )

        except (AttributeError, OSError):
            pass

    return "Memory information not supported on this OS"


def main():
    print("=" * 50)
    print("         SYSTEM INFORMATION REPORT")
    print("=" * 50)

    print(f"Hostname       : {get_hostname()}")
    print(f"Current User   : {get_current_user()}")
    print(f"Operating System: {get_os_info()}")
    print(f"Kernel Version : {platform.release()}")
    print(f"IP Address     : {get_ip_address()}")
    print(f"Disk Usage     : {get_disk_info()}")
    print(f"Memory Usage   : {get_memory_info()}")

    print("=" * 50)


if __name__ == "__main__":
    main()
