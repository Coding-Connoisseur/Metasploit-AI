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
                return self.ai.advanced_exploitation.run_exploit(args[1:])
            else:
                return "No exploit specified."
        elif cmd == "multi_exploit":
            if len(args) > 1:
                return self.ai.multi_stage_exploit.run_multi_stage_exploit(args[1:])
            else:
                return "No multi-stage exploit specified."
        elif cmd == "vuln_check":
            if len(args) > 1:
                return self.ai.vulnerability_database.check_vulnerabilities(args[1:])
            else:
                return "No target specified for vulnerability check."
        elif cmd == "post_exploit":
            if len(args) > 1:
                return self.ai.post_exploitation.perform_post_exploit(args[1:])
            else:
                return "No target specified for post-exploitation."
        elif cmd == "report":
            return self.ai.reporting.generate_report(args[1:])
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
        exploit <type> <target>     : Execute an advanced exploit on a target.
        multi_exploit <target>      : Execute a multi-stage exploit on a target.
        vuln_check <target>         : Check the target against a vulnerability database.
        post_exploit <target>       : Perform post-exploitation techniques.
        report                      : Generate a detailed report of the session.
        =========================================
        """
        return help_text