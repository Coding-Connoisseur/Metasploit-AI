# ai_core/custom_command.py

class CustomCommand:
    def __init__(self, ai):
        self.ai = ai
        self.custom_commands = {}

    def add_custom_command(self, args):
        alias = args[0]
        command = " ".join(args[1:])
        self.custom_commands[alias] = command
        self.ai.logging_manager.log_info(f"Added custom command: {alias} -> {command}")
        return f"Custom command '{alias}' added."

    def remove_custom_command(self, args):
        alias = args[0]
        if alias in self.custom_commands:
            del self.custom_commands[alias]
            self.ai.logging_manager.log_info(f"Removed custom command: {alias}")
            return f"Custom command '{alias}' removed."
        else:
            return f"Custom command '{alias}' not found."

    def execute_custom_command(self, alias):
        if alias in self.custom_commands:
            return self.ai.command_handler.execute_command(self.custom_commands[alias])
        else:
            return f"Custom command '{alias}' not found."
