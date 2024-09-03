# ai_core/reporting_manager.py

import os
import json

class ReportingManager:
    def __init__(self, ai):
        self.ai = ai
        self.reports_dir = "reports"
        os.makedirs(self.reports_dir, exist_ok=True)

    def generate_report(self, session_name):
        report_file = os.path.join(self.reports_dir, f"report_{session_name}.json")
        actions = self.ai.logging_manager.get_session_actions()
        report_data = {
            "session_name": session_name,
            "actions": actions,
            "analysis": self.analyze_actions(actions)
        }
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=4)
        self.ai.logging_manager.log_info(f"Report generated: {report_file}")
        return report_file

    def analyze_actions(self, actions):
        # Perform some basic analysis on the actions taken
        successful_exploits = [a for a in actions if "Exploit result: Success" in a['description']]
        failed_exploits = [a for a in actions if "Exploit result: Failure" in a['description']]
        return {
            "total_actions": len(actions),
            "successful_exploits": len(successful_exploits),
            "failed_exploits": len(failed_exploits),
            "success_rate": len(successful_exploits) / len(actions) if actions else 0
        }
