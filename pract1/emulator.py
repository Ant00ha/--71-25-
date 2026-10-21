import socket
import getpass
import shlex
import argparse
import csv
import zipfile
from datetime import datetime
import sys

# VFS в памяти
vfs_paths = []
current_dir = "" 

def load_vfs(zip_path):
    
    global vfs_paths
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            vfs_paths = z.namelist()
    except Exception:
        
        print(f"Архив '{zip_path}' не найден. Загружена тестовая файловая система.")
        vfs_paths = ["Documents/", "Documents/file.txt", "Downloads/", "Pictures/"]

def get_invitation():
    hostname = socket.gethostname()
    username = getpass.getuser()
    display_dir = f"~/{current_dir.rstrip('/')}" if current_dir else "~"
    return f"{username}@{hostname}:{display_dir}$ "

def log_event(log_path, command, cmd_args, error_msg=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, command, " ".join(cmd_args), error_msg])
    except Exception:
        pass 

def cmd_cd(cmd_args):
    global current_dir
    if not cmd_args or cmd_args[0] == "~":
        current_dir = ""
        return ""
    
    target = cmd_args[0]
    
    if target == "..":
        if current_dir:
            parts = current_dir.rstrip('/').split('/')
            current_dir = "/".join(parts[:-1]) + "/" if len(parts) > 1 else ""
        return ""
    
    new_dir = current_dir + target.strip('/') + '/'
    
    if any(p.startswith(new_dir) for p in vfs_paths):
        current_dir = new_dir
        return ""
    else:
        return f"cd: {target}: Нет такого каталога"

def cmd_ls(cmd_args):
    items = set()
    for p in vfs_paths:
        if p.startswith(current_dir) and p != current_dir:
            rest = p[len(current_dir):]
            top_level_item = rest.split('/')[0]
            items.add(top_level_item)
    
    if items:
        print("  ".join(sorted(items)))
    return ""

def execute_command(user_input, log_path):
    if not user_input.strip():
        return True, False

    try:
        parsed = shlex.split(user_input)
        command, cmd_args = parsed[0], parsed[1:]
    except ValueError as e:
        error_msg = f"Ошибка синтаксиса: {e}"
        print(error_msg)
        log_event(log_path, "SYNTAX_ERROR", [], error_msg)
        return True, True

    error_msg = ""
    should_continue = True

    if command == "exit":
        should_continue = False
    elif command == "cd":
        error_msg = cmd_cd(cmd_args)
        if error_msg: 
            print(error_msg)
    elif command == "ls":
        error_msg = cmd_ls(cmd_args)
    else:
        error_msg = f"{command}: команда не найдена"
        print(error_msg)
    
    log_event(log_path, command, cmd_args, error_msg)
    return should_continue, bool(error_msg)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--vfs', default='vfs.zip', help="Путь к ZIP-архиву VFS")
    parser.add_argument('--log', default='log.csv', help="Путь к лог-файлу (CSV)")
    parser.add_argument('--script', default=None, help="Путь к стартовому скрипту")
    args = parser.parse_args()

    load_vfs(args.vfs)

    
    if args.script:
        try:
            with open(args.script, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    
                    print(f"{get_invitation()}{line}")
                    should_continue, has_error = execute_command(line, args.log)
                    
                    if has_error or not should_continue:
                        break 
        except FileNotFoundError:
            pass

    
    while True:
        try:
            user_input = input(get_invitation())
            should_continue, _ = execute_command(user_input, args.log)
            if not should_continue:
                break 
        except (EOFError, KeyboardInterrupt):
            print("\nexit")
            break

if __name__ == "__main__":
    main()
