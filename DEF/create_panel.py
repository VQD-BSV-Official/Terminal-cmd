def get_system_info():
    os_info = f"{platform.system()} {platform.release()} {platform.machine()}" # OS system

    ram = psutil.virtual_memory() # Thông in ram, >> là bitwise right shift
    ram_info = f"{ram.used >> 30:.2f} / {ram.total >> 30:.2f}  GiB ({ram.percent}%)"

    disk = psutil.disk_usage('/') # Thông in ổ cứng, >> là bitwise right shift
    disk_info = f"{disk.used >> 30:.2f} / {disk.total >> 30:.2f} GiB ({disk.percent}%)"

    # Lấy ngày giờ                      days, month, year - hours, min, s
    current_time = datetime.now().strftime("%d/%m/%Y - %I:%M %p") + f" ({['Mo - T2', 'Tu - T3', 'We - T4', 'Th - T5', 'Fr - T6', 'Sa - T7', 'Su - CN'][datetime.now().weekday()]})"

    # Lấy thời gian hoạt động
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    uptime_now = f"{uptime.days} Days, {uptime.seconds // 3600} hours, {(uptime.seconds % 3600) // 60} mins"

    return os_info, ram_info, disk_info, current_time, uptime_now

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():
    os_info, ram_info, disk_info, current_time, uptime_now = get_system_info()
    space = ' ' * 40
    banner = f"""[#A0D8FF]
  ██╗    ██╗██╗         ██╗         [bold cyan]Vu Quang Dai ^_^ Bevis Vu(nickname)[/bold cyan]
 ██╔╝   ██╔╝╚██╗     ██╗╚██╗        _________
██╔╝   ██╔╝  ╚██╗    ╚═╝ ██║        [white][purple]OS[/purple]: {os_info} [/white]
╚██╗  ██╔╝   ██╔╝    ██╗ ██║        [white][purple]Uptime[/purple]: {uptime_now} [/white]
 ╚██╗██╔╝   ██╔╝     ╚═╝██╔╝        [white][purple]Memory[/purple]: {ram_info} [/white]
  ╚═╝╚═╝    ╚═╝         ╚═╝         [white][purple]Disk (C:)[/purple]: {disk_info} [/white]
[/#A0D8FF]"""

    # ////////////////////////////////////////////////////////
    return banner

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
def run():
    console.print(main())

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import platform, psutil

from datetime import datetime
from rich.panel import Panel
from rich.console import Console


console = Console(force_terminal=True)