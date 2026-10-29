
import getpass
import platform
import shutil
import socket
import os
import subprocess


def run_safe_command(args, timeout=3):
    """Run only allowlisted, read-only system commands."""
    allowed_commands = {"uname", "hostname"}

    if not isinstance(args, list) or not args:
        return None

    if args[0] not in allowed_commands:
        print("Blocked: command is not allowed.")
        return None

    try:
        result = subprocess.run(
            args,
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )

        if result.returncode != 0:
            return None

        output = result.stdout.strip()
        return output if output else None

    except FileNotFoundError:
        print(f"Command not found: {args[0]}")
    except subprocess.TimeoutExpired:
        print(f"Command timed out: {args[0]}")
    except OSError as error:
        print(f"Could not run command: {error}")

    return None


def get_hostname():
    return socket.gethostname()


def get_current_user():
    try:
        return getpass.getuser()
    except (OSError, KeyError):
        return "Unable to determine current user"


def get_os_info():
    return f"{platform.system()} {platform.release()}"


def get_kernel_info():
    # uname is available on Linux and most Unix-like systems.
    if platform.system() == "Linux":
        kernel = run_safe_command(["uname", "-r"])
        if kernel:
            return kernel

    # Fallback if uname is unavailable or fails.
    return platform.release() or "Unavailable"


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
    try:
        usage = shutil.disk_usage(os.path.abspath(os.sep))

        total_gb = usage.total / (1024 ** 3)
        used_gb = usage.used / (1024 ** 3)
        free_gb = usage.free / (1024 ** 3)

        return (
            f"Total: {total_gb:.2f} GB | "
            f"Used: {used_gb:.2f} GB | "
            f"Free: {free_gb:.2f} GB"
        )
    except OSError:
        return "Unable to read disk information"


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
            return "Unable to read memory information"

    return "Memory information not supported on this OS"


def main():
    print("=" * 50)
    print("         SYSTEM INFORMATION REPORT")
    print("=" * 50)

    try:
        print(f"Hostname        : {get_hostname()}")
    except OSError:
        print("Hostname        : Unavailable")

    print(f"Current User    : {get_current_user()}")
    print(f"Operating System: {get_os_info()}")
    print(f"Kernel Version  : {get_kernel_info()}")
    print(f"IP Address      : {get_ip_address()}")
    print(f"Disk Usage      : {get_disk_info()}")
    print(f"Memory Usage    : {get_memory_info()}")

    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSystem information check cancelled safely.")
