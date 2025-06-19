def main():
    tree = Tree(f"[bold cyan]{os.path.basename(os.getcwd()) or '/'}")
    # Tìm độ dài tối đa của tên tệp và dung lượng để căn chỉnh
    max_name_length = max(len(item) for item in os.listdir())
    max_size_length = max(len(f"{os.path.getsize(os.path.join(os.getcwd(), item)):,}") for item in os.listdir() if not os.path.isdir(os.path.join(os.getcwd(), item)))
    
    for item in os.listdir():
        path = os.path.join(os.getcwd(), item)
        
        creation_time = os.path.getmtime(path) # Lấy thời gian chỉnh sửa | getctime -> Lấy ngày tạo và định dạng
        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

        if os.path.isdir(path):
            # Căn chỉnh tên thư mục
            name_str = f"{item}/".ljust(max_name_length + 1)  # +1 để tính dấu /
            tree.add(f"[green]{name_str}| {creation_date}[/green]")
        else:
            size = os.path.getsize(path)
            # Định dạng dung lượng sao cho thẳng hàng
            size_str = f"{size:,}".rjust(max_size_length)
            # Căn chỉnh tên tệp
            if ".lnk" in item.lower():
                name_str = f"{item}/".ljust(max_name_length)
                tree.add(f"[purple]{name_str} | {creation_date} | {size_str} bytes[/purple]")
            else:
                name_str = item.ljust(max_name_length)
                tree.add(f"[white]{name_str} | {creation_date} | {size_str} bytes[/white]")

    console.print(tree)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def run():
    main()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os
from datetime import datetime
from rich.tree import Tree
from rich.console import Console

console = Console(force_terminal=True)

