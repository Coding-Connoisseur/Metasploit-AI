# ai_core/command_handler.py

import os

class CommandHandler:
    def __init__(self, ai):
        self.ai = ai
        self.history_file = "command_history.txt"
        self.command_history = []
        self.load_history()

    def execute_command(self, command):
        self.command_history.append(command)
        self.save_history()
        self.ai.logging_manager.log_info(f"Executing command: {command}")
        args = command.split()
        if not args:
            return "No command entered."
        
        cmd = args[0]

        if cmd == "cd":
            return self.ai.module_loader.change_directory(args[1:])
        elif cmd == "ls":
            return self.ai.module_loader.list_directory()
        elif cmd == "exec":
            return self.ai.module_loader.execute_module(args[1:])
        elif cmd == "exploit":
            if len(args) > 1:
                return self.ai.exploit_framework.run_exploit(args[1:])
            else:
                return "No exploit specified."
        elif cmd == "scan":
            if len(args) > 1:
                return self.ai.vulnerability_scanner.scan_target(args[1:])
            else:
                return "No target specified for scanning."
        elif cmd == "session":
            if len(args) > 1:
                return self.ai.session_manager.handle_session_command(args[1:])
            else:
                return "No session command specified."
        elif cmd == "history":
            return self.show_history()
        elif cmd == "notify":
            return self.ai.logging_manager.send_notification(args[1:])
        else:
            return f"Command '{cmd}' is not supported."

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                self.command_history = f.read().splitlines()

    def save_history(self):
        with open(self.history_file, 'w') as f:
            f.write("\n".join(self.command_history))

    def show_history(self):
        return "\n".join(self.command_history)

    def show_help(self):
        help_text = """
        =========================================
        AI Framework Help Menu
        =========================================
        cd <directory>              : Change the current directory.
        ls                          : List the contents of the current directory.
        exec <module> <args>        : Execute a specified module.
        exploit <type> <target>     : Execute an exploit on a target.
        scan <target>               : Scan a target for vulnerabilities.
        session <command> <args>    : Manage sessions (save, load, list, delete).
        history                     : Show command history.
        notify <message>            : Send a notification.
        =========================================
        """
        return help_text
