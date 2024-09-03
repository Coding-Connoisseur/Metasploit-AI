# ai_core/interactive_enum_workflow.py

class InteractiveEnumWorkflow:
    def __init__(self, ai):
        self.ai = ai

    def start(self):
        while True:
            print("\nInteractive Target Enumeration")
            print("1. Basic Scan")
            print("2. Detailed Scan")
            print("3. Vulnerability Scan")
            print("4. Return to Main Menu")
            choice = input("Select an option: ")
            if choice == "1":
                self.basic_scan()
            elif choice == "2":
                self.detailed_scan()
            elif choice == "3":
                self.vulnerability_scan()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def basic_scan(self):
        target = input("Enter the target for basic scan: ")
        print(self.ai.vulnerability_scanner.basic_scan(target))

    def detailed_scan(self):
        target = input("Enter the target for detailed scan: ")
        print(self.ai.vulnerability_scanner.detailed_scan(target))

    def vulnerability_scan(self):
        target = input("Enter the target for vulnerability scan: ")
        print(self.ai.vulnerability_scanner.scan_for_vulnerabilities(target))
