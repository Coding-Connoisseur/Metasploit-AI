# ai_core/ai.py

import os
from ai_core.command_handler import CommandHandler
from ai_core.module_loader import ModuleLoader
from ai_core.logging_manager import LoggingManager
from ai_core.session_manager import SessionManager
from ai_core.exploit_framework import ExploitFramework
from ai_core.vulnerability_scanner import VulnerabilityScanner
from ai_core.interactive_menu import InteractiveMenu
from ai_core.reporting import Reporting

class SelfLearningAI:
    def __init__(self):
        self.cwd = os.getcwd()
        self.logging_manager = LoggingManager()
        self.module_loader = ModuleLoader(self.logging_manager)
        self.command_handler = CommandHandler(self)
        self.exploit_framework = ExploitFramework(self)
        self.vulnerability_scanner = VulnerabilityScanner(self)
        self.interactive_menu = InteractiveMenu(self)
        self.reporting = Reporting(self)
        self.session_manager = SessionManager(self)
        self.module_loader.load_modules()
        self.module_loader.load_plugins()
    
    def run(self):
        while True:
            try:
                user_input = input("ai> ")
                if user_input == "help":
                    self.command_handler.show_help()
                elif user_input == "menu":
                    self.interactive_menu.show_main_menu()
                else:
                    print(self.command_handler.execute_command(user_input))
            except Exception as e:
                self.logging_manager.log_error(f"Error in main loop: {e}")
                print("An unexpected error occurred. Please check the logs for details.")