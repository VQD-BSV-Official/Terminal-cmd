def highlight_file(code, parts):
    try:
        # Thử đoán ngôn ngữ dựa trên nội dung
        lexer = guess_lexer(code)
        language = lexer.aliases[0]  # Lấy bí danh đầu tiên
        # print(f"Ngôn ngữ đoán được: {lexer.name} (bí danh: {language})")
    except ClassNotFound:
        # Nếu không đoán được dựa trên nội dung, thử dựa trên phần mở rộng file
        try:
            lexer = guess_lexer_for_filename(file_path, code)
            language = lexer.aliases[0]  # Lấy bí danh đầu tiên
        except ClassNotFound:
            language = "text"  # Mặc định nếu không đoán được
    
    # Tô sáng cú pháp với bí danh đã xác định
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title=f"Content of {os.path.basename(parts)}", border_style="yellow"))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main(cmd, parts):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8' ,check=True)
    # Tạo đối tượng Syntax để tô màu cú pháp
    highlight_file(result.stdout, parts)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def run(cmd, parts):
	main(cmd, parts)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os, subprocess

from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.util import ClassNotFound

from rich.panel import Panel
from rich.syntax import Syntax
from rich.console import Console

console = Console(force_terminal=True)