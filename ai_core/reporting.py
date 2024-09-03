# ai_core/reporting.py

import os

class Reporting:
    def __init__(self, ai):
        self.ai = ai

    def generate_report(self, args):
        session_name = self.ai.session_manager.active_session or "default_session"
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)
        report_file = os.path.join(report_dir, f"report_{session_name}.txt")
        
        with open(report_file, 'w') as f:
            f.write(f"Report for session: {session_name}\n")
            f.write("=====================================\n")
            actions = self.ai.logging_manager.get_session_actions()
            if not actions:
                f.write("No actions recorded in this session.\n")
            else:
                for action in actions:
                    f.write(f"{action['timestamp']}: {action['description']}\n")

        self.ai.logging_manager.log_info(f"Report generated: {report_file}")
        return f"Report generated: {report_file}"
