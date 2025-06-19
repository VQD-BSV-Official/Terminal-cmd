def get_short_path(): # Rút ngắn đường dẫn nếu trên 4
    current_path = os.getcwd()
    parts = current_path.split(os.sep)
    if len(parts) >= 4:
        shortened = f"{parts[0]}{os.sep}..{os.sep}{parts[-2]}{os.sep}{parts[-1]}"
    else:
        shortened = current_path

    return shortened
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os

from rich.console import Console
from DEF import execute_command

import getpass, socket

username = getpass.getuser()
hostname = socket.gethostname()


console = Console(force_terminal=True)
execute_command.run('cls') # create_panel.run()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
while True:     
    prompt = f"╭─[{username}@{hostname} ~ {get_short_path()}]\n╰──❯ "
    # Or cutsome
    # prompt = f"╭─[BSVQDai2278@vqd-bsv ~ {get_short_path()}]\n╰──❯ "

    cmd = input(prompt).strip()
    if cmd.lower() in ["exit", "quit"]:
        break

    execute_command.run(cmd)