# ai_core/reporting_manager.py

import os

class ReportingManager:
    def __init__(self, ai):
        self.ai = ai
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)

    def generate_report(self, session_name):
        report_file = os.path.join(self.reports_dir, f"report_{session_name}.txt")
        with open(report_file, 'w') as f:
            f.write(f"Report for session: {session_name}\n")
            f.write("============================\n")
            actions = self.ai.logging_manager.get_session_actions()
            if not actions:
                f.write("No actions recorded in this session.\n")
            else:
                for action in actions:
                    f.write(f"{action['timestamp']}: {action['description']}\n")

        self.ai.logging_manager.log_info(f"Report generated: {report_file}")
        return f"Report generated: {report_file}"

    def list_reports(self):
        return os.listdir(self.reports_dir)
