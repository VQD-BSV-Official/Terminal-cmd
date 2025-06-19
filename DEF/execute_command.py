def resolve_shortcut(lnk_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(lnk_path)
    return shortcut.TargetPath  # Lấy đường dẫn thực tế của file thực thi

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main(cmd):
    if not cmd.strip():
        return
    try:
        if cmd.lower() == "cls" or cmd.lower() == "clear":
            console.clear()
            create_panel.run()
            print("\n")

        # //////////////////////////////////////////////////////////////////
        elif cmd.lower() == "dir" or cmd.lower() == "ls" or cmd.lower() == "dir /a":
            show_dir.run()
            print("\n")

        # //////////////////////////////////////////////////////////////////
        elif cmd.lower().startswith("type ") or cmd.lower().startswith("cat "):

            if cmd.lower().startswith("cat "):
                parts = cmd[4:].strip()
                show_type.run(f'type {parts}', parts) 

            else: 
                parts = cmd[5:].strip()
                show_type.run(cmd, parts) 

        # //////////////////////////////////////////////////////////////////
        elif cmd.lower().startswith("cd "):
            path = cmd[3:].strip()
            os.chdir(path)

        # //////////////////////////////////////////////////////////////////
        elif cmd.lower().startswith("hex"):
            parts = cmd[4:].strip().split(maxsplit=1)

            if len(parts) < 1:
                console.print("Please try again. Ex: hex [Number of bytes or 'all'] [path]\n", style="red", markup=False)
                return

            file_path = parts[1] if len(parts) > 1 else None
            if parts[0] == 'all':
                with open(file_path, "rb") as f: # Đọc so byte từ file
                    data = f.read()  

            else:
                number_of_bytes = int(parts[0])
                with open(file_path, "rb") as f: # Đọc so byte từ file
                    data = f.read(number_of_bytes)

            



            # //////////////////////////////////////////////////////////////////
            mv = memoryview(data)
            for i in range(0, len(mv), 16):
                chunk = mv[i:i + 16]
                hex_part = ' '.join(f"{b:02X}" for b in chunk)
                ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                # result.append(f"0x{i:04X}:  {hex_part:<47}  |  {ascii_part}  |")
                console.print(f"0x{i:08X}:  {hex_part:<47}  |  {ascii_part}  |")

            # console.print("\n".join(result))

        # //////////////////////////////////////////////////////////////////
        elif cmd.lower().startswith("run"):
            # Tách lệnh thành tên shortcut và file
            parts = cmd[4:].strip().split(maxsplit=1)
            if len(parts) < 1:
                console.print("Please try again. Ex: run abc.lnk [path]\n", style="red", markup=False)
                return

            lnk_name = parts[0]
            file_to_open = parts[1] if len(parts) > 1 else None
            
            lnk_path = os.path.join(os.getcwd(), lnk_name)
            if os.path.exists(lnk_path) and lnk_name.lower().endswith(".lnk"):
                # Giải mã shortcut để lấy đường dẫn đến file thực thi
                exe_path = resolve_shortcut(lnk_path)
                if os.path.exists(exe_path):
                    if file_to_open and os.path.exists(os.path.join(os.getcwd(), file_to_open)):
                        # Gọi file thực thi với tham số là file cần mở
                        subprocess.run([exe_path, os.path.join(os.getcwd(), file_to_open)], check=True)
                        while True:
                            break

                    else:
                        # Chạy shortcut mà không mở file nếu không có file được chỉ định
                        os.startfile(lnk_path)
                        while True:
                            break
                else:
                    console.print(f"[red]Không tìm thấy file thực thi từ shortcut {lnk_name}.[/red]")
            else:
                console.print(f"[red]Không tìm thấy shortcut {lnk_name} trong thư mục hiện tại.[/red]")

        else:
            # Sử dụng subprocess.Popen để chạy lệnh và in kết quả liên tục
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', bufsize=1)

            # Đọc stdout và stderr theo thời gian thực
            while process.poll() is None:
                # Đọc stdout
                stdout_line = process.stdout.readline()
                if stdout_line:
                    console.print(stdout_line.rstrip())

                # Đọc stderr
                stderr_line = process.stderr.readline()
                if stderr_line:
                    console.print(stderr_line.rstrip(), style="red")

            # Đọc các dòng còn lại sau khi lệnh kết thúc
            for stdout_line in process.stdout:
                console.print(stdout_line.rstrip())
            for stderr_line in process.stderr:
                console.print(stderr_line.rstrip(), style="red")

            # Kiểm tra mã lỗi
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, cmd)


                
    except subprocess.CalledProcessError as e:
        console.print(f"[red]{e.stderr}[/red]")
    except Exception as e:
        console.print(f"[red]{str(e)}[/red]")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def run(cmd):
    main(cmd)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os, subprocess
import win32com.client   # Để giải mã shortcut .lnk

from . import show_dir, create_panel
from . import show_type

from rich.console import Console

console = Console(force_terminal=True)