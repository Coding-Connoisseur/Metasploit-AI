# ai_core/command_handler.py

class CommandHandler:
    def __init__(self, ai):
        self.ai = ai

    def execute_command(self, command):
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
        elif cmd == "report":
            return self.ai.reporting.generate_report(args[1:])
        elif cmd == "menu":
            return self.ai.interactive_menu.show_main_menu()
        else:
            return f"Command '{cmd}' is not supported."
    
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
        report                      : Generate a report of the session.
        menu                        : Open the interactive menu.
        =========================================
        """
        return help_text
