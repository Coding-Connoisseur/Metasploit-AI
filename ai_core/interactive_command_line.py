# ai_core/interactive_command_line.py

class InteractiveCommandLine:
    def __init__(self, ai):
        self.ai = ai

    def start(self):
        while True:
            print("\nInteractive Command Line")
            print("1. Run Exploit")
            print("2. Scan Target")
            print("3. View Command History")
            print("4. Manage Sessions")
            print("5. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.run_exploit()
            elif choice == "2":
                self.scan_target()
            elif choice == "3":
                self.view_history()
            elif choice == "4":
                self.manage_sessions()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def run_exploit(self):
        target = input("Enter the target: ")
        exploit = input("Enter the exploit type: ")
        options = input("Enter any options (optional): ").split()
        print(self.ai.exploit_framework.run_exploit([exploit, target] + options))

    def scan_target(self):
        target = input("Enter the target: ")
        print(self.ai.vulnerability_scanner.scan_target([target]))

    def view_history(self):
        print(self.ai.command_handler.show_history())

    def manage_sessions(self):
        action = input("Enter session action (save, load, list, delete, switch): ")
        name = input("Enter session name: ") if action in ["save", "load", "delete", "switch"] else None
        print(self.ai.session_manager.handle_session_command([action, name]))
