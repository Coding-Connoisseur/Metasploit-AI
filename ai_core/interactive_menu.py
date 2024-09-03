# ai_core/interactive_menu.py

class InteractiveMenu:
    def __init__(self, ai):
        self.ai = ai

    def show_main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Run Exploit")
            print("2. Scan Target")
            print("3. Manage Sessions")
            print("4. Generate Report")
            print("5. Exit Menu")
            choice = input("Select an option: ")
            if choice == "1":
                self.run_exploit_menu()
            elif choice == "2":
                self.scan_target_menu()
            elif choice == "3":
                self.manage_sessions_menu()
            elif choice == "4":
                self.generate_report_menu()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def run_exploit_menu(self):
        target = input("Enter the target: ")
        exploit = input("Enter the exploit type (sql_injection, xss, directory_traversal): ")
        print(self.ai.exploit_framework.run_exploit([exploit, target]))

    def scan_target_menu(self):
        target = input("Enter the target: ")
        print(self.ai.vulnerability_scanner.scan_target([target]))

    def manage_sessions_menu(self):
        action = input("Enter session action (save, load, list, delete): ")
        name = input("Enter session name: ") if action in ["save", "load", "delete"] else None
        print(self.ai.session_manager.handle_session_command([action, name]))

    def generate_report_menu(self):
        print(self.ai.reporting.generate_report([]))
